import nltk 
from newspaper import Article
nltk.download('punkt')

# List of URLs to fetch article data from
urls = [
    "https://en.wikipedia.org/wiki/Mathematics",
    "https://en.wikipedia.org/wiki/Artificial_intelligence"
]

for url in urls:
    article = Article(url)
    article.download()
    article.parse()
    article.nlp()
    
    print(f'Title: {article.title}')
    print(f'Author: {article.authors}')
    print(f'Publication date: {article.publish_date}')
    print(f'Summary: {article.summary}\n')
