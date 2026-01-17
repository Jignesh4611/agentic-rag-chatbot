## Pull required models:
```bash
ollama pull llama3
ollama pull nomic-embed-text
```

### Start Ollama:

```bash
ollama serve
```

### Verify Ollama:

```bash
curl http://localhost:11435/api/tags
```

Run Backend Using Docker Hub Image

 ### Pull Image
```bash
docker pull jigs1234/rag-backend:latest
```

### Run Container
```bash
docker run -p 8000:8000 \
  -e OLLAMA_BASE_URL=http://host.docker.internal:11435 \
  jigs1234/rag-backend:latest
  ```

### Open browser:

http://localhost:8000/docs

### Run Frontend

Move to frontend folder:
```bash
cd frontend
npm install
npm run dev
```
