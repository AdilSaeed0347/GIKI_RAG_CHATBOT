#  GIKI RAG Chatbot

A sophisticated Retrieval-Augmented Generation (RAG) chatbot specifically designed for GIKI (Ghulam Ishaq Khan Institute) which can help GIKI student about their queries, have smart privacy protection, and academic intelligence.

##  Features

###  Core Capabilities
- **ChatGPT-like Interface**: Modern, intuitive chat experience
- **Smart Document Analysis**: PDF, DOCX, TXT file processing
- **Academic Intelligence**: Focused on educational content
- **Privacy Protection**: Smart filtering without over-blocking academic queries
- **Session Management**: Persistent conversations and document cache
- **Official Document Links**: Direct access to GIKI policies and resources

###  AI Features
- **Context-Aware Responses**: Maintains conversation history
- **Intent Detection**: Understands document requests vs specific questions
- **Smart Chunking**: Optimized text processing for better retrieval
- **Multi-format Support**: Handle various document types seamlessly

###  Security & Privacy
- **Academic-Safe Filtering**: Blocks sensitive data but allows academic queries
- **Secure API Key Management**: Environment-based configuration
- **Content Validation**: Prevents dangerous or harmful content
- **Session Isolation**: Each session is independent and secure

##  Quick Start

### Prerequisites
- Python 3.8 or higher
  

### Installation

1. **Clone or create the project structure**:
   ```bash
   mkdir GIKI_RAG_Chatbot
   cd GIKI_RAG_Chatbot
   ```

2. **Create virtual environment**:
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Setup environment variables**:
   ```bash
   # Copy the .env file and add your API key
   cp .env.example .env
   
   # Edit .env and add your Groq API key:
   GROQ_API_KEY=your_actual_api_key_here
   ```

5. **Run the application**:
   ```bash
   python run.py
   ```

6. **Access the chatbot**:
   Open your browser and go to: `http://localhost:7860`

##  Project Structure

```
GIKI_RAG_Chatbot/
│
├── .env                          # Environment variables (API keys)
├── .gitignore                    # Git ignore file
├── requirements.txt              # Python dependencies
├── README.md                     # Project documentation
├── run.py                        # Main entry point
│
├── src/                          # Source code directory
│   ├── __init__.py
│   ├── config.py                 # Configuration settings
│   ├── chatbot.py               # Main RAG chatbot class
│   ├── privacy_protection.py    # Privacy and security features
│   ├── document_processor.py    # Document handling and processing
│   ├── session_manager.py       # Session and context management
│   └── utils.py                 # Utility functions
│
├── interface/                    # UI components
│   ├── __init__.py
│   ├── chat_interface.py        # ChatGPT-like Gradio interface
│   └── components.py            # Reusable UI components
│
├── data/                         # Data directory
│   ├── uploads/                 # Uploaded documents
│   └── cache/                   # Temporary files and cache
│
└── logs/                        # Application logs
    └── chatbot.log
```

##  How to Use

### 1. **Setup Phase**
   - Enter your llama API key in the sidebar
   - Upload your documents (PDF, DOCX, TXT)
   - Wait for processing to complete

### 2. **Chat Phase**
   - Type questions in the chat input
   - Use quick action buttons for common queries
   - View sources and references for each response

### 3. **Management**
   - Clear chat history when needed
   - Export conversations for records
   - Monitor session statistics

##  Example Queries

### Document Requests (Get Official Links)
- "I need GIKI admission policy"
- "Show me fee structure"
- "Give me academic calendar"

### Specific Academic Questions
- "What are the admission requirements for engineering?"
- "Tell me about hostel facilities"
- "What programs does GIKI offer?"

### Academic Records (Safe Processing)
- "What are Adil Saeed's matriculation marks?"
- "Show me academic qualifications"
- "Tell me about graduation requirements"

## ⚙️ Configuration

### Environment Variables (.env)
```bash
# Required
GROQ_API_KEY=your_groq_api_key_here
GROQ_MODEL=llama-3.3-70b-versatile

EMBEDDING_MODEL=sentence-transformers/all-MiniLM-L6-v2  # model to convert text to vectors
CHUNK_SIZE=800  # size of each text chunk in tokens
CHUNK_OVERLAP=150  # overlap tokens between consecutive chunks
TOP_K_CHUNKS=6  # number of top relevant chunks to retrieve
MAX_TOKENS=600  # max tokens to generate in a response
TEMPERATURE=0.3  # controls creativity; low=factual, high=creative
DEBUG=True  # show detailed logs for troubleshooting

```

### Supported File Types
- **PDF**: Academic documents, policies, handbooks
- **DOCX**: Forms, announcements, reports
- **TXT**: Plain text files, notices
- **MD**: Markdown documents

##  Development

### Adding New Features
1. **Document Registry**: Add official GIKI documents in `src/chatbot.py`
2. **Quick Answers**: Extend pre-computed responses
3. **Privacy Rules**: Modify patterns in `src/privacy_protection.py`
4. **UI Components**: Create reusable components in `interface/components.py`

### Customization
- **Styling**: Modify CSS in `interface/chat_interface.py`
- **Prompts**: Update templates in `src/config.py`
- **Models**: Change Groq model in environment variables
- **Chunk Sizes**: Adjust for different document types

##  Security Features

### Smart Privacy Protection
-  **Academic Queries Allowed**: Matriculation, grades, admission info
-  **Personal Data Blocked**: CNIC, phone numbers, email addresses
-  **Context Aware**: Distinguishes between academic and personal requests

### Content Validation
- Blocks dangerous keywords and harmful content
- Validates file types and sizes
- Sanitizes user inputs and file names

##  Performance

### Optimizations
- **FAISS Vector Store**: Fast similarity search
- **Smart Chunking**: Balanced context and performance
- **Session Caching**: Reduced reprocessing
- **Async Processing**: Non-blocking operations

### Resource Usage
- **Memory**: ~2-4GB depending on document size
- **Storage**: Temporary files auto-cleaned
- **CPU**: Moderate usage during processing

##  Troubleshooting

### Common Issues

**1. API Key Error**
```
 ERROR: Please provide a valid Groq API key!
```
- Solution: Add your Groq API key to the `.env` file

**2. Document Processing Error**
```
 No documents could be processed successfully!
```
- Solution: Check file formats (PDF, DOCX, TXT only)
- Ensure files are not corrupted or password-protected

**3. Import Errors**
```
ModuleNotFoundError: No module named 'src'
```
- Solution: Run from the project root directory: `python run.py`

**4. Memory Issues**
- Solution: Reduce `CHUNK_SIZE` in `.env` or process fewer documents

### Debug Mode
Enable debug mode in `.env`:
```bash
DEBUG=True
```

Check logs in `logs/chatbot.log` for detailed information.

##  Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

##  License

This project is licensed under the MIT License - see the LICENSE file for details.

##  Acknowledgments

- **Groq**: Fast AI inference
- **LangChain**: RAG framework
- **Gradio**: Web interface
- **FAISS**: Vector similarity search
- **Sentence Transformers**: Text embeddings

##  Support

For support and questions:
-  Email: adilahmad0347@gmail.com
-  Issues: Create a GitHub issue
-  Docs: Check this README and code comments

---


**Made with ❤️ for GIKI Community by Adil saeed**
