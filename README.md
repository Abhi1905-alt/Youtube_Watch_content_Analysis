# StreamAI - YouTube Clone with AI Productivity Tracker

StreamAI is a specialized full-stack YouTube clone framework built using Python. It tracking platform usage and user analytics natively through a relational storage backend, passing data pipelines directly into a Local/Cloud Generative AI layer to gauge target productivity metrics.

## 🛠️ Architecture & Technical Stack

- **Backend core:** Python 3.x using the **Flask** WSGI micro-framework.
- **Data Persistence Layer:** SQL relational environment via **SQLite3** for atomic transactional tracking of viewing streams.
- **AI Reasoning Engine:** Built with the native **Google GenAI SDK**, calling `gemini-2.5-flash` for high-throughput heuristic assessment of user behavior metrics.
- **Frontend Engine:** Semantic HTML5, CSS3 structural layout architecture, with dynamic variable binding executed via the server-side **Jinja2** template execution stack.

---

## 🎛️ Feature Run-Through & AI Processing Pipeline

1. **Structured Video Delivery Grid:** Serves content entries fetched straight from relational indexed arrays.
2. **Interactive Stream Isolation Hooks:** Opening an asset triggers an asynchronous write instruction updating database transaction arrays (`watch_history`).
3. **Structured AI Prompt Synthesizer:**
   - On landing inside the `/dashboard` route, an aggregated join query pulls down historical interactions.
   - The query parses categorical distributions over time, concatenating them into a structured prompt context layer.
   - The compiled analytical profile object is fired over API tunnels to Gemini, generating an explicit semantic breakdown of active consumption metrics alongside dynamic structural advice to align behavior back toward technical competency tracks.

---

## 🚀 Environment Initialization Protocols

### 1. Project Scaffolding Allocation
Isolate your development runtime environment explicitly using native virtual resource environments:
```bash
python -m venv venv
source venv/bin/activate  # On Windows execution pipelines use: venv\Scripts\activate