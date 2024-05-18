import get_text
import xml.etree.ElementTree as ET

#LOAD AND GET TEXT FROM PLAGIATED
plagiated_paper = 'Semantic_Similarity/paper_to_test/PMC13901_plagiated.xml'
plagiated_tree = ET.parse(plagiated_paper)
plagiated_abstract= get_text.extract_abstract(plagiated_tree)
plagiated_intro = get_text.extract_intro(plagiated_tree)
plagiated_conclusion = get_text.extract_conclusion(plagiated_tree)

#print("ABSTRACT:" +plagiated_abstract)
#print("INTRO:" + plagiated_intro)
#print("CONCLUSION:" + plagiated_conclusion)


#LOAD AND GET TEXT FROM PLAGIATED
original_paper = 'Semantic_Similarity/paper_to_test/PMC35277.xml' #PMC13901 PMC29028 PMC32247 PMC34549 #PMC35277
original_tree = ET.parse(original_paper)
original_abstract= get_text.extract_abstract(original_tree)
original_intro = get_text.extract_intro(original_tree)
original_conclusion = get_text.extract_conclusion(original_tree)

#print("ABSTRACT:" + original_abstract)
#print("INTRO:" + original_intro)
#print("CONCLUSION:" + original_conclusion)


from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Carica il modello SentenceTransformer pre-addestrato (es. distiluse-base-multilingual-cased)
model = SentenceTransformer('distiluse-base-multilingual-cased')

def text_similarity_bert(text1, text2):
    embeddings = model.encode([text1, text2])
    similarity = cosine_similarity([embeddings[0]], [embeddings[1]])[0][0]
    return similarity

# Esempio di utilizzo

similarity_score = text_similarity_bert(plagiated_abstract, original_abstract)
print("Similarity Score (BERT) for abstract:", similarity_score)

similarity_score = text_similarity_bert(plagiated_intro, original_intro)
print("Similarity Score (BERT) for introduction:", similarity_score)

similarity_score = text_similarity_bert(plagiated_conclusion, original_conclusion)
print("Similarity Score (BERT) for conclusion:", similarity_score)
