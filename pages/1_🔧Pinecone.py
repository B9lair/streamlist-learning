# 会话
import streamlit as st

if "PINECONE_API_KEY" not in st.session_state:
    st.session_state["PINECONE_API_KEY"] = ''

# 环境设置
if "PINECONE_ENVIRONMENT" not in st.session_state:
    st.session_state["PINECONE_ENVIRONMENT"] = ''

# 初始化
st.set_page_config(page_title="Pinecone Settings", layout="wide")

st.title("Pinecone Settings")

pinecone_api_key = st.text_input("API Key", value=st.session_state["PINECONE_API_KEY"], max_chars=None, key=None, type='default')
environment = st.text_input("Environment", value=st.session_state["PINECONE_ENVIRONMENT"], max_chars=None, key=None, type='default')

saved = st.button("Save")

if saved:
    st.session_state["PINECONE_API_KEY"] = pinecone_api_key
    st.session_state["PINECONE_ENVIRONMENT"] = environment


with st.container():
    st.header("Pinecone Settings")
    st.markdown(
        """
        | Key | Value |
        | --- | ----- |
        | PINECONE_API_KEY | {} |
        | PINECONE_ENVIRONMENT | {} |
        """.format(st.session_state["PINECONE_API_KEY"], st.session_state["PINECONE_ENVIRONMENT"]))