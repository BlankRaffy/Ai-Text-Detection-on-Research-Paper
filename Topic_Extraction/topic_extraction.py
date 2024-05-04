import get_text
import xml.etree.ElementTree as ET
import yake

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import NMF

import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from gensim.corpora import Dictionary
from gensim.models.ldamodel import LdaModel
import get_text
import xml.etree.ElementTree as ET
import re



# Assicurati di aver scaricato i dati necessari per NLTK
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

def yake_extraction(file_path):

    # Configurazione dell'estrattore di parole chiave YAKE
    language = "en"
    max_ngram_size = 3
    deduplication_threshold = 0.9
    numOfKeywords = 6
    custom_kw_extractor = yake.KeywordExtractor(lan=language, n=max_ngram_size, dedupLim=deduplication_threshold, top=numOfKeywords, features=None)

    # Parsing del file XML
    tree = ET.parse(file_path)
    abstract =[]
    intro = []
    conclusion = []

    abstract_txt = get_text.extract_abstract(tree)  
    introduction_txt = get_text.extract_intro(tree)  
    conclusion_txt = get_text.extract_conclusion(tree)  

    abstract_keywords = custom_kw_extractor.extract_keywords(abstract_txt)
    introduction_keywords = custom_kw_extractor.extract_keywords(introduction_txt)
    conclusion_keywords = custom_kw_extractor.extract_keywords(conclusion_txt)

    # Aggiungi le parole estratte al dizionario per l'abstract
    for kw in abstract_keywords:
        abstract.append(kw[0])

    # Aggiungi le parole estratte al dizionario per l'introduzione
    for kw in introduction_keywords:
        intro.append(kw[0])

    # Aggiungi le parole estratte al dizionario per le conclusioni
    for kw in conclusion_keywords:
        conclusion.append(kw[0])

    return abstract,intro,conclusion

def NMF_extraction(file_path):
    tree = ET.parse(file_path)
    vectorizer = TfidfVectorizer(max_features=1000, stop_words='english')
    num_topics = 1
    nmf_model = NMF(n_components=num_topics, random_state=1)
    abstract =[]
    intro = []
    conclusion = []

    abstract = get_text.extract_abstract(tree)
    conclusion = get_text.extract_conclusion(tree)
    introduction= get_text.extract_intro(tree)

    abstract_vector = vectorizer.fit_transform([abstract])
    nmf_model.fit(abstract_vector)

    feature_names = vectorizer.get_feature_names_out()

    topic = nmf_model.components_[0]
    top_words_indices = topic.argsort()[:-6 - 1:-1]  # Get indices of top 6 words
    top_words_abstract = [feature_names[i] for i in top_words_indices]

    abstract = top_words_abstract

    #introducition keyword
    introduction_vector = vectorizer.fit_transform([introduction])
    nmf_model.fit(introduction_vector)

    feature_names = vectorizer.get_feature_names_out()

    topic = nmf_model.components_[0]
    top_words_indices = topic.argsort()[:-6 - 1:-1]  # Get indices of top 6 words
    top_words_introduction = [feature_names[i] for i in top_words_indices]
    intro = top_words_introduction 

    #conclusion keyword
    conclusion_vector = vectorizer.fit_transform([conclusion])
    nmf_model.fit(conclusion_vector)

    feature_names = vectorizer.get_feature_names_out()

    topic = nmf_model.components_[0]
    top_words_indices = topic.argsort()[:-6 - 1:-1]  # Get indices of top 6 words
    top_words_conclusion = [feature_names[i] for i in top_words_indices]

    conclusion = top_words_conclusion
    
    return abstract,intro,conclusion


def LDA_extraction(file_path):
    def preprocess_text(text):
    # Tokenizzazione del testo
        tokens = word_tokenize(text.lower())
    
    # Rimozione delle stopwords e dei caratteri non alfabetici
        tokens = [token for token in tokens if token.isalpha() and token not in stopwords.words('english')]
    
    # Lemmatizzazione delle parole
        lemmatizer = WordNetLemmatizer()
        tokens = [lemmatizer.lemmatize(token) for token in tokens]
    
        return tokens

    def extract_topics_from_text(text, num_topics):
    # Preprocessamento del testo
        preprocessed_text = preprocess_text(text)
    
    # Creazione del dizionario e del corpus per un solo documento
        dictionary = Dictionary([preprocessed_text])
        corpus = [dictionary.doc2bow(preprocessed_text)]
    
    # Creazione e addestramento del modello LDA
        lda_model = LdaModel(corpus, num_topics=num_topics, id2word=dictionary, passes=15)
    
    # Estrazione e stampa dei temi
        topics = lda_model.print_topics()
        return topics[0][1] # we only get the first set of topic

    def extract_keywords(topic_distribution):
    # Utilizza espressioni regolari per trovare le parole tra virgolette e aggiungerle alla lista
        keywords = re.findall(r'"(.*?)"', topic_distribution)
        return keywords

# Testiamo la funzione con un singolo testo di input
    tree = ET.parse(file_path)
    abstarct =[]
    intro = []
    conclusion = []


    abstract_text = get_text.extract_conclusion(tree)
    raw_topic = extract_topics_from_text(abstract_text, num_topics=1)
    abstarct.append(extract_keywords(raw_topic))


    intro_text = get_text.extract_intro(tree)
    raw_topic = extract_topics_from_text(intro_text, num_topics=1)
    intro.append(extract_keywords(raw_topic))


    conclusion_text = get_text.extract_intro(tree)
    raw_topic = extract_topics_from_text(conclusion_text, num_topics=1)
    conclusion.append(extract_keywords(raw_topic))

    return abstarct[0][:6], intro[0][:6], conclusion[0][:6]