# 🧠 YouTranscripta

**YouTranscripta** is an intelligent tool that transcribes YouTube videos and enables contextual Q&A using RAG (Retrieval-Augmented Generation), LangChain, and ChatGPT.

## 🚀 Overview

With YouTranscripta, you can:
- Automatically transcribe YouTube videos using their `video_id`.
- Store transcripts in a vector database (ChromaDB).
- Ask natural language questions about the video content and receive contextual answers.

## 🧩 Architecture

The system is composed of:

- `TranscriptProcessor`: Fetches video transcript using `youtube_transcript_api`.
- `TemporalTextSplitter`: Splits the transcript into overlapping time-based windows.
- `VectorStoreHandler`: Generates and stores embeddings in ChromaDB using `OpenAIEmbeddings`.
- `QASystem`: Uses LangChain + ChatGPT to answer questions based on vector data filtered by `video_id`.
- `YouTranscripta`: A facade class that integrates all steps into a simple interface.

## 🛠️ Installation

1. Clone the repository:

```bash
git clone https://github.com/your-user/youtranscripta.git
cd youtranscripta
```

2. Create a virtual environment and install dependencies:

```bash
pip install pipenv
pipenv install
```

3. Create a `.env` file with your OpenAI key:

```ini
OPENAI_API_KEY=your-openai-key-here
```

## 🧪 Usage

Edit and run the `main.py` file:

```python
if __name__ == '__main__':
    VIDEO_ID = "MAo7Z8UttyY"
    yt = YouTranscripta(video_id=VIDEO_ID)
    question = "What are the main points discussed in the video?"
    answer = yt.ask(question)
    print(answer)
```

## 📦 Project Structure

```
.
├── core/
│   ├── config.py
│   ├── qa_system.py
│   ├── splitter.py
│   ├── transcript.py
│   └── vectorstore.py
├── main.py
├── Pipfile
├── Pipfile.lock
```

## 🤖 Technologies

- [LangChain](https://python.langchain.com/)
- [ChromaDB](https://www.trychroma.com/)
- [OpenAI](https://openai.com/)
- [YouTube Transcript API](https://pypi.org/project/youtube-transcript-api/)
- [Python 3.11+](https://www.python.org/)

## 💡 Future Improvements

- Web interface with URL input support
- Multi-language transcript support
- Persisting transcripts in SQL databases (e.g., PostgreSQL)
- Automatic video summarization

## 📄 License

MIT License.
