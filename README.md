# agentic-rag-backend


////Pull required models:

Pull required models:

ollama pull llama3
ollama pull nomic-embed-text

Start Ollama:

ollama serve
Verify Ollama:

curl http://localhost:11435/api/tags

🐳 Option 1: Run Backend Using Docker Hub Image

⚠️ Replace YOUR_DOCKER_USERNAME with your actual Docker Hub username.

🔽 Pull Image
docker pull jigs1234/rag-backend:latest

▶️ Run Container
docker run -p 8000:8000 \
  -e OLLAMA_BASE_URL=http://host.docker.internal:11435 \
  jigs1234/rag-backend:latest

Open browser:

http://localhost:8000/docs

🌐 Run Frontend

Move to frontend folder:

cd frontend
npm install
npm run dev


Open browser:

http://localhost:5173

////project structure : 

agentic-rag-chatbot/
│
├── backend/
│   ├── app.py
│   ├── rag.py
│   ├── agent.py
│   ├── requirements.txt
│   └── Dockerfile
│
├── frontend/
│   ├── src/
│   ├── public/
│   └── package.json
│
├── .gitignore
├── .dockerignore
├── README.md
└── PROJECT_DOCUMENTATION.md
