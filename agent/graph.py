from dotenv import load_dotenv

load_dotenv()

from langchain_groq import ChatGroq

llm = ChatGroq(model="openai/gpt-oss-120b")

from pydantic import BaseModel

user_prompt = "create a simple calculator web application"

prompt = f"""
You are the PLANNER agent. Convert the user prompt into a COMPLETE engineering project plan 

User request: {user_prompt}
"""









class Schema(BaseModel):
    price: float
    eps: float

resp = llm.with_structured_output(Schema).invoke("Extracct Price and EPS from this report:"
                                           "NVIDIA reported quaterly EPS of 2.3 and"
                                           "their current price is $100.")

print(resp)