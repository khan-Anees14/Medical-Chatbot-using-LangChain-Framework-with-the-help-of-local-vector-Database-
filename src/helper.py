
# 01 PDF Loader
from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader

def load_pdfs(folder_path):
    loader = DirectoryLoader(
        folder_path,
        glob="*.pdf",
        loader_cls=PyPDFLoader
    )
    documents = loader.load()
    print(f"Loaded {len(documents)} documents.")
    return documents


# 02 Text Splitter
from langchain_text_splitters import RecursiveCharacterTextSplitter

def split_text(documents):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=300,
        chunk_overlap=50
    )
    text_chunks = splitter.split_documents(documents)
    # print(f"Created {len(text_chunks)} text chunks.")
    return text_chunks


# 03 HuggingFace Embeddings (FREE)
from langchain_huggingface import HuggingFaceEmbeddings

def download_hugging_face_embeddings():
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )
    return embeddings


# 04 FAISS Vector Store (CREATE)
from langchain_community.vectorstores import FAISS

def create_faiss_index(text_chunks, embeddings, save_path="faiss_index"):
    db = FAISS.from_documents(text_chunks, embeddings)
    db.save_local(save_path)
    print("FAISS vector store created and saved locally.")
    return db


# 05 FAISS Vector Store (LOAD)
def load_faiss_index(embeddings, load_path="faiss_index"):
    db = FAISS.load_local(
        load_path,
        embeddings,
        allow_dangerous_deserialization=True
    )
    print("FAISS vector store loaded from disk.")
    return db
