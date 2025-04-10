# 🎥 YouTranscripta

**YouTranscripta** is an intelligent assistant that transcribes YouTube videos and enables users to ask questions about the video content using a RAG (Retrieval-Augmented Generation) pipeline with LangChain and OpenAI.

---

## 🚀 Features

- ✅ Extracts transcripts from YouTube videos automatically
- 🧠 Performs semantic search and question answering using LangChain + GPT
- 📌 Persists vector data locally with ChromaDB
- 🧹 Uses temporal windows to split transcripts for better context
- 📇 Retrieves and uses video metadata to enrich responses
- 🧪 Includes unit tests for all components
- 🎨 UI built with Streamlit for easy interaction

---

## 🧱 Architecture

```
YouTube Video URL
       ↓
Transcript Fetcher (youtube-transcript-api)
       ↓
Temporal Text Splitter
       ↓
Document Embedding (OpenAIEmbeddings)
       ↓
Vector Store (Chroma)
       ↓
RAG QA System (LangChain + OpenAI Chat Model)
       ↓
      Answer
```

---

## 🧰 Tech Stack

- Python 3.10+
- [LangChain](https://www.langchain.com/)
- [ChromaDB](https://docs.trychroma.com/)
- [OpenAI](https://openai.com/)
- [Streamlit](https://streamlit.io/)
- [youtube-transcript-api](https://pypi.org/project/youtube-transcript-api/)
- [yt-dlp](https://github.com/yt-dlp/yt-dlp)
- [loguru](https://github.com/Delgan/loguru)
- [python-decouple](https://github.com/henriquebastos/python-decouple)
- [Pytest]()

---

## 🧚 Running Tests

```bash
pytest
```

Covers:

- Metadata extraction
- Transcript fetching
- Temporal splitting
- Vector storage and retrieval
- QA system inference

---

## ▶️ How to Use

```bash
git clone https://github.com/ericksonlopes/YouTranscripta
cd youtranscripta
pip install -r requirements.txt
```

Create a `.env` file:

```
OPENAI_API_KEY=your_openai_key_here
```

Run the app:

```bash
streamlit run app.py
```

---

## 📂 Project Structure

```
core/
├── config.py               # Loads environment variables
├── metadata_extractor.py  # Extracts video metadata using yt-dlp
├── qa_system.py           # RAG-based QA pipeline setup
├── transcript.py          # Fetches transcript using YouTubeTranscriptAPI
├── temporal_text_splitter.py # Splits transcript into time-based windows
├── vectorstore.py         # Handles embedding + Chroma vectorstore
├── you_transcripta.py     # Facade that connects all components

app.py                     # Streamlit user interface
tests/                     # Pytest unit tests
```

---

## 💡 Example

Input:

- Video: `https://www.youtube.com/watch?v=dummy123`
- Question: *"What is the main topic of this video?"*

Output:

```
💡 Answer:
This video discusses the benefits and use cases of the 'caixinha turbo' accessory for your car...
```
