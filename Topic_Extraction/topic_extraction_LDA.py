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
path='Topic_Extraction/PMC29044_plagiated.xml'
tree = ET.parse(path)
topic_list =[]

input_text = get_text.extract_conclusion(tree)
raw_topic = extract_topics_from_text(input_text, num_topics=1)
topic_list.append(extract_keywords(raw_topic))

for ele in topic_list[0]:
    print(ele)


