from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import streamlit as st
import os
from langchain_core.prompts import PromptTemplate


load_dotenv()


model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash", 
    api_key=os.getenv("GOOGLE_API_KEY")
)


st.title("🔍 Smart Research Summarization Tool")
st.markdown("Use AI to summarize your research paper content by focus and length.")

user_input = st.text_area("🧠 Paste your research text or abstract below:", height=220)


summarization_type = st.selectbox(
    "📚 Choose summarization type:",
    ["General", "Codebase", "Contextual", "Research", "Business"]
)

summary_length = st.selectbox(
    "📏 Choose summary length:",
    ["Short", "Medium", "Long"]
)


template = """
You are an expert research assistant. Summarize the following academic paper 
using a {summary_type} approach in a {summary_length} format.

The summary must:
- Maintain an academic and objective tone.
- Include key findings, methodology, and implications.
- Avoid redundancy, filler words, or opinions.
- Preserve technical terms accurately.

--- Research Paper Content ---
{text}
"""

prompt_template = PromptTemplate(
    input_variables=["summary_type", "summary_length", "text"],
    template=template,
)


if st.button("✨ Generate Summary"):
    if not user_input.strip():
        st.warning("Please enter some text to summarize.")
    else:
        with st.spinner("Generating summary... ⏳"):
            try:
               
                final_prompt = prompt_template.format(
                    summary_type=summarization_type,
                    summary_length=summary_length,
                    text=user_input
                )

       
                response = model.invoke(final_prompt)
                summary = response.content.strip()

           
                st.subheader("🧠 Summary:")
                st.text_area("Generated Summary", summary, height=250)

            except Exception as e:
                st.error(f"⚠️ Error: {str(e)}")
