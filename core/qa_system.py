from langchain.chains.retrieval_qa.base import RetrievalQA
from langchain_chroma import Chroma
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from loguru import logger

class QASystem:
    """Question and Answer system based on vector retrieval."""

    def __init__(self, vectorstore: Chroma, video_id, model_name: str = "gpt-4o-mini", temperature: float = 0.3):
        self.video_id = video_id
        self.vectorstore = vectorstore
        self.llm = ChatOpenAI(model=model_name, temperature=temperature)
        self.qa_chain = self._setup_qa_chain()

    def _setup_qa_chain(self) -> RetrievalQA:
        """Sets up the QA chain."""
        logger.info("Setting up the question and answer chain...")
        prompt = self._create_prompt()

        qa_chain = RetrievalQA.from_chain_type(
            llm=self.llm,
            retriever=self.vectorstore.as_retriever(
                search_type="mmr",
                filter={"video_id": self.video_id},
            ),
            return_source_documents=True,
            chain_type_kwargs={"prompt": prompt}
        )
        logger.success("QA chain successfully set up.")
        return qa_chain

    @staticmethod
    def _create_prompt() -> PromptTemplate:
        """Creates the prompt template."""
        return PromptTemplate(
            input_variables=["question"],
            template="""
            You are an intelligent assistant who has read the transcript of a YouTube video.

            Based on the following extracted content from the video:

            {context}

            Provide a detailed and well-structured answer to the following question:

            {question}
            """
        )

    def ask(self, question: str) -> str:
        """Performs a query to the QA system."""
        logger.info(f"Asking question to the system: {question}")
        result = self.qa_chain.invoke({"query": question})
        logger.success("Answer successfully retrieved.")
        return result["result"]
