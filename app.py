from models.llm.ollama_llm import DeepSeekR1, Llama
from models.llm.prompts.structurizer import system_prompt, user_prompt
from prepocessing.llm import LLMTextPreprocessor
from postprocessing.postprocess import HTMLPostprocessor
from logger import get_logger
import streamlit as st
import time

class StructurizedText:
    def __init__(self):
        st.session_state["preprocessor"] = LLMTextPreprocessor()
        st.session_state["logger"] = get_logger()
        if "model" not in st.session_state:
            s = time.time()
            st.session_state["model"] = Llama()
            e = time.time()
            st.session_state["logger"].info(f"Model loaded in {e - s:.2f} seconds.")
        else:
            st.session_state["logger"].info("Model already loaded.")

    def execute(self):
        st.title("📄 Structurized Raw Text")
        input_text = st.text_area("**Input text**", height=200)

        if st.button("Generate Structurized Text"):
            if input_text:
                s = time.time()
                # apply preprocess
                clean_input_text = st.session_state["preprocessor"].get_cleaned_text(
                    input_text
                )

                st.session_state["logger"].debug(
                    f"preprocessed news text: {clean_input_text}"
                )
                st.session_state["logger"].debug(
                    f"LLM prompt: {system_prompt+user_prompt.format(clean_input_text)}"
                )

                # llm inference
                html_text = st.session_state["model"].generate(
                    system_prompt,
                    user_prompt.format(clean_input_text),
                )
                e = time.time()

                st.session_state["logger"].info(
                    f"Output generated in {e - s:.2f} seconds."
                )

                # postprocess
                is_pdf_saved = HTMLPostprocessor().html2pdf(html_text)
                st.session_state["logger"].info(
                    f"PDF generation status: {is_pdf_saved}."
                )

                st.write(is_pdf_saved)
            else:
                st.warning("Please enter some text to generate a structurized PDF output.")


if __name__ == "__main__":
    StructurizedText().execute()
