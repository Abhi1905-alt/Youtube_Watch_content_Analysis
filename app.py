import os
from flask import Flask, render_template, request, redirect, url_for, flash
from database import get_db_connection, init_db
from google import genai

app = Flask(__name__)
app.secret_key = 'super_secret_key_change_this'

# Initialize Database on boot
init_db()

# Initialize Gemini Client
# Ensure GEMINI_API_KEY is set in your environment variables
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")
ai_client = genai.Client() if GEMINI_API_KEY else None

@app.route('/')
def index():
    conn = get_db_connection()
    videos = conn.execute('SELECT * FROM videos').fetchall()
    conn.close()
    return render_template('index.html', videos=videos)

@app.route('/watch/<int:video_id>')
def watch(video_id):
    conn = get_db_connection()
    video = conn.execute('SELECT * FROM videos WHERE id = ?', (video_id,)).fetchone()
    
    if video:
        # Log video into watch history
        conn.execute('INSERT INTO watch_history (video_id) VALUES (?)', (video_id,))
        conn.commit()
        
    conn.close()
    return render_template('watch.html', video=video)

@app.route('/dashboard')
def dashboard():
    conn = get_db_connection()
    
    # 1. Fetch entire watch history with video context
    history = conn.execute('''
        SELECT h.watched_at, v.title, v.category, v.description 
        FROM watch_history h
        JOIN videos v ON h.video_id = v.id
        ORDER BY h.watched_at DESC
    ''').fetchall()
    
    # 2. Extract Category Breakdown Metrics for UI display
    metrics = conn.execute('''
        SELECT v.category, COUNT(h.id) as count 
        FROM watch_history h
        JOIN videos v ON h.video_id = v.id
        GROUP BY v.category
        ORDER BY count DESC
    ''').fetchall()
    
    conn.close()

    # 3. Compile context string for the AI Analyzer
    if history:
        history_summary = "\n".join([f"- {row['title']} (Category: {row['category']})" for row in history])
    else:
        history_summary = "No watch history available yet."

    ai_feedback = "Please set your GEMINI_API_KEY environment variable to generate AI analysis."
    
    # 4. Trigger Gemini Client Analysis
    if ai_client and history:
        try:
            prompt = f"""
            You are a helpful behavioral productivity AI. Review the user's YouTube watch history provided below:
            
            {history_summary}
            
            Based on this history:
            1. Analyze what type of content they are watching the most and state their current distraction vs productivity trends.
            2. Give them specific, actionable constructive feedback on their consumption patterns.
            3. Recommend technical or educational topics they *should* watch next to remain highly productive and align with professional development goals (e.g., Computer Science, Engineering, Business foundations).
            
            Format your response clearly using markdown bullet points and headings. Keep it direct and encouraging.
            """
            
            response = ai_client.models.generate_content(
                model='gemini-2.5-flash',
                contents=prompt
            )
            ai_feedback = response.text
        except Exception as e:
            ai_feedback = f"Error generating AI feedback: {str(e)}"
    elif not history:
        ai_feedback = "Watch some videos first to populate your history and unlock AI insights!"

    return render_template('dashboard.html', metrics=metrics, history=history, ai_feedback=ai_feedback)

if __name__ == '__main__':
    app.run(debug=True)