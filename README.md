# 🎥 StreamAI — Data-Driven Video Platform & Behavioral Evaluation Matrix

StreamAI is a full-stack video streaming application engineered with a Python-centric architecture. The platform bridges media presentation layers with automated backend database telemetry to track user consumption patterns, processing platform utilization logs to evaluate viewing distributions over time.

---

## 🛠️ Architecture & Technical Stack

- **Backend core:** Python 3.x using the high-performance **Flask** WSGI micro-framework.
- **Data Persistence Layer:** Relational structure via **SQLite3** ensuring ACID-compliant transaction logging.
- **Analytical Reasoning Component:** Built using the external reasoning model integration to parse semantic context tokens.
- **Frontend Engine:** Semantic HTML5, CSS3 structural layout architecture, with dynamic content bindings executed via the server-side **Jinja2** template execution stack.

---

## 🚀 Key System Mechanics

1. **Transactional Event Logging:** Every video playback instance triggers an immediate, asynchronous database instruction, capturing video metadata, categorization arrays, and temporal markers into a centralized `watch_history` schema.
2. **Behavioral Evaluation Matrix:** On loading the analytics dashboard, the application executes optimized SQL join and aggregation queries to process usage density over time.
3. **Targeted Productivity Recommendations:** The system isolates entertainment consumption metrics from instructional progression data, translating raw user interaction weights into actionable feedback paths tailored to pivot user focus toward technical and professional milestones.

---

## 💻 Environment Staging & Initialization

### 1. Initialize Virtual Environment Isolation
Isolate project boundaries away from systemic environment scopes:
```bash
python -m venv venv
source venv/bin/activate  # On Windows execution pipelines use: venv\Scripts\activate

pip install -r requirements.txt

Set your target environment variable parameter straight inside your active shell terminal session profile before initializing data loops:

# Mac / Linux environments
export GEMINI_API_KEY="your_actual_integration_api_key_string"

# Windows PowerShell environments
$env:GEMINI_API_KEY="your_actual_integration_api_key_string"