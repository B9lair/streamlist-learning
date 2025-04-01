import streamlit as st
from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage


# 初始化ChatOpenAI对象
chat = None

# 开发测试，不对输入进行明文显示
if "OPENAI_API_KEY" not in st.session_state:
    st.session_state["OPENAI_API_KEY"] = ''
else:
    chat = ChatOpenAI(openai_api_key=st.session_state["OPENAI_API_KEY"], base_url="https://api.chatanywhere.tech")

if "PINECONE_API_KEY" not in st.session_state:
    st.session_state["PINECONE_API_KEY"] = ''

if "PINECONE_ENVIRONMENT" not in st.session_state:
    st.session_state["PINECONE_ENVIRONMENT"] = ''

# 全局标题
st.set_page_config(page_title="Welcome to ASL", layout="wide")

# 页面标题
st.title("👍Welcome to wxy")

# 当chat实例不为空,完成实例
if chat:
    with st.container():
        st.header("Chat with GPT")
        prompt = st.text_input("Prompt", value="", max_chars=None, key=None, type='default')
        # 提交按钮
        asked = st.button("Ask")
        if asked:
            ai_message = chat([HumanMessage(content=prompt)])
            # 开心
            st.write(ai_message.content)

else:
    with st.container():
        # 提示用户输入openai_api_key
        st.warning("请先输入openai_api_key。")


