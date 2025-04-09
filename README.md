# 🎙️ YouTranscripta

**YouTranscripta** is an intelligent tool that takes a YouTube video ID, transcribes its audio content, stores the transcription in a vector database, and enables intelligent queries using **LangChain**, **OpenAI GPT**, and RAG (Retrieval-Augmented Generation).

## ✨ Features

- 🔍 Automatic transcription of YouTube videos (multi-language support).
- 📚 Vector store using **LangChain Chroma**.
- 🤖 Question-Answering system powered by **GPT models**.
- 🧠 Intelligent RAG-based queries with contextualization.
- ⏱️ Time-based windowed segmentation of the transcript with metadata.

---

## 🚀 How It Works

1. The system receives a `video_id` from YouTube.
2. It fetches and processes the video transcription.
3. The transcription is split into temporal windows and embedded.
4. These vectorized segments are stored with metadata in a Chroma DB.
5. A QA system answers user queries based on the most relevant parts of the transcript.

---

## 🛠️ Tech Stack

- [Python 3.10+](https://www.python.org/)
- [LangChain](https://www.langchain.com/)
- [OpenAI API](https://platform.openai.com/)
- [Chroma Vector DB](https://docs.trychroma.com/)
- [youtube-transcript-api](https://pypi.org/project/youtube-transcript-api/)
- [Loguru](https://github.com/Delgan/loguru)
- [python-decouple](https://pypi.org/project/python-decouple/)

---

## 📦 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/youtranscripta.git
   cd youtranscripta
