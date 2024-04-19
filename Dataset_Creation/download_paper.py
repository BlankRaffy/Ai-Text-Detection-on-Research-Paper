import arxiv_downloader
import arxiv
import pandas as pd
download_source=False

n_paper= 10

df= pd.read_csv(r'Dataset_Creation\arxiv-papers.csv') 

#The dowload is based on the id of the document
for i in range(n_paper):
    paper_id = df['arxiv_id'][i]
    search_result = arxiv.Client().results(arxiv.Search(id_list=[paper_id]))

    if article := next(search_result):
        print(f'Starting download of article: "{article.title}" ({paper_id})')
        pdf_path = article.download_pdf(dirpath="Dataset_Collection\original_paper")
        print(f"Download finished! Result saved at:\n{pdf_path}")

        if download_source:
            print(f'Starting download of article source files: "{article.title}" ({paper_id})')
            article.download_source(dirpath=paper_id)
    else:
        print("Article not found.")