import streamlit as st


# 全局标题
st.set_page_config(page_title="OpenAI Settings",layout="wide")
# 页面标题
st.title("OpenAI Settings")

# 初始化OPEN_API_KEY输入框内容为空
if"OPENAI_API_KEY"not in st.session_state:
    #该函数用于储存共享变量
    st.session_state["OPENAI_API_KEY"] = ''

# OPEN_API_KEY输入框,输入返回openai_api_key,加密
openai_api_key = st.text_input("API KEY",value=st.session_state["OPENAI_API_KEY"],max_chars=None,key=None,type='password')


# 提交按钮
saved = st.button("Save")
# 点击保存的回应
if saved:
    st.session_state["OPENAI_API_KEY"] = openai_api_key

# 使用两个container显示OPENAI和PINECONE的设置、参数信息(两种方式)
with st.container():
    st.header("OpenAI Settings")
    # 允许使用markdown渲染数据信息，这里是两列表格
    st.markdown(
        f"""
        | OpenAI API Key |
        | -------------- |
        | {st.session_state["OPENAI_API_KEY"]} | 
        """
    )

