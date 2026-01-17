
from dotenv import load_dotenv
from langchain_ollama import OllamaEmbeddings, OllamaLLM
from langchain_community.vectorstores import FAISS
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document
import traceback

load_dotenv()

EMBED_MODEL = "nomic-embed-text"
LLM_MODEL = "llama3"
CHUNK_SIZE = 200
TOP_K = 2


with open("abc.txt", "r", encoding="utf-8") as f:
    text = f.read()

text = text.replace("\n", " ")
text = " ".join(text.split())

docs = [Document(page_content=text)]


splitter = RecursiveCharacterTextSplitter(
    chunk_size=CHUNK_SIZE,
    chunk_overlap=40
)

chunks = splitter.split_documents(docs)
print("✅ Total chunks:", len(chunks))


embeddings = OllamaEmbeddings(
    model=EMBED_MODEL,
    base_url="http://172.21.96.1:11435"
)
db = FAISS.from_documents(chunks, embeddings)
print("✅ FAISS index ready")


llm = OllamaLLM(
    model=LLM_MODEL,
    base_url="http://172.21.96.1:11435"
)


def answer_question(query: str):
    try:
        print("\n==============================")
        print("Question:", query)

        docs = db.similarity_search(query, k=TOP_K)

        if not docs:
            return "No relevant context found.", []

        context = "\n".join([d.page_content for d in docs])

        prompt = f"""
RULES (DO NOT BREAK):
- You must answer ONLY using the information in the Context below.
- Do NOT use any outside knowledge.
- If the answer is not explicitly present in the Context, reply EXACTLY:
  NOT_FOUND.

Context:
{context}

Question:
{query}
"""

        answer = llm.invoke(prompt)

        print("✅ Answer:", answer)
        return answer, docs

    except Exception:
        print("\n❌ ERROR")
        traceback.print_exc()
        return "System error.", []


if __name__ == "__main__":
    while True:
        q = input("\nAsk question (or exit): ")
        if q.lower() == "exit":
            break

        ans, src = answer_question(q)
        print("\nAnswer:", ans)
