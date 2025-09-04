from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from langchain_qdrant import QdrantVectorStore
from openai import OpenAI
import os
load_dotenv()


openai_client = OpenAI(
    api_key=os.getenv("GOOGLE_API"),
    base_url="https://generativelanguage.googleapis.com/v1beta/"
)

# vector Embeddings

ebedding_model = OpenAIEmbeddings(
    model="text-embedding-3-large"
)


vector_db = QdrantVectorStore.from_existing_collection(
    url="http://localhost:6333",
    collection_name="learning_rag",
    embedding_model=ebedding_model
)


# Take the user input

user_query = input("Ask Something")


# Relevant Chunks from the vector db
search_results = vector_db.similarity_search(query=user_query)

content = "\n\n\n".join([f"Page Content : {result.page_content}\nPage Number : {result.metadata['page_label']}\nFile Location:{result.metadata["source"]}" for result in search_results])

SYSTEM_PROMPT = f"""
You are a hellfull ai assistant who answeres users query based on the available context retrived from a pdf file along with page_contents and page number

you should only ans hte user based on the following context and navigate the user to open the right page number to know more.

Context:
{content}

"""

response = openai_client.chat.completions.create(
    model="gpt-5",
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": user_query}
    ]
)


print(f"🤖: {response.choices[0].message.content}")