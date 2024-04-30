from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import NMF
import xml.etree.ElementTree as ET
import get_text

path=r'C:\Users\Blank\Desktop\Ai-Text-Detection-on-Research-Paper\Topic_Extraction\PMC29044_plagiated.xml'
tree = ET.parse(path)

sentence = get_text.extract_conclusion(tree)

vectorizer = TfidfVectorizer(max_features=1000, stop_words='english')
X = vectorizer.fit_transform([sentence])

num_topics = 1
nmf_model = NMF(n_components=num_topics, random_state=1)
nmf_model.fit(X)

feature_names = vectorizer.get_feature_names_out()

topic = nmf_model.components_[0]
top_words_indices = topic.argsort()[:-10 - 1:-1]  # Get indices of top 10 words
top_words = [feature_names[i] for i in top_words_indices]

print("Top words for the topic:")
print(", ".join(top_words))

