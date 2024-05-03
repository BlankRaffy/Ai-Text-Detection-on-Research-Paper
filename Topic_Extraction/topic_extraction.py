import get_text
import xml.etree.ElementTree as ET
import yake

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