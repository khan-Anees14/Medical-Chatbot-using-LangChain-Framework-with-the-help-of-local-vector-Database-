from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

# 1️⃣ Load PDFs
loader = DirectoryLoader(
    path = "data",                 # your PDF folder
    glob = "*.pdf",
    loader_cls = PyPDFLoader
)

documents = loader.load()
print(f"Loaded {len(documents)} documents")

# 2️⃣ Split text
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=300,
    chunk_overlap=20
)

text_chunks = text_splitter.split_documents(documents)
print(f"Created {len(text_chunks)} text chunks")

# 3️⃣ Load embeddings (FREE)
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# 4️⃣ Create FAISS index
db = FAISS.from_documents(text_chunks, embeddings)

# 5️⃣ Save FAISS locally
db.save_local("faiss_index")

print("✅ FAISS index saved successfully!")

from src.helper import (
    load_pdfs,
    split_text,
    download_hugging_face_embeddings,
    create_faiss_index
)

docs = load_pdfs("data")
chunks = split_text(docs)
embeddings = download_hugging_face_embeddings()
create_faiss_index(chunks, embeddings)
