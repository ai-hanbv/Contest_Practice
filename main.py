from langchain_ollama import OllamaLLM, OllamaEmbeddings
import faiss
from langchain_community.docstore import InMemoryDocstore # 내부 메모리 사용용
from langchain_community.vectorstores import FAISS
from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
import uuid

model = OllamaLLM(model="llama3.2:latest")
embeddi_model = OllamaEmbeddings(model="bge-m3:latest")
# embedding = embeddi_model.embed_query("test")
# print(len(embedding))
dim = 1024

faiss_index = faiss.IndexFlatL2(dim)

faiss_db = FAISS(
    embedding_function=embeddi_model,
    index=faiss_index,
    docstore=InMemoryDocstore(),
    index_to_docstore_id={}
)

# faiss -> 검색 라이브러리리
# print(faiss_db.index.ntotal)

loader = PyPDFLoader("transformer.pdf")
splitter = CharacterTextSplitter(
    chunk_size=300,
    chunk_overlap=60,
    length_function=len,
)
pdf = loader.load_and_split(splitter)

#ids는 자동으로 지정해준다. 추적 관리가 필요하면 설정하는 게 좋다.
doc_ids = [str(uuid.uuid4()) for _ in range(len(pdf))]

add_pdf = faiss_db.add_documents(documents=pdf,ids=doc_ids)
# 저장된 문서 확인
print(len(add_pdf))
print(faiss_db.index.ntotal)