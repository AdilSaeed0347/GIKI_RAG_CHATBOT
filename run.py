"""
Main entry point for GIKI RAG Chatbot
Run this file to start the application
"""
import sys
import os
import logging
from groq import Groq

# Add src directory to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from interface.chat_interface import ChatInterface
from src.utils import setup_logging
from src.config import Config

def main():
    """Main function to run the chatbot"""
    # Setup logging
    logger = setup_logging()
    
    logger.info("Starting GIKI RAG Chatbot...")
    
    try:
        # Ensure directories exist
        Config.setup_directories()
        
        # Validate Groq API key
        logger.info("Validating Groq API key...")
        try:
            test_client = Groq(api_key=Config.GROQ_API_KEY)
            test_response = test_client.chat.completions.create(
                model=Config.GROQ_MODEL,
                messages=[{"role": "user", "content": "Test API key"}],
                max_tokens=10
            )
            logger.info("Groq API key validated successfully")
        except Exception as e:
            logger.error("Failed to validate Groq API key: %s", str(e))
            raise ValueError(f"Invalid Groq API key: {str(e)}. Please verify GROQ_API_KEY in .env.")
        
        # Create and launch interface
        chat_interface = ChatInterface()
        interface = chat_interface.create_interface()
        
        # Launch configuration
        launch_config = {
            "server_name": "0.0.0.0",  # Allow external access
            "server_port": 7860,       # Default Gradio port
            "share": False,            # Set to True for public sharing
            "debug": Config.DEBUG,     # Debug mode from config
            "show_error": True,        # Show detailed errors
            "quiet": False,            # Show startup messages
        }
        
        # Print startup information
        print("🚀 GIKI RAG Chatbot Starting...")
        print(f"🔧 Debug Mode: {Config.DEBUG}")
        print(f"🌐 Server: http://localhost:{launch_config['server_port']}")
        print(f"📂 Upload Directory: {Config.UPLOAD_DIR}")
        print(f"💾 Cache Directory: {Config.CACHE_DIR}")
        print(f"📝 Log Directory: {Config.LOG_DIR}")
        print("✅ Groq API Key: Configured and validated")
        
        print("\n🎯 Features Available:")
        print("   💬 ChatGPT-like Interface")
        print("   🔒 Smart Privacy Protection") 
        print("   📚 Document Analysis")
        print("   📋 Official Document Links")
        print("   💾 Session Management")
        print("   📊 Conversation Export")
        
        print("\n📋 How to Use:")
        print("   1. Add your Groq API key (if not in .env)")
        print("   2. Upload PDF, DOCX, or TXT documents")
        print("   3. Wait for processing to complete")
        print("   4. Start chatting about your documents!")
        
        print(f"\n🌟 Access your chatbot at: http://localhost:{launch_config['server_port']}")
        print("=" * 60)
        
        # Launch the interface
        interface.launch(**launch_config)
        
    except KeyboardInterrupt:
        print("\n👋 Shutting down GIKI RAG Chatbot...")
        logger.info("Application stopped by user")
    except Exception as e:
        print(f"\n❌ Error starting application: {str(e)}")
        logger.error(f"Application startup error: {str(e)}")
        return 1
    
    return 0

if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code)




# for Html css and javascript code 








# """
# Main entry point for GIKI RAG Chatbot
# Run this file to start the Flask-based application
# """
# import sys
# import os
# import logging
# from flask import Flask, render_template, request, jsonify
# from grog import Groq

# # Add src directory to Python path
# sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# from interface.chat_interface import ChatInterface
# from src.utils import setup_logging
# from src.config import Config

# app = Flask(__name__, static_folder='static', template_folder='templates')
# logger = setup_logging()

# def validate_api_key():
#     """Validate Groq API key"""
#     logger.info("Validating Groq API key...")
#     try:
#         test_client = Groq(api_key=Config.GROQ_API_KEY)
#         test_response = test_client.chat.completions.create(
#             model=Config.GROQ_MODEL,
#             messages=[{"role": "user", "content": "Test API key"}],
#             max_tokens=10
#         )
#         logger.info("Groq API key validated successfully")
#         return True
#     except Exception as e:
#         logger.error("Failed to validate Groq API key: %s", str(e))
#         return False

# # Initialize ChatInterface
# chat_interface = ChatInterface()

# @app.route('/')
# def index():
#     """Serve the main HTML page"""
#     return render_template('index.html')

# @app.route('/api/setup_api_key', methods=['POST'])
# def setup_api_key():
#     """API endpoint to configure API key"""
#     try:
#         api_key = request.json.get('api_key')
#         result, is_setup_complete = chat_interface.setup_api_key(api_key)
#         return jsonify({'status': result, 'is_setup_complete': is_setup_complete})
#     except Exception as e:
#         logger.error(f"Error in setup_api_key: {str(e)}")
#         return jsonify({'status': f"Error: {str(e)}"}), 500

# @app.route('/api/upload_documents', methods=['POST'])
# def upload_documents():
#     """API endpoint to upload documents"""
#     try:
#         files = request.files.getlist('files')
#         result = chat_interface.upload_documents(files)
#         return jsonify({'status': result})
#     except Exception as e:
#         logger.error(f"Error in upload_documents: {str(e)}")
#         return jsonify({'status': f"Error: {str(e)}"}), 500

# @app.route('/api/chat', methods=['POST'])
# def chat_response():
#     """API endpoint to handle chat messages"""
#     try:
#         message = request.json.get('message')
#         history = request.json.get('history', [])
#         prompt, updated_history = chat_interface.chat_response(message, history)
#         return jsonify({'prompt': prompt, 'history': updated_history})
#     except Exception as e:
#         logger.error(f"Error in chat_response: {str(e)}")
#         return jsonify({'prompt': '', 'history': history, 'status': f"Error: {str(e)}"}), 500

# @app.route('/api/clear_chat', methods=['POST'])
# def clear_chat():
#     """API endpoint to clear chat history"""
#     try:
#         result = chat_interface.clear_chat_history()
#         return jsonify({'history': result})
#     except Exception as e:
#         logger.error(f"Error in clear_chat: {str(e)}")
#         return jsonify({'history': [], 'status': f"Error: {str(e)}"}), 500

# def main():
#     """Main function to run the chatbot"""
#     logger.info("Starting GIKI RAG Chatbot...")
    
#     try:
#         # Ensure directories exist
#         Config.setup_directories()
        
#         # Validate Groq API key
#         if not validate_api_key():
#             raise ValueError("Invalid Groq API key. Please verify GROQ_API_KEY in .env.")
        
#         # Print startup information
#         port = 7860  # Default Flask port (same as Gradio for consistency)
#         print("🚀 GIKI RAG Chatbot Starting...")
#         print(f"🔧 Debug Mode: {Config.DEBUG}")
#         print(f"🌐 Server: http://localhost:{port}")
#         print(f"📂 Upload Directory: {Config.UPLOAD_DIR}")
#         print(f"💾 Cache Directory: {Config.CACHE_DIR}")
#         print(f"📝 Log Directory: {Config.LOG_DIR}")
#         print("✅ Groq API Key: Configured and validated")
        
#         print("\n🎯 Features Available:")
#         print("   💬 ChatGPT-like Interface")
#         print("   🔒 Smart Privacy Protection") 
#         print("   📚 Document Analysis")
#         print("   📋 Official Document Links")
#         print("   💾 Session Management")
#         print("   📊 Conversation Export")
        
#         print("\n📋 How to Use:")
#         print("   1. Add your Groq API key (if not in .env)")
#         print("   2. Upload PDF, DOCX, or TXT documents")
#         print("   3. Wait for processing to complete")
#         print("   4. Start chatting about your documents!")
        
#         print(f"\n🌟 Access your chatbot at: http://localhost:{port}")
#         print("=" * 60)
        
#         # Run Flask app
#         app.run(host="0.0.0.0", port=port, debug=Config.DEBUG)
        
#     except KeyboardInterrupt:
#         print("\n👋 Shutting down GIKI RAG Chatbot...")
#         logger.info("Application stopped by user")
#     except Exception as e:
#         print(f"\n❌ Error starting application: {str(e)}")
#         logger.error(f"Application startup error: {str(e)}")
#         return 1
    
#     return 0

# if __name__ == "__main__":
#     exit_code = main()
#     sys.exit(exit_code)