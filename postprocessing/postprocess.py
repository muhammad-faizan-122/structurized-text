from abc import ABC
import pdfkit
import re


class TextPostprocessor(ABC):
    def __init__(self):
        pass


class HTMLPostprocessor:
    def __init__(self):
        pass

    def remove_image_tags(self, html_text):
        """
        Removes <img> tags from an HTML string without removing surrounding text.
        """
        return re.sub(r"<img[^>]*>", "", html_text, flags=re.IGNORECASE)
    
    def remove_triple_backticks(self, html_text):
        """
        Removes triple backticks from an HTML string without removing surrounding text.
        """
        return re.sub(r'^[`\s]+|[`s]+$', '', html_text)

    def html2pdf(self, html_text, output_path="output/output.pdf"):
        """save the html in the output PDF file"""
        if not html_text:
            return "No HTML text provided."

        clean_html = self.remove_image_tags(html_text)
        clean_html = self.remove_triple_backticks(clean_html)

        try:

            options = {
                "page-size": "Letter",
                "margin-top": "0.75in",
                "margin-right": "0.75in",
                "margin-bottom": "0.75in",
                "margin-left": "0.75in",
                "encoding": "UTF-8",
                "custom-header": [("Accept-Encoding", "gzip")],
                "cookie": [
                    ("cookie-empty-value", '""'),
                    ("cookie-name1", "cookie-value1"),
                    ("cookie-name2", "cookie-value2"),
                ],
                "no-outline": None,
            }

            pdfkit.from_string(clean_html, output_path, options=options)
            return f"PDF successfully saved at {output_path}."
        except Exception as e:
            print(e)
            raise f"Failed to convert HTML to PDF due to {e}"
