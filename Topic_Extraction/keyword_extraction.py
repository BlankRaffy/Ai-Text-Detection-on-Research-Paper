import get_text
import xml.etree.ElementTree as ET


# Example texts
import yake
kw_extractor = yake.KeywordExtractor()
language = "en"
max_ngram_size = 3
deduplication_threshold = 0.9
numOfKeywords = 6
custom_kw_extractor = yake.KeywordExtractor(lan=language, n=max_ngram_size, dedupLim=deduplication_threshold, top=numOfKeywords, features=None)

path=r'C:\Users\Blank\Desktop\Ai-Text-Detection-on-Research-Paper\Topic_Extraction\PMC29044_plagiated.xml'
tree = ET.parse(path)
text = get_text.extract_intro(tree)

keywords = custom_kw_extractor.extract_keywords(text)

print("\n\n")
for kw in keywords:
    print(kw[0])