# 📄 Structurized Raw Text

This project takes unstructured text and enhances its readability by adding headings, subheadings, bullet points, and other formatting elements where necessary. The transformation is powered by the **Llama-3.1** model (using **Ollama**). The goal is to **structure the input text without altering its content** and generate a well-formatted **PDF output**.

## 🔹 High-Level Pipeline

```
Raw Input Text --> | HTML Converter | --> HTML Output --> | HTML to PDF | --> PDF Output
```

## 📌 Demo

![Unstructured text to Strucured text ](demo/structured_text.gif)

## ⚙️ Setup

### 1️⃣ Create a Conda Virtual Environment

```sh
conda create -n env_name python=3.11.11 -y
```

### 2️⃣ Install Dependencies

```sh
pip install -r requirements.txt

```
**For Ubuntu**
```sh
sudo apt-get install wkhtmltopdf 
```
**For macOS**
```sh
brew install homebrew/cask/wkhtmltopdf
```

### 3️⃣ Install Ollama and Pull the Model Locally

- Download and install **Ollama** based on your OS by following [this guide](https://ollama.com/download).
- Pull the required model using:

```sh
ollama run deepseek-r1:1.5b
```

### 4️⃣ Run the Application

```sh
streamlit run app.py
```

---

## ✅ To-Do List

- work for long text
- create endpoint which will take text and return html text.
- html to pdf conversion



📌 **Contributions & Feedback**
Feel free to raise issues or contribute to the repository to improve functionality. 🚀

