import streamlit as st
from summarizer import summarize_text

st.set_page_config(page_title="Text Summarizer", page_icon="📝")

st.title("📝 Text Summarization App")
st.write("Paste any long text below and get an instant summary!")

text_input = st.text_area("Enter your text here:", height=250)

style = st.selectbox(
    "Choose summary style:",
    ["brief", "detailed", "eli5"]
)

if st.button("Summarize"):
    if not text_input.strip():
        st.warning("Please enter some text first.")
    else:
        with st.spinner("Summarizing..."):
            summary = summarize_text(text_input, style)
        st.success("Done!")
        st.subheader("📌 Summary:")
        st.write(summary)