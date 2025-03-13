import streamlit as st
from langchain_community.document_loaders import PDFPlumberLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_ollama import OllamaEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM

# Streamlit UI styling using Markdown and CSS
st.markdown("""
    <style>
    .stApp {
        background-color: #0E1117;
        color: #FFFFFF;
    }
    
    /* Styling for the chat input field */
    .stChatInput input {
        background-color: #1E1E1E !important;
        color: #FFFFFF !important;
        border: 1px solid #3A3A3A !important;
    }
    
    /* Styling for user messages in chat */
    .stChatMessage[data-testid="stChatMessage"]:nth-child(odd) {
        background-color: #1E1E1E !important;
        border: 1px solid #3A3A3A !important;
        color: #E0E0E0 !important;
        border-radius: 10px;
        padding: 15px;
        margin: 10px 0;
    }
    
    /* Styling for assistant messages in chat */
    .stChatMessage[data-testid="stChatMessage"]:nth-child(even) {
        background-color: #2A2A2A !important;
        border: 1px solid #404040 !important;
        color: #F0F0F0 !important;
        border-radius: 10px;
        padding: 15px;
        margin: 10px 0;
    }
    
    /* Styling for chat avatars */
    .stChatMessage .avatar {
        background-color: #00FFAA !important;
        color: #000000 !important;
    }
    
    /* Fix text color inside messages */
    .stChatMessage p, .stChatMessage div {
        color: #FFFFFF !important;
    }
    
    /* Styling for file uploader */
    .stFileUploader {
        background-color: #1E1E1E;
        border: 1px solid #3A3A3A;
        border-radius: 5px;
        padding: 15px;
    }
    
    /* Styling for headers */
    h1, h2, h3 {
        color: #00FFAA !important;
    }
    </style>
    """, unsafe_allow_html=True)

# Define prompt template for AI response
PROMPT_TEMPLATE = """
You are an expert research assistant. Use the provided context to answer the query. 
If unsure, state that you don't know. Be concise and factual (max 3 sentences).

Query: {user_query} 
Context: {document_context} 
Answer:
"""

# Constants for file storage and AI components
PDF_STORAGE_PATH = 'document_store/pdfs/'
EMBEDDING_MODEL = OllamaEmbeddings(model="deepseek-r1:32b")  # Embedding model for vector search
DOCUMENT_VECTOR_DB = InMemoryVectorStore(EMBEDDING_MODEL)  # In-memory vector store for document retrieval
LANGUAGE_MODEL = OllamaLLM(model="deepseek-r1:32b")  # Language model for answering queries

# Function to save uploaded PDF file
def save_uploaded_file(uploaded_file):
    file_path = PDF_STORAGE_PATH + uploaded_file.name
    with open(file_path, "wb") as file:
        file.write(uploaded_file.getbuffer())  # Save the file to disk
    return file_path

# Function to load PDF documents using PDFPlumberLoader
def load_pdf_documents(file_path):
    document_loader = PDFPlumberLoader(file_path)
    return document_loader.load()

# Function to split documents into smaller chunks for processing
def chunk_documents(raw_documents):
    text_processor = RecursiveCharacterTextSplitter(
        chunk_size=1000,  # Maximum chunk size
        chunk_overlap=200,  # Overlapping characters between chunks
        add_start_index=True
    )
    return text_processor.split_documents(raw_documents)

# Function to add document chunks to the in-memory vector store
def index_documents(document_chunks):
    DOCUMENT_VECTOR_DB.add_documents(document_chunks)

# Function to find related documents based on user query
def find_related_documents(query):
    return DOCUMENT_VECTOR_DB.similarity_search(query)

# Function to generate AI response using retrieved documents
def generate_answer(user_query, context_documents):
    context_text = "\n\n".join([doc.page_content for doc in context_documents])
    conversation_prompt = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
    response_chain = conversation_prompt | LANGUAGE_MODEL  # Combine prompt and model
    return response_chain.invoke({"user_query": user_query, "document_context": context_text})

# UI Configuration
st.title("📘 DocuMind AI")  # App title
st.markdown("### Your Intelligent Document Assistant")  # Subtitle
st.markdown("---")  # Horizontal separator

# File Upload Section
uploaded_pdf = st.file_uploader(
    "Upload Research Document (PDF)",
    type="pdf",
    help="Select a PDF document for analysis",
    accept_multiple_files=False
)

# Process the uploaded document if a file is uploaded
if uploaded_pdf:
    saved_path = save_uploaded_file(uploaded_pdf)  # Save file
    raw_docs = load_pdf_documents(saved_path)  # Load document contents
    processed_chunks = chunk_documents(raw_docs)  # Split into chunks
    index_documents(processed_chunks)  # Index chunks for search
    
    st.success("✅ Document processed successfully! Ask your questions below.")  # Confirmation message
    
    user_input = st.chat_input("Enter your question about the document...")  # User input field
    
    if user_input:
        with st.chat_message("user"):
            st.write(user_input)  # Display user question
        
        with st.spinner("Analyzing document..."):
            relevant_docs = find_related_documents(user_input)  # Retrieve relevant document chunks
            ai_response = generate_answer(user_input, relevant_docs)  # Generate AI response
            
        with st.chat_message("assistant", avatar="🤖"):
            st.write(ai_response)  # Display AI response
