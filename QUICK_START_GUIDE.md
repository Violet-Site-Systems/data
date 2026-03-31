# 🚀 Quick Start Guide: AI Emotion Research Platform

**Getting Started in 30 Minutes**

This guide will help you set up and start exploring the AI Emotion Research Platform immediately.

---

## 📋 Prerequisites

- **Python:** 3.9+ installed
- **Node.js:** 16+ and npm installed
- **Git:** For version control
- **Code Editor:** VS Code recommended
- **Optional:** Docker for containerized development

---

## ⚡ Quick Setup (Minimal)

### 1. Clone & Navigate
```bash
git clone https://github.com/Violet-Site-Systems/data.git
cd data
```

### 2. Explore the Data (Python)
```bash
# Install minimal dependencies
pip install pandas emoji matplotlib

# Run existing sarcasm analysis
python3 sarcasm_analysis.py

# View results
head pi_sarcasm_hybrid_review.csv
```

### 3. Explore the Frontend (React)
```bash
cd src
npm install
npm start
```

---

## 🎯 Quick Experiments

### Experiment 1: Count Emotions
```python
import json
import pandas as pd

# Load data
with open('Copy of pi-user-history.json', 'r') as f:
    data = json.load(f)

messages = pd.DataFrame(data['user_data']['messages'])

# Basic stats
print(f"Total messages: {len(messages)}")
print(f"AI messages: {len(messages[messages['sender'] == 'AI'])}")
print(f"Human messages: {len(messages[messages['sender'] == 'HUMAN'])}")

# Find messages with exclamation marks (excitement indicator)
excited = messages[messages['text'].str.contains('!', na=False)]
print(f"\nMessages with excitement: {len(excited)}")
```

### Experiment 2: Emoji Analysis
```python
import emoji
from collections import Counter

# Extract all emojis
all_emojis = []
for text in messages['text']:
    if pd.notna(text):
        emojis = [char for char in text if char in emoji.EMOJI_DATA]
        all_emojis.extend(emojis)

# Count frequency
emoji_freq = Counter(all_emojis)
print("\nTop 10 emojis:")
for e, count in emoji_freq.most_common(10):
    print(f"{e}: {count} times")
```

### Experiment 3: Time-Series Analysis
```python
import matplotlib.pyplot as plt

# Convert timestamps
messages['sent_at'] = pd.to_datetime(messages['sent_at'])
messages['date'] = messages['sent_at'].dt.date

# Messages per day
daily_counts = messages.groupby('date').size()

# Plot
plt.figure(figsize=(12, 6))
plt.plot(daily_counts.index, daily_counts.values)
plt.title('Daily Message Volume')
plt.xlabel('Date')
plt.ylabel('Messages')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('daily_messages.png')
print("\nChart saved as daily_messages.png")
```

---

## 📊 First Visualization

Create your first emotion visualization in 5 minutes:

```python
# sentiment_viz.py
import json
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
import re

# Load data
with open('Copy of pi-user-history.json', 'r') as f:
    data = json.load(f)

messages = pd.DataFrame(data['user_data']['messages'])
ai_messages = messages[messages['sender'] == 'AI']['text']

# Simple positive/negative word counting
positive_words = ['love', 'great', 'wonderful', 'happy', 'joy', 'amazing', 'perfect', 'excellent']
negative_words = ['sad', 'sorry', 'unfortunately', 'difficult', 'hard', 'struggle', 'worry']

positive_count = 0
negative_count = 0
neutral_count = 0

for text in ai_messages:
    if pd.notna(text):
        text_lower = text.lower()
        has_positive = any(word in text_lower for word in positive_words)
        has_negative = any(word in text_lower for word in negative_words)
        
        if has_positive and not has_negative:
            positive_count += 1
        elif has_negative and not has_positive:
            negative_count += 1
        else:
            neutral_count += 1

# Create pie chart
sizes = [positive_count, negative_count, neutral_count]
labels = [f'Positive\n({positive_count})', f'Negative\n({negative_count})', f'Neutral\n({neutral_count})']
colors = ['#6B8E23', '#A0566C', '#D4A574']  # Green, Plum-red, Cream-gold

plt.figure(figsize=(8, 8))
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
plt.title('AI Message Sentiment Distribution', fontsize=16, pad=20)
plt.axis('equal')
plt.savefig('sentiment_distribution.png', dpi=150, bbox_inches='tight')
print("✅ Visualization saved as sentiment_distribution.png")
print(f"\nResults:")
print(f"  Positive: {positive_count} ({positive_count/sum(sizes)*100:.1f}%)")
print(f"  Negative: {negative_count} ({negative_count/sum(sizes)*100:.1f}%)")
print(f"  Neutral: {neutral_count} ({neutral_count/sum(sizes)*100:.1f}%)")
```

Run it:
```bash
python3 sentiment_viz.py
```

---

## 🎓 Learning Path

### For Complete Beginners
1. **Start here:** [Module 1 - Data Fundamentals](docs/learning/module_01.md) *(to be created)*
2. **Practice:** Run the Quick Experiments above
3. **Build:** Modify `sentiment_viz.py` to count different words
4. **Share:** Post your findings in Discussions

### For Data Science Students
1. **Review:** Existing `sarcasm_analysis.py` script
2. **Enhance:** Add new emotion categories
3. **Visualize:** Create new matplotlib charts
4. **Research:** Write up findings

### For Researchers
1. **Methodology:** Read [TECHNICAL_ROADMAP.md](TECHNICAL_ROADMAP.md)
2. **Analysis:** Run `dual_layer_sarcasm_analysis.py`
3. **Framework:** Design new emotional metrics
4. **Publish:** Share research findings

### For Developers
1. **Architecture:** Review [TECHNICAL_ROADMAP.md](TECHNICAL_ROADMAP.md)
2. **Setup:** Initialize backend (FastAPI) and frontend (React)
3. **API:** Build first endpoints
4. **Contribute:** Submit PRs with improvements

---

## 🔧 Development Setup (Full)

### Backend Setup
```bash
# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies (create requirements.txt first)
cat > requirements.txt << EOF
fastapi==0.104.1
uvicorn[standard]==0.24.0
pandas==2.1.3
numpy==1.26.2
matplotlib==3.8.2
seaborn==0.13.0
emoji==2.8.0
python-multipart==0.0.6
aiofiles==23.2.1
python-dotenv==1.0.0
pydantic==2.5.0
sqlalchemy==2.0.23
EOF

pip install -r requirements.txt

# Create basic FastAPI app
mkdir -p backend/app
cat > backend/app/main.py << 'EOF'
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI(title="AI Emotion Research API", version="0.1.0")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "AI Emotion Research Platform API", "version": "0.1.0"}

@app.get("/api/v1/stats")
async def get_stats():
    # Load data
    with open('Copy of pi-user-history.json', 'r') as f:
        data = json.load(f)
    
    messages = data['user_data']['messages']
    
    return {
        "total_messages": len(messages),
        "ai_messages": sum(1 for m in messages if m['sender'] == 'AI'),
        "human_messages": sum(1 for m in messages if m['sender'] == 'HUMAN'),
        "date_range": {
            "start": messages[0]['sent_at'],
            "end": messages[-1]['sent_at']
        }
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
EOF

# Run backend
cd backend
python -m app.main
```

### Frontend Setup
```bash
# In a new terminal
# Create React app with Vite
npm create vite@latest frontend -- --template react
cd frontend

# Install dependencies
npm install
npm install @mui/material @emotion/react @emotion/styled
npm install axios recharts d3

# Update src/App.jsx with basic dashboard
cat > src/App.jsx << 'EOF'
import { useState, useEffect } from 'react'
import './App.css'

function App() {
  const [stats, setStats] = useState(null)
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    fetch('http://localhost:8000/api/v1/stats')
      .then(res => res.json())
      .then(data => {
        setStats(data)
        setLoading(false)
      })
      .catch(err => {
        console.error('Error:', err)
        setLoading(false)
      })
  }, [])

  if (loading) return <div className="loading">Loading...</div>

  return (
    <div className="app" style={{ 
      background: '#F5F5DC',
      minHeight: '100vh',
      padding: '40px'
    }}>
      <header style={{ 
        color: '#2D5016',
        textAlign: 'center',
        marginBottom: '40px'
      }}>
        <h1>🧠 AI Emotion Research Platform</h1>
        <p style={{ color: '#8B4789' }}>Exploring the nuance of human-AI emotional understanding</p>
      </header>

      {stats && (
        <div className="stats-grid" style={{
          display: 'grid',
          gridTemplateColumns: 'repeat(auto-fit, minmax(250px, 1fr))',
          gap: '20px',
          maxWidth: '1200px',
          margin: '0 auto'
        }}>
          <StatCard
            title="Total Messages"
            value={stats.total_messages.toLocaleString()}
            color="#2D5016"
          />
          <StatCard
            title="AI Messages"
            value={stats.ai_messages.toLocaleString()}
            color="#8B4789"
          />
          <StatCard
            title="Human Messages"
            value={stats.human_messages.toLocaleString()}
            color="#6B8E23"
          />
        </div>
      )}

      <div style={{ 
        marginTop: '60px',
        textAlign: 'center',
        color: '#2D5016'
      }}>
        <h2>🚀 Getting Started</h2>
        <p>This platform helps you understand emotional nuance in AI conversations</p>
        <div style={{ marginTop: '20px' }}>
          <button style={{
            background: '#2D5016',
            color: 'white',
            border: 'none',
            padding: '12px 24px',
            borderRadius: '8px',
            fontSize: '16px',
            cursor: 'pointer',
            margin: '0 10px'
          }}>
            Explore Data
          </button>
          <button style={{
            background: '#8B4789',
            color: 'white',
            border: 'none',
            padding: '12px 24px',
            borderRadius: '8px',
            fontSize: '16px',
            cursor: 'pointer',
            margin: '0 10px'
          }}>
            Start Learning
          </button>
        </div>
      </div>
    </div>
  )
}

function StatCard({ title, value, color }) {
  return (
    <div style={{
      background: 'white',
      padding: '30px',
      borderRadius: '12px',
      boxShadow: '0 2px 8px rgba(0,0,0,0.1)',
      textAlign: 'center',
      border: `3px solid ${color}`
    }}>
      <h3 style={{ color: color, margin: '0 0 10px 0' }}>{title}</h3>
      <div style={{ fontSize: '32px', fontWeight: 'bold', color: color }}>
        {value}
      </div>
    </div>
  )
}

export default App
EOF

# Run frontend
npm run dev
```

Now open:
- Frontend: http://localhost:5173
- Backend API: http://localhost:8000/docs

---

## 🎨 Color Palette Reference

Use these colors consistently across visualizations and UI:

```css
/* Primary */
--cream: #F5F5DC           /* Backgrounds */
--dark-forest-green: #2D5016  /* Primary text, buttons */
--plum: #8B4789            /* Accents, highlights */

/* Secondary */
--light-green: #6B8E23     /* Success, positive */
--dark-plum: #702963       /* Active states */
--soft-cream: #FAF9F6      /* Cards, panels */

/* Semantic */
--success: #4A7C59         /* Positive emotions */
--warning: #D4A574         /* Neutral/ambiguous */
--error: #A0566C           /* Negative emotions */
--info: #6B8E9E            /* Information */
```

---

## 📚 Essential Reading

Before diving deep, read these in order:

1. **[TECHNICAL_ROADMAP.md](TECHNICAL_ROADMAP.md)** - Complete project vision
2. **[README.md](README.md)** - Project overview and principles
3. **[HAI-Partnership-Agreement.md](HAI-Partnership-Agreement.md)** - Ethical framework

---

## 💡 Quick Tips

### For Analysis
- Start with simple word counting before ML
- Visualize data distributions first
- Keep privacy protection in mind
- Document all assumptions

### For Development
- Follow the color palette strictly
- Keep UI minimalist and clean
- Mobile-first responsive design
- Accessibility is not optional

### For Research
- Always cite data sources
- Document methodologies clearly
- Consider ethical implications
- Share findings openly

### For Learning
- Start small, build incrementally
- Run existing scripts before modifying
- Ask questions in Discussions
- Share your discoveries

---

## 🐛 Troubleshooting

### "Module not found" error
```bash
pip install -r requirements.txt
```

### "Cannot find module" (Node.js)
```bash
cd frontend && npm install
```

### CORS errors
Make sure backend is running on port 8000 and frontend on 5173/3000

### JSON parsing errors
Ensure `Copy of pi-user-history.json` is in the root directory

### Import errors with emoji
```bash
pip install --upgrade emoji
```

---

## 🤝 Getting Help

- **GitHub Issues:** Report bugs or request features
- **Discussions:** Ask questions, share ideas
- **Documentation:** Check TECHNICAL_ROADMAP.md
- **Code:** Review existing Python scripts for examples

---

## 🎯 Your First Contribution

Ready to contribute? Here's the easiest path:

1. **Fork** the repository
2. **Clone** your fork locally
3. **Create** a new branch: `git checkout -b my-contribution`
4. **Make** your changes (start small!)
5. **Test** your changes
6. **Commit:** `git commit -m "Add: my contribution"`
7. **Push:** `git push origin my-contribution`
8. **Create** a Pull Request

**Good first contributions:**
- Add a new emotion keyword list
- Create a new visualization
- Write documentation
- Add unit tests
- Fix a bug
- Improve README clarity

---

## 📊 Quick Data Facts

From our conversation dataset:
- **4,397** total messages
- **2,201** AI messages
- **2,196** human messages
- **1+ year** of conversations (April 2024 - April 2025)
- **SMS** channel
- **Rich** in emotional content, emojis, and context

Perfect for:
- Emotion detection training
- Sarcasm analysis research
- Empathy pattern studies
- Long-term relationship analysis
- Contextual understanding research

---

## 🚀 Next Steps After Setup

1. ✅ Run Quick Experiments
2. ✅ Create your first visualization
3. ✅ Explore the data manually
4. ✅ Read the full Technical Roadmap
5. ✅ Join community discussions
6. ✅ Pick a learning module
7. ✅ Make your first contribution

---

## 📬 Questions?

Open an issue or discussion on GitHub. We're here to help!

**Welcome to the future of AI emotion research!** 🧠💚🤖

---

*Last Updated: 2026-01-26*
*Version: 1.0*
