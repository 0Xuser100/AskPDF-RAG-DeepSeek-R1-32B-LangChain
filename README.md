# 📘 AskPDF-RAG-DeepSeek-R1-32B-LangChain - Your Intelligent Document Assistant

## 📌 Project Description
AskPDF-RAG-DeepSeek-R1-32B-LangChain is an advanced research assistant that helps users analyze and extract insights from PDF documents. By leveraging powerful AI models, it provides concise and factual answers to user queries based on document content. The project is built using Streamlit for an interactive UI and LangChain for document processing and retrieval.

---

## 🔧 Tools & Technologies Used
- **Streamlit**: For building an interactive web interface.
- **LangChain**: For handling document loading, text splitting, and retrieval.
- **Ollama**: For running AI models locally.
- **DeepSeek-R1:32B**: A powerful LLM used for answering queries.
- **PDFPlumber**: For extracting text from PDF files.
- **In-Memory Vector Database**: For document storage and similarity search.

---

## 🚀 How to Run the Project

### Step 1: Clone the Repository
```bash
git clone https://github.com/0Xuser100/AskPDF-RAG-DeepSeek-R1-32B-LangChain.git
cd AskPDF-RAG-DeepSeek-R1-32B-LangChain
```

### Step 2: Install Dependencies
Make sure you have Python installed, then run:
```bash
pip install -r requirements.txt
```

### Step 3: Install and Run Ollama
You need to download and set up **Ollama** to run the AI model locally.
1. Download Ollama from: [https://ollama.com/](https://ollama.com/)
2. Install it following the instructions on the website.
3. Run the following commands:
```bash
ollama run deepseek-r1:32b
ollama pull deepseek-r1:32b
```

### Step 4: Start the Application
Run the following command:
```bash
streamlit run app.py
```
Your application will be available at `http://localhost:8501/` in your browser.

---

## 🔥 How Can We Improve This Project?
### Future Enhancements
- Implement a **database-backed** vector store instead of an in-memory store for scalability.
- Enhance **UI/UX** with more advanced chat formatting and interactive elements.
- Add **multi-document support** to allow querying across multiple PDFs.
- Integrate **more AI models** to enhance response accuracy and diversity.

### Why This Project is Important
- It provides a **fast and intelligent** way to extract insights from research papers, legal documents, and reports.
- Helps students, researchers, and professionals **save time** by automating document analysis.
- Showcases the power of **LLMs and LangChain** in real-world applications.

---

## 📬 Contact Information
📌 **LinkedIn**: [My LinkedIn Profile](https://www.linkedin.com/in/mahmoud-abdulhamid-052244230/)  
📌 **Kaggle**: [My Kaggle Profile](https://www.kaggle.com/triblex)  
📌 **Email**:  mahmoudabdulhamid22@gmail.com  
📌 **Phone**: +201550391185

---

Thank you for using **AskPDF-RAG-DeepSeek-R1-32B-LangChain**! 🚀

