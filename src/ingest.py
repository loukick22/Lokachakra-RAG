from langchain_community.document_loaders import Docx2txtLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

print("Step 1: Loading document...")

loader = Docx2txtLoader("data/REPORT.docx")
documents = loader.load()

print("Step 2: Document loaded!")
print(f"Documents loaded: {len(documents)}")

print("Step 3: Splitting document...")

splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=100
)

docs = splitter.split_documents(documents)

print(f"Step 4: Created {len(docs)} chunks")

print("Step 5: Loading embedding model...")

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

print("Step 6: Creating FAISS database...")

db = FAISS.from_documents(docs, embeddings)

print("Step 7: Saving vector database...")

db.save_local("vectorstore")

print("SUCCESS! Vector database created.")