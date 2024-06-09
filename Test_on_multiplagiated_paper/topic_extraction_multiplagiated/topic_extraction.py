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

from sklearn.decomposition import TruncatedSVD

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




    def preprocess_text(text):
        tokens = word_tokenize(text.lower())  # Tokenization and lowercasing
        tokens = [token for token in tokens if token.isalpha()]  # Keep alphabetic words
        tokens = [lemmatizer.lemmatize(token) for token in tokens if token not in stop_words]  # Lemmatization and remove stopwords
        return ' '.join(tokens)

    tree = ET.parse(file_path)
    stop_words = set(stopwords.words('english'))
    
    lemmatizer = WordNetLemmatizer()
    tfidf_vectorizer = TfidfVectorizer()
    num_topics = 2
    lsa_model = TruncatedSVD(n_components=num_topics)

    abstract =[]
    intro = []
    conclusion = []


    abstract_txt = get_text.extract_conclusion(tree)
    intro_txt = get_text.extract_intro(tree)
    conclusion_txt = get_text.extract_conclusion(tree)
    

# Preprocess the ABSTRACT
    preprocessed_abstract = preprocess_text(abstract_txt)

# Create TF-IDF matrix for the sentence
    tfidf_abstract = tfidf_vectorizer.fit_transform([preprocessed_abstract])

    lsa_abstract= lsa_model.fit_transform(tfidf_abstract)

# Display the top terms associated with the extracted topic
    terms = tfidf_vectorizer.get_feature_names_out()
    top_terms_idx = lsa_model.components_[0].argsort()[-6:]  # Get indices of top 6 terms
    abstract = [terms[idx] for idx in top_terms_idx]
    #print(abstract)

    # Preprocess the INTRO
    preprocessed_intro= preprocess_text(intro_txt)

# Create TF-IDF matrix for the sentence
    tfidf_intro = tfidf_vectorizer.fit_transform([preprocessed_intro])

    lsa_intro= lsa_model.fit_transform(tfidf_intro)

# Display the top terms associated with the extracted topic
    terms = tfidf_vectorizer.get_feature_names_out()
    top_terms_idx = lsa_model.components_[0].argsort()[-6:]  # Get indices of top 6 terms
    intro = [terms[idx] for idx in top_terms_idx]
    #print(intro)

    # Preprocess the CONCLUSION
    preprocessed_conclusion= preprocess_text(conclusion_txt)

# Create TF-IDF matrix for the sentence
    tfidf_conclusion = tfidf_vectorizer.fit_transform([preprocessed_conclusion])

    lsa_conclusion= lsa_model.fit_transform(tfidf_conclusion)

# Display the top terms associated with the extracted topic
    terms = tfidf_vectorizer.get_feature_names_out()
    top_terms_idx = lsa_model.components_[0].argsort()[-6:]  # Get indices of top 6 terms
    conclusion = [terms[idx] for idx in top_terms_idx]
    #print(conclusion)
    
    return abstract,intro,conclusion