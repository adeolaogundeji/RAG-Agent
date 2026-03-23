RAG PDF Question Answering System
A Retrieval-Augmented Generation (RAG) AI system that allows users to upload PDFs and ask
questions, returning accurate answers grounded in document content.
Features
- Upload PDFs and process automatically
- Chunking (1000 size, 200 overlap)
- OpenAI embeddings
- Qdrant vector database
- Semantic search
- AI answers with context
- Event-driven with Inngest
- Streamlit frontend

You will an api key (preferrably openai api key)
You also need a qdrant cloud account and database (create one for free using this link: https://login.cloud.qdrant.io/u/signup/identifier?state=hKFo2SAyaEh3WU50WHdweWp2U1pfa3BobFZQUkdNUlZMQmZOcKFur3VuaXZlcnNhbC1sb2dpbqN0aWTZIFYxc1lUblR3YldzOWVKYkhXeEowRy1qZGRKaXVmSXlqo2NpZNkgckkxd2NPUEhPTWRlSHVUeDR4MWtGMEtGZFE3d25lemc&gbraid=0AAAAAodw_9BOzFRN1PmTPKeGJFbAiOiy6&gclid=EAIaIQobChMIkojGvuy0kwMVdU1HAR0gzyGaEAAYASAAEgJotvD_BwE&utm_campaign=21029649098&utm_content=167551587268&utm_medium=cpc&utm_source=google&utm_term=qdrant&__hstc=265983056.0aacb43d01e9b620af352216192fddbd.1774228577248.1774228577248.1774228577248.1&__hssc=265983056.1.1774228577248&__hsfp=153f91a84277f91825e2bd27780951b2)

Architecture:

User → Streamlit → Inngest → FastAPI → Embeddings → Qdrant → LLM → Answer


How It Works
1. Upload PDF → chunk → embed → store -> Ask question → embed → search → LLM answer

Tech Stack
FastAPI, Inngest, Qdrant, OpenAI, Streamlit


Installation: uv add fastapi inngest llama-index-core llama-index-readers-file python-dotenv qdrant-client uvicorn streamlit openai

Run Commands:

Backend(main.py): uv run uvicorn main:app

Frontend (streamlit_app.py): uv run streamlit run .\streamlit_app.py

Inngest server: npx inngest-cli@latest dev -u http://127.0.0.1:8000/api/inngest --no-discovery
