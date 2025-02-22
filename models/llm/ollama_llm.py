from .llm import LLM
import ollama
import re
import streamlit as st


class Ollama(LLM):
    def __init__(self, model):
        """input model name of same name as pulled using ollama command"""
        self.model = model

    def generate(self, system_prompt, user_prompt):
        """return output of ollama model result"""
        try:
            response = ollama.chat(
                model=self.model,
                messages=[
                    {
                        "role": "system",
                        "content": system_prompt,
                    },
                    {
                        "role": "user",
                        "content": user_prompt,
                    },
                ],
            )
            output = response["message"]["content"]
            st.session_state["logger"].debug(f"Ollama LLM output: {output}")

            return output

        except Exception as e:
            raise f"{self.model} failed to generate Headline due to {e}"


class DeepSeekR1(Ollama):
    def __init__(self, model="llama3.1:latest"):
        self.model = model

    def extract_headline(self, text):
        reason = " ".join(re.findall(r"<think>(.*?)</think>", text, flags=re.DOTALL))
        headline = re.split(r"</think>", text)[-1].strip()
        return reason, headline
