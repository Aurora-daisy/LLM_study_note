# app.py
import json

import streamlit as st
from ai_utils import sentiment_analyse, summarization, keyword_extraction, translate

st.set_page_config(page_title="AI文本处理工具箱", layout="wide")
st.title("🛠️ 多功能AI文本处理工具箱")
st.markdown("基于DeepSeek API实现，支持情感分析、摘要、关键词提取、翻译。")

# 侧边栏选择功能
function = st.sidebar.selectbox(
    "选择功能",
    ["情感分析", "文本摘要", "关键词提取", "翻译"]
)

# 主界面
st.header(function)


input_text = st.text_area("输入文本", height=200)

if st.button("运行", type="primary"):
    if not input_text.strip():
        st.warning("请输入文本")
        st.stop()

    with st.spinner("AI正在思考中..."):
        try:
            if function == "情感分析":
                result_json = sentiment_analyse(input_text)
                result=json.loads(result_json)
                sentiment = result["sentiment"]
                text = result["text"]
                st.success(f"文本：{text} 情感：{sentiment}")
                # 可以加个简单的仪表
                if sentiment == "积极":
                    st.markdown("😊 积极")
                elif sentiment == "消极":
                    st.markdown("😞 消极")
                else:
                    st.markdown("😐 中性")

            elif function == "文本摘要":
                result = summarization(input_text)
                #st.markdown("**摘要：**")
                st.write(result)

            elif function == "关键词提取":
                result = keyword_extraction(input_text)
                #keywords = result["keywords"]
                #st.markdown("**关键词：**")
                st.write(result)

            elif function == "翻译":
                result = translate(input_text)
                st.markdown("**翻译结果：**")
                st.write(result)

        except Exception as e:
            st.error(f"处理失败：{str(e)}")

st.markdown("---")
st.caption("注意：免费API可能有速率限制，请合理使用。")