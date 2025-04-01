import streamlit as st
from langchain_openai import ChatOpenAI
from langchain.schema import (HumanMessage,AIMessage)


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


# 维护会话状态列表,用message这个键值，管理所有的历史消息
if "messages" not in st.session_state:
    st.session_state["messages"] = []


# 固定在最底部
prompt = st.chat_input("Type something...")

# 当chat实例不为空,完成实例
if chat:
    with st.container():
        st.header("Chat with GPT")

        for message in st.session_state["messages"]:
            if isinstance(message, HumanMessage):
                with st.chat_message("user"):
                    st.markdown(message.content)
            elif isinstance(message, AIMessage):
                with st.chat_message("assistant"):
                    st.markdown(message.content)

        # prompt = st.text_input("Prompt", value="", max_chars=None, key=None, type='default')

        # 提交按钮
        #asked = st.button("Ask")
        #if asked:
        # 实现历史对话
        if prompt:
            # 当提问时追加提问的历史消息
            st.session_state["messages"].append(HumanMessage(content=prompt))
            with st.chat_message("user"):
                st.markdown(prompt)
            ai_message = chat([HumanMessage(content=prompt)])
            # 追加回答的历史消息
            st.session_state["messages"].append(ai_message)
            with st.chat_message("assistant"):
                st.markdown(ai_message.content)


else:
    with st.container():
        # 提示用户输入openai_api_key
        st.warning("请先输入openai_api_key。")


