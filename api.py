from typing import Union
from fastapi import FastAPI
from models.llm.ollama_llm import DeepSeekR1, Llama
from models.llm.prompts.structurizer import system_prompt, user_prompt
from prepocessing.llm import LLMTextPreprocessor
from postprocessing.postprocess import HTMLPostprocessor
from logger import get_logger
import time


app = FastAPI()
logger = get_logger()


@app.get("/")
def welcome_pipeline():
    return "Welcome to Structurizer Pipeline"


@app.post("/structurized/")
def structurized(
    req_id: str, llm_type: str = "deepseek", unstructured_text: Union[str, None] = None
):
    clean_input_text = LLMTextPreprocessor().get_cleaned_text(unstructured_text)

    logger.debug(f"preprocessed news text: {clean_input_text}")
    logger.debug(f"LLM prompt: {system_prompt+user_prompt.format(clean_input_text)}")
    s = time.time()

    # llm inference
    if llm_type == "deepseek":
        model = DeepSeekR1()
        llm_out = model.generate(system_prompt, user_prompt.format(clean_input_text))
        think_process, html_text = model.get_structurize_html(llm_out)
    elif llm_type == "llama":
        model = Llama()
        html_text = model.generate(system_prompt, user_prompt.format(clean_input_text))

    e = time.time()

    logger.info(f"LLM Inference time: {e - s:.2f} seconds.")

    # postprocess
    is_pdf_saved = HTMLPostprocessor().html2pdf(
        html_text, output_path=f"output/{req_id}.pdf"
    )
    logger.info(f"PDF generation status: {is_pdf_saved}.")
    return {"html_text": html_text, "is_pdf_saved": is_pdf_saved}
