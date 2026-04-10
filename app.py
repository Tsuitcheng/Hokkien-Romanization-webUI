import streamlit as st
from taibun import Converter

# 设置页面标题
st.set_page_config(page_title="闽南语泉漳组字音转换器", page_icon="🗣️💬")
st.title("闽南语泉漳组汉字-读音转写转换")

# 创建侧边栏选项
st.sidebar.header("转换设置")
system = st.sidebar.selectbox("选择读音转写方案", ["Tailo", "POJ", "Zhuyin", "TLPA", "Pingyim", "IPA"], help="Tailo: 台罗，POJ: 白话字，Zhuyin: 台湾方音符号，TLPA: 台湾语言音标方案，Pingyim: 闽南话拼音方案，IPA: 国际音标")
dialect_mapping = {"漳腔": "south", "泉腔": "north", "新加坡偏泉腔": "singapore"}
accent_label = st.sidebar.selectbox("选择口音", list(dialect_mapping.keys()), help="泉腔：厦门、台北口音，漳腔：台湾优势口音")
dialect_code = dialect_mapping[accent_label]

# 输入框
text_input = st.text_area("请输入闽南语汉字：", "你好，你食饱未？")

# 转换逻辑
if st.button("开始转换"):
    if text_input.strip() == "":
        st.warning("你尚未输入文字，请输入后再进行转换。")
    else:
        try:
            # 初始化转换器
            c = Converter(system=system, dialect=dialect_code)
            result = c.get(text_input)
            
            # 显示结果
            st.subheader("转换结果：")
            st.success(result)
            
            # 辅助信息
            st.info(f"当前配置：转写={system}，口音={accent_label}")
        except Exception as e:
            st.error(f"转换过程中出现错误：{e}")

# 页脚说明
st.markdown("---")
st.caption("基于 Taibun 库构建。支持闽南语分词、多种转写方案转换。")