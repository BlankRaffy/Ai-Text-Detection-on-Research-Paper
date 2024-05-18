import get_text
import xml.etree.ElementTree as ET

plagiated_paper = 'Semantic_Similarity/PMC13901_plagiated.xml'
tree = ET.parse(plagiated_paper)
plagiated_abstract= get_text.extract_abstract(tree)
#print(plagiated_abstract)

original_paper = 'Semantic_Similarity/PMC13901.xml'
tree = ET.parse(original_paper)
original_abstract= get_text.extract_abstract(tree)
#print(original_abstract)


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
print("Similarity Score (BERT):", similarity_score)
