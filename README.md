# WebReinvent Rank Tracker (Assignment)

This is a full-stack AI-powered application that tracks WebReinvent’s Google search rankings for specific keywords using an agentic system.

---

## 📦 Tech Stack

- **Frontend**: React 19 (Vite)
- **Backend**: FastAPI (served using `uv`)
- **Tools**:

  - `watchfiles` (auto-reload backend on changes)
  - `concurrently` (run frontend & backend together)
  - `.venv` for Python environment
  - docker for running ollama mistral

## 🧑‍💻 How to Run (Step-by-Step)

### 0. Setup Ollama locally with docker

#### a.Pull Ollama Docker Image

```bash
    docker run -d -v ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama
```

#### b.Go to Cmd or powershell and run after pulling image

```bash
    docker exec -it <process-id> bash 
```

#### c.Try to run mistral

```bash
    ollama run mistral
```

if it will not work download manually

### 1. Backend Setup

```bash
cd Backend
python -m venv .venv
.venv\Scripts\activate     # On Mac/Linux: source .venv/bin/activate
uv pip install -r requirements.txt
uv run backend_api.py      # OR use watchfiles for hot-reload
```

Backend will be available at:

```
http://127.0.0.1:8000
```

### 2. Frontend Setup

```bash
cd ../FrontEnd
npm install
npm run dev
```

Frontend will run at:

```
http://localhost:5173
```

### 3. Run Both Together (Frontend + Backend)

In the `FrontEnd/package.json`, two scripts are defined:

```json
"backend": "cd ../Backend && watchfiles \"cmd /c set PYTHONIOENCODING=utf-8 && uv run backend_api.py\" .",
"dev": "concurrently \"npm run vite\" \"npm run backend\""
```

or 

In the `FrontEnd/package.json`, two scripts are defined:

```json
"backend": "cd ../Backend && python -m watchfiles \"cmd /c set PYTHONIOENCODING=utf-8 && uv run backend_api.py\" ."
"dev": "concurrently \"npm run vite\" \"npm run backend\""
```



Use:

```bash
npm run dev
```

---

## ⚠️ Warnings You Might See

- **PydanticDeprecationWarning**Replace:

  ```python
  Field(..., required=True)
  ```

  With:

  ```python
  Field(..., json_schema_extra={"required": True})
  ```
- **WebSocket Deprecation**
  These can be safely ignored unless WebSockets are actively used.

## 📌 Submission Notes

- All components work in sync: React + FastAPI + WatchFiles
- Project has been tested and verified on local setup using:
  - Node.js v18+
  - Python 3.10+
  - Windows 11 (PowerShell)
