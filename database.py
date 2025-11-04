import os
os.environ["USER_AGENT"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"

from langchain_community.document_loaders import WebBaseLoader # pyright: ignore[reportMissingImports]

loader = WebBaseLoader("https://gdpr.eu/")
docs = loader.load()
print(docs[0].page_content)

