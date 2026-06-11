import streamlit as st
from rag import get_rag_response

# Basic Page Settings
st.set_page_config(page_title="Lokachakra RAG Chatbot", page_icon="🤖", layout="centered")

st.title("🤖 Lokachakra RAG Document Chat")
st.write("Ask any questions regarding the `REPORT.docx` file below.")
st.markdown("---")

# Initialize an empty list to track chat history so it doesn't vanish on refresh
if "messages" not in st.session_state:
    st.session_state.messages = []

# Redraw any previous chat messages from history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input text box at the bottom
if user_query := st.chat_input("Ask a question about the report..."):
    
    # Show user message on screen
    with st.chat_message("user"):
        st.markdown(user_query)
    st.session_state.messages.append({"role": "user", "content": user_query})

    # Show a loading spinner while Gemini thinks
    with st.chat_message("assistant"):
        with st.spinner("Searching document database..."):
            try:
                # Send question to our backend engine
                answer = get_rag_response(user_query)
                st.markdown(answer)
                st.session_state.messages.append({"role": "assistant", "content": answer})
            except Exception as e:
                st.error(f"Error: {str(e)}")
                st.info("Double check that your GOOGLE_API_KEY is spelled correctly inside your `.env` file.")