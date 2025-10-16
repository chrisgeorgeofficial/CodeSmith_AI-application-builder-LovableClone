from langchain_groq import ChatGroq

llm = ChatGroq(model="openai/gpt-oss-120b")

resp = llm.invoke("Who invented kriya yoga. answer in one sentence.")

print(resp.content)