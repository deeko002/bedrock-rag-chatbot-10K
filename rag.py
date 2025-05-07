import os
import streamlit as st
import boto3
from dotenv import load_dotenv

# Load env
load_dotenv()

# Get environment variables
aws_access_key = os.getenv("AWS_ACCESS_KEY_ID")
aws_secret_key = os.getenv("AWS_SECRET_ACCESS_KEY")
aws_session_token = os.getenv("AWS_SESSION_TOKEN")
region = os.getenv("AWS_REGION", "us-east-1")
model_arn = os.getenv("MODEL_ARN")  # must be full foundation-model ARN
knowledge_base_id = os.getenv("KNOWLEDGE_BASE_ID")

# Initialize Bedrock Agent Runtime client
client = boto3.client(
    service_name="bedrock-agent-runtime",
    region_name=region,
    aws_access_key_id=aws_access_key,
    aws_secret_access_key=aws_secret_key,
    aws_session_token=aws_session_token
)

# Streamlit UI
st.set_page_config(page_title="RAG Chatbot", layout="centered")
st.title('RAG Chatbot Demo')
st.subheader("A RAG-based chatbot that can answer questions about company 10-K filing documents")

st.markdown("""
In the knowledge base, we have Amazon's 2024 10-K filing document. Sample questions include:
- What are Amazon's primary business segments?
- What was Amazon's total net sales for the reporting period?
- How does Amazon describe its use of AI in its operations?
- What areas did Amazon identify as strategic investment priorities?
- What are the main risk factors identified in this 10-k filing?
- What is Amazon's strategy for growth?
""")

# Welcome message
with st.chat_message("assistant"):
    st.markdown("Hi there! What questions do you have?")

def get_response(prompt: str) -> str:
    """Call retrieve_and_generate with Claude 3.5 Haiku"""
    try:
        response = client.retrieve_and_generate(
            input={"text": prompt},
            retrieveAndGenerateConfiguration={
                "type": "KNOWLEDGE_BASE",
                "knowledgeBaseConfiguration": {
                    "knowledgeBaseId": knowledge_base_id,
                    "modelArn": model_arn
                }
            }
        )
        return response["output"]["text"]
    except Exception as e:
        return f"Error processing your request: {str(e)}"

prompt = st.chat_input("Ask anything about this document")

if prompt:
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        response = get_response(prompt)
        st.markdown(response)
