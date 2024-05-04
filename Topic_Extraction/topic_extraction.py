import get_text
import xml.etree.ElementTree as ET
import yake

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import NMF

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
