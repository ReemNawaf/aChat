# 🐍 FastAPI Dummy Backend

This is a minimal Python backend built with FastAPI. It has a single `/message` POST endpoint that receives a message and returns it in the response — useful for testing frontend integration.

---

## 🔧 Requirements

- Python 3.8+
- `pip`

---

## 🚀 Setup Instructions

### 1. Clone the repo and navigate into it

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload --port 8000
```