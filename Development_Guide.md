# **🌟 Development Guide for GIKI RAG Chatbot 🌟**

---

## **📘 Overview**
This guide provides a detailed roadmap for developers to understand, study, and customize the GIKI RAG Chatbot, a Retrieval-Augmented Generation (RAG)-based application designed to assist with GIKI (Ghulam Ishaq Khan Institute)-related queries, such as academic calendars. The project leverages Streamlit for the user interface, a custom RAG pipeline for data retrieval, and Python for backend logic. This guide outlines the project structure, study sequence, and customization steps.

---

## **📂 Project Structure**
### **Root Directory: GIKI_RAG_CHATBOT**
- `venv/`: Virtual environment for dependencies.
- `data/`: Contains data files or documents for the RAG system.
- `interface/`: Houses UI-related files.
  - `__init__.py`: Initializes the package.
  - `chat_interface.py`: Defines chat UI logic.
  - `components.py`: Contains reusable UI components.
  - `streamlit_app.py`: Main Streamlit application script.
- `src/`: Contains core logic files.
  - `__init__.py`: Initializes the package.
  - `chatbot.py`: Core chatbot logic (2 modified lines).
  - `config.py`: Configuration settings.
  - `document_processor.py`: Document processing for RAG (5 modified lines).
  - `privacy_protection.py`: Handles data privacy.
  - `session_manager.py`: Manages conversation sessions.
  - `utils.py`: Utility functions.
- `logs/`: Directory for log files.
- `.env`: Environment variables.
- `.gitignore`: Git ignore file.
- `README.md`: Project overview.
- `requirements.txt`: Dependency list.
- `OUTLINE`: Project outline.
- `TIMELINE`: Development timeline.

---

## **📋 Study Sequence**
### **Step 1: Read README.md**
Start here to understand the project’s purpose, setup instructions, and initial context. Look for setup commands and project goals.

### **Step 2: Review requirements.txt**
Check and install dependencies (e.g., Streamlit, LangChain) using `pip install -r requirements.txt` in the `venv` environment. This ensures your setup aligns with the project.

### **Step 3: Explore config.py**
Examine configuration settings (e.g., API keys, model names). Note parameters that can be adjusted for customization.

### **Step 4: Run streamlit_app.py**
Activate the virtual environment (`source venv/bin/activate` on Unix or `venv\Scripts\activate` on Windows) and run `streamlit run interface/streamlit_app.py`. Interact with the app to see its behavior with sample inputs.

### **Step 5: Analyze chatbot.py**
Study the core logic (2 modified lines) for handling queries, retrieval, and response generation. Search for “RAG,” “retrieval,” and “generation” to trace the flow.

### **Step 6: Investigate document_processor.py**
Explore document loading, splitting, and embedding creation (5 modified lines). Search for “document loading,” “chunking,” and “embedding” to understand data preparation.

### **Step 7: Understand session_manager.py and privacy_protection.py**
Review how conversation history and privacy are managed. Search for “session” and “privacy” to learn context and security features.

### **Step 8: Examine utils.py**
Look for helper functions (e.g., logging, data processing). Search for “utility” or “helper” to identify reusable code.

### **Step 9: Check chat_interface.py and components.py**
Study UI-specific logic and components. Search for “interface” or “component” to see integration with `streamlit_app.py`.

### **Step 10: Review OUTLINE and TIMELINE**
Read these files for project structure and development history to plan your customizations.

---

## **🔧 How to Study the Project**
- **Setup Environment**: Follow `README.md` to set up the virtual environment and install dependencies. Test the app to observe its current functionality.
- **Trace the Flow**: Start with user input in `streamlit_app.py`, move to query processing in `chatbot.py`, and data handling in `document_processor.py`. Use logs (if available) or add debug prints to track execution.
- **Experiment Gradually**: Modify small parts (e.g., adjust chunk size in `document_processor.py` or UI elements in `streamlit_app.py`) and rerun the app to see changes.
- **Use Debugging**: Add logging (e.g., `import logging` and use `logging.debug()`) in key files to monitor the process. Save logs to the `logs` folder.
- **Test with Inputs**: Create an `EXAMPLE_INPUTS.md` file with queries (e.g., “GIKI academic calendar 2022”) and compare outputs to understand behavior.
- **Visualize Architecture**: Sketch a flowchart (e.g., using Draw.io) showing the data flow from `streamlit_app.py` to `document_processor.py` and back. Save as `FLOWCHART.png` or document in `ARCHITECTURE.md`.

---

## **🎨 Customization Steps**
- **Modify Data Handling**: Adjust `document_processor.py` to change chunk sizes or embedding models based on your data needs.
- **Enhance UI**: Customize `streamlit_app.py` or `components.py` to add new features (e.g., buttons, input fields).
- **Tune Retrieval**: Update `chatbot.py` to improve RAG retrieval logic (e.g., add year-specific filtering).
- **Extend Functionality**: Add new utilities in `utils.py` or enhance session management in `session_manager.py`.
- **Test Changes**: Use `EXAMPLE_INPUTS.md` to validate modifications and debug with logs.

---

## **🔍 Additional Resources**
- Search online for: “How to implement RAG with LangChain” for `chatbot.py`.
- Search for: “Streamlit app customization tutorial” for `streamlit_app.py`.
- Search for: “Document embedding techniques” for `document_processor.py`.

---

## **🚀 Getting Started**
- Activate the virtual environment: `source venv/bin/activate` (Unix) or `venv\Scripts\activate` (Windows).
- Install dependencies: `pip install -r requirements.txt`.
- Run the app: `streamlit run interface/streamlit_app.py`.
- Explore and modify code following the study sequence.

---

## **✅ This guide will help you master the project and tailor it to your requirements!**