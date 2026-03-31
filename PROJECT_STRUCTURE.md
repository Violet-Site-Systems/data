# 📁 Project Structure Plan

## Current Structure (As-Is)

```
data/
├── .git/                              # Git repository
├── .github/
│   └── copilot-instructions.md        # AI agent guidance (6.4KB)
├── Copy of pi-user-history.json       # Conversation data (2.7MB)
├── PRIVATE-pi-user-history.json.backup # Backup copy (2.7MB)
├── HAI-Partnership-Agreement.html     # Partnership doc HTML (7.7KB)
├── HAI-Partnership-Agreement.md       # Partnership doc (5.8KB)
├── README.md                          # Main documentation (6.4KB)
├── TECHNICAL_ROADMAP.md               # Complete roadmap (44KB)
├── QUICK_START_GUIDE.md               # Getting started (14KB)
├── convert_to_html.py                 # Conversion utility (913B)
├── create_readable_version.py         # Data processing (2.5KB)
├── dual_layer_sarcasm_analysis.py     # Advanced sarcasm detection (7.9KB)
├── sarcasm_analysis.py                # Basic sarcasm detection (5.9KB)
├── show_readable_samples.py           # Sample display utility (2.1KB)
├── pi_emoji_messages_readable.csv     # Emoji analysis results (275KB)
├── pi_sarcasm_hybrid_review.csv       # Sarcasm review data (442KB)
├── pi_sarcasm_readable_analysis.csv   # Sarcasm analysis (1.2KB)
└── src/                               # React app starter
    ├── App.css
    ├── App.js                         # Todo app component
    └── index.js
```

**Total Size:** ~6.2MB  
**Key Assets:**
- 4,397 messages spanning April 2024 - April 2025
- Working Python analysis scripts (3 scripts)
- CSV analysis results (3 files)
- React starter components

---

## Proposed Structure (To-Be)

```
data/
├── .git/
├── .github/
│   ├── workflows/
│   │   ├── ci.yml                     # Continuous integration
│   │   ├── test.yml                   # Automated testing
│   │   └── deploy.yml                 # Deployment automation
│   └── copilot-instructions.md
│
├── docs/                              # 📖 Documentation
│   ├── README.md                      # Docs homepage
│   ├── api/
│   │   ├── endpoints.md               # API reference
│   │   ├── authentication.md          # Auth guide
│   │   └── examples.md                # Usage examples
│   ├── learning/
│   │   ├── module_01_fundamentals.md  # Module 1
│   │   ├── module_02_emotions.md      # Module 2
│   │   ├── module_03_advanced.md      # Module 3
│   │   └── module_04_qualia.md        # Module 4
│   ├── research/
│   │   ├── methodology.md             # Research methods
│   │   ├── emotional_framework.md     # Emotion taxonomy
│   │   └── papers/                    # Published research
│   ├── design/
│   │   ├── ui_components.md           # Component specs
│   │   ├── color_palette.md           # Design system
│   │   └── mockups/                   # UI mockups
│   └── ethics/
│       ├── rights_of_being.md         # Ethical framework
│       ├── data_privacy.md            # Privacy policy
│       └── governance.md              # Governance model
│
├── frontend/                          # ⚛️ React Frontend
│   ├── package.json
│   ├── package-lock.json
│   ├── vite.config.js
│   ├── .env.example
│   ├── public/
│   │   ├── index.html
│   │   ├── favicon.ico
│   │   └── assets/
│   │       └── images/
│   └── src/
│       ├── components/
│       │   ├── Dashboard/
│       │   │   ├── Dashboard.jsx
│       │   │   ├── StatsCard.jsx
│       │   │   └── RecentAnalysis.jsx
│       │   ├── Visualizer/
│       │   │   ├── VisualizerStudio.jsx
│       │   │   ├── EmotionNetwork.jsx
│       │   │   ├── EmotionSpace3D.jsx
│       │   │   ├── Timeline.jsx
│       │   │   └── SentimentHeatmap.jsx
│       │   ├── LearningHub/
│       │   │   ├── LearningHub.jsx
│       │   │   ├── ModuleCard.jsx
│       │   │   ├── Exercise.jsx
│       │   │   └── ProgressTracker.jsx
│       │   ├── DataExplorer/
│       │   │   ├── DataExplorer.jsx
│       │   │   ├── MessageList.jsx
│       │   │   ├── MessageDetail.jsx
│       │   │   └── SearchBar.jsx
│       │   ├── ResearchLab/
│       │   │   ├── ResearchLab.jsx
│       │   │   ├── ExperimentForm.jsx
│       │   │   └── ResultsViewer.jsx
│       │   └── shared/
│       │       ├── Header.jsx
│       │       ├── Navigation.jsx
│       │       ├── Footer.jsx
│       │       ├── Button.jsx
│       │       ├── Card.jsx
│       │       └── Loading.jsx
│       ├── pages/
│       │   ├── Home.jsx
│       │   ├── Dashboard.jsx
│       │   ├── Visualizer.jsx
│       │   ├── Learning.jsx
│       │   ├── Explorer.jsx
│       │   ├── Research.jsx
│       │   └── About.jsx
│       ├── hooks/
│       │   ├── useApi.js
│       │   ├── useAuth.js
│       │   ├── useAnalysis.js
│       │   └── useWebSocket.js
│       ├── services/
│       │   ├── api.js                 # API client
│       │   ├── auth.js                # Authentication
│       │   └── websocket.js           # WebSocket client
│       ├── utils/
│       │   ├── format.js              # Formatters
│       │   ├── validation.js          # Validators
│       │   └── constants.js           # Constants
│       ├── styles/
│       │   ├── theme.js               # MUI theme
│       │   ├── global.css             # Global styles
│       │   └── variables.css          # CSS variables
│       ├── App.jsx
│       ├── main.jsx
│       └── router.jsx
│
├── backend/                           # 🐍 Python Backend
│   ├── requirements.txt               # Python dependencies
│   ├── requirements-dev.txt           # Dev dependencies
│   ├── setup.py                       # Package setup
│   ├── pytest.ini                     # Test configuration
│   ├── .env.example                   # Environment template
│   ├── alembic/                       # Database migrations
│   │   ├── versions/
│   │   └── env.py
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py                    # FastAPI app
│   │   ├── config.py                  # Configuration
│   │   ├── dependencies.py            # FastAPI dependencies
│   │   ├── api/
│   │   │   ├── __init__.py
│   │   │   └── v1/
│   │   │       ├── __init__.py
│   │   │       ├── messages.py        # Message endpoints
│   │   │       ├── analysis.py        # Analysis endpoints
│   │   │       ├── visualization.py   # Viz endpoints
│   │   │       ├── learning.py        # Learning endpoints
│   │   │       └── research.py        # Research endpoints
│   │   ├── core/
│   │   │   ├── __init__.py
│   │   │   ├── emotion_analyzer.py    # Emotion detection
│   │   │   ├── sentiment_analyzer.py  # Sentiment analysis
│   │   │   ├── sarcasm_detector.py    # Sarcasm detection
│   │   │   ├── empathy_scorer.py      # Empathy scoring
│   │   │   ├── context_analyzer.py    # Context analysis
│   │   │   └── qualia_mapper.py       # Qualia framework
│   │   ├── ml/
│   │   │   ├── __init__.py
│   │   │   ├── models/
│   │   │   │   ├── __init__.py
│   │   │   │   ├── emotion_model.py
│   │   │   │   └── sarcasm_model.py
│   │   │   ├── training/
│   │   │   │   ├── __init__.py
│   │   │   │   ├── trainer.py
│   │   │   │   └── evaluator.py
│   │   │   └── inference/
│   │   │       ├── __init__.py
│   │   │       └── predictor.py
│   │   ├── visualization/
│   │   │   ├── __init__.py
│   │   │   ├── matplotlib_charts.py   # Chart generation
│   │   │   ├── plotly_charts.py       # Interactive charts
│   │   │   └── data_prep.py           # Data preparation
│   │   ├── db/
│   │   │   ├── __init__.py
│   │   │   ├── base.py                # Base class
│   │   │   ├── session.py             # DB session
│   │   │   └── models.py              # SQLAlchemy models
│   │   ├── schemas/
│   │   │   ├── __init__.py
│   │   │   ├── message.py             # Message schemas
│   │   │   ├── analysis.py            # Analysis schemas
│   │   │   └── user.py                # User schemas
│   │   └── utils/
│   │       ├── __init__.py
│   │       ├── privacy.py             # Redaction tools
│   │       ├── validation.py          # Validators
│   │       └── logging.py             # Logging utilities
│   └── tests/
│       ├── __init__.py
│       ├── conftest.py                # Pytest fixtures
│       ├── test_api/
│       │   ├── test_messages.py
│       │   └── test_analysis.py
│       ├── test_core/
│       │   ├── test_emotion_analyzer.py
│       │   └── test_sentiment.py
│       └── test_ml/
│           └── test_models.py
│
├── data/                              # 📊 Data Directory
│   ├── raw/
│   │   ├── Copy of pi-user-history.json
│   │   └── README.md                  # Data description
│   ├── processed/
│   │   ├── messages_clean.parquet     # Cleaned messages
│   │   ├── emotions_labeled.parquet   # Labeled emotions
│   │   └── metadata.json              # Processing metadata
│   ├── analysis/
│   │   ├── sarcasm_results.csv
│   │   ├── emotion_vectors.npy
│   │   ├── sentiment_timeseries.csv
│   │   └── empathy_scores.csv
│   ├── models/
│   │   ├── emotion_classifier.pkl
│   │   ├── sarcasm_detector.pkl
│   │   └── model_metadata.json
│   └── exports/
│       └── research_datasets/
│
├── scripts/                           # 🔧 Utility Scripts
│   ├── setup_database.py              # Database initialization
│   ├── import_data.py                 # Data import script
│   ├── train_models.py                # Model training
│   ├── evaluate_models.py             # Model evaluation
│   ├── generate_reports.py            # Report generation
│   ├── sarcasm_analysis.py            # Current script
│   ├── dual_layer_sarcasm_analysis.py # Current script
│   ├── create_readable_version.py     # Current script
│   └── utils/
│       ├── __init__.py
│       └── helpers.py
│
├── notebooks/                         # 📓 Jupyter Notebooks
│   ├── 01_data_exploration.ipynb
│   ├── 02_emotion_analysis.ipynb
│   ├── 03_sarcasm_detection.ipynb
│   ├── 04_model_training.ipynb
│   ├── 05_qualia_framework.ipynb
│   └── 06_visualization_examples.ipynb
│
├── deployment/                        # 🚀 Deployment
│   ├── Dockerfile.backend             # Backend container
│   ├── Dockerfile.frontend            # Frontend container
│   ├── docker-compose.yml             # Docker orchestration
│   ├── docker-compose.dev.yml         # Dev environment
│   ├── nginx.conf                     # Nginx config
│   └── kubernetes/                    # K8s (optional)
│       ├── backend-deployment.yml
│       ├── frontend-deployment.yml
│       └── ingress.yml
│
├── .gitignore                         # Git ignore rules
├── .env.example                       # Environment template
├── LICENSE                            # BGI Sustainability License
├── README.md                          # Main README
├── TECHNICAL_ROADMAP.md               # This roadmap
├── QUICK_START_GUIDE.md               # Quick start guide
├── CONTRIBUTING.md                    # Contribution guide
├── CODE_OF_CONDUCT.md                 # Code of conduct
└── CHANGELOG.md                       # Version history
```

---

## Migration Plan

### Phase 1: Organize Current Files
```bash
# Create directory structure
mkdir -p {frontend,backend,data,scripts,notebooks,docs,deployment}
mkdir -p data/{raw,processed,analysis,models,exports}
mkdir -p docs/{api,learning,research,design,ethics}
mkdir -p backend/{app,tests}

# Move existing files
mv "Copy of pi-user-history.json" data/raw/
mv sarcasm_analysis.py scripts/
mv dual_layer_sarcasm_analysis.py scripts/
mv create_readable_version.py scripts/
mv *.csv data/analysis/
mv src/ frontend/src/
```

### Phase 2: Initialize New Directories
```bash
# Frontend
cd frontend
npm create vite@latest . -- --template react
npm install

# Backend
cd ../backend
python3 -m venv venv
source venv/bin/activate
pip install fastapi uvicorn pandas numpy matplotlib

# Create basic structure
touch backend/app/{__init__.py,main.py,config.py}
touch backend/requirements.txt
```

### Phase 3: Create Documentation
```bash
# Learning modules
touch docs/learning/module_{01..04}_*.md

# API docs
touch docs/api/{endpoints,authentication,examples}.md

# Research docs
touch docs/research/{methodology,emotional_framework}.md
```

### Phase 4: Setup Development Tools
```bash
# Git
echo "venv/" >> .gitignore
echo "node_modules/" >> .gitignore
echo ".env" >> .gitignore
echo "*.pyc" >> .gitignore
echo "__pycache__/" >> .gitignore

# Docker
touch deployment/Dockerfile.{backend,frontend}
touch deployment/docker-compose.yml

# CI/CD
mkdir -p .github/workflows
touch .github/workflows/{ci,test,deploy}.yml
```

---

## File Naming Conventions

### Python Files
- **Scripts:** `lowercase_with_underscores.py`
- **Modules:** `lowercase_module.py`
- **Classes:** `PascalCase` in files
- **Tests:** `test_feature.py`

### JavaScript Files
- **Components:** `PascalCase.jsx`
- **Utilities:** `camelCase.js`
- **Tests:** `Feature.test.js`

### Documentation
- **Markdown:** `UPPERCASE_MAJOR.md` or `lowercase_detail.md`
- **Examples:** `README.md`, `api_reference.md`

### Data Files
- **Raw:** `original_name.json`
- **Processed:** `descriptive_name.parquet`
- **Analysis:** `analysis_type_results.csv`

---

## .gitignore Template

```gitignore
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
venv/
env/
ENV/
.venv
pip-log.txt
pip-delete-this-directory.txt
.pytest_cache/
.coverage
htmlcov/
*.egg-info/
dist/
build/

# Node.js
node_modules/
npm-debug.log*
yarn-debug.log*
yarn-error.log*
.pnpm-debug.log*
dist/
build/
.cache/

# Environment
.env
.env.local
.env.*.local

# IDEs
.vscode/
.idea/
*.swp
*.swo
*~
.DS_Store

# Data (sensitive)
data/raw/PRIVATE*
*.backup
personal_data/

# Models (large files)
data/models/*.pkl
data/models/*.h5
data/models/*.pt

# Logs
logs/
*.log

# Temporary
tmp/
temp/
*.tmp

# OS
Thumbs.db
.DS_Store
```

---

## Environment Variables Template

### Backend (.env)
```bash
# Database
DATABASE_URL=sqlite:///./data/emotions.db
# DATABASE_URL=postgresql://user:pass@localhost/emotions

# API
API_VERSION=v1
API_PREFIX=/api/v1
SECRET_KEY=your-secret-key-here
DEBUG=False

# CORS
CORS_ORIGINS=http://localhost:3000,http://localhost:5173

# ML Models
MODEL_PATH=./data/models
HUGGINGFACE_TOKEN=your-hf-token-here

# Logging
LOG_LEVEL=INFO
LOG_FILE=./logs/app.log
```

### Frontend (.env)
```bash
# API
VITE_API_URL=http://localhost:8000
VITE_WS_URL=ws://localhost:8000

# Features
VITE_ENABLE_ANALYTICS=false
VITE_ENABLE_EXPERIMENTS=true
```

---

## Dependencies

### Backend (requirements.txt)
```
# Core
fastapi==0.104.1
uvicorn[standard]==0.24.0
python-multipart==0.0.6
python-dotenv==1.0.0
pydantic==2.5.0
pydantic-settings==2.1.0

# Data Science
pandas==2.1.3
numpy==1.26.2
scipy==1.11.4

# Visualization
matplotlib==3.8.2
seaborn==0.13.0
plotly==5.18.0

# NLP & ML
transformers==4.35.2
torch==2.1.1
scikit-learn==1.3.2
nltk==3.8.1
spacy==3.7.2
emoji==2.8.0
vaderSentiment==3.3.2
textblob==0.17.1

# Database
sqlalchemy==2.0.23
alembic==1.12.1
aiosqlite==0.19.0

# Utilities
aiofiles==23.2.1
python-jose==3.3.0
passlib==1.7.4
bcrypt==4.1.1

# Testing
pytest==7.4.3
pytest-asyncio==0.21.1
pytest-cov==4.1.0
httpx==0.25.2
```

### Frontend (package.json)
```json
{
  "dependencies": {
    "react": "^18.2.0",
    "react-dom": "^18.2.0",
    "react-router-dom": "^6.20.0",
    "@mui/material": "^5.14.20",
    "@emotion/react": "^11.11.1",
    "@emotion/styled": "^11.11.0",
    "axios": "^1.6.2",
    "recharts": "^2.10.3",
    "d3": "^7.8.5",
    "plotly.js": "^2.27.1",
    "react-plotly.js": "^2.6.0"
  },
  "devDependencies": {
    "@vitejs/plugin-react": "^4.2.0",
    "vite": "^5.0.0",
    "eslint": "^8.54.0",
    "prettier": "^3.1.0",
    "@testing-library/react": "^14.1.2",
    "@testing-library/jest-dom": "^6.1.5",
    "vitest": "^1.0.4"
  }
}
```

---

## Size Estimates

### Current Repository
- Total: ~6.2MB
- JSON data: 5.4MB (2 copies)
- Analysis results: 718KB
- Scripts: 20KB
- Docs: 30KB

### Projected Size (After Development)
- Frontend build: ~2-5MB
- Backend code: ~5-10MB
- Dependencies: ~500MB (not committed)
- Models: ~100-500MB (not committed)
- Processed data: ~10-50MB
- Documentation: ~5-10MB
- **Committed Total:** ~30-80MB
- **Working Total:** ~600MB-1GB (with venv/node_modules)

---

## Maintenance Notes

### Regular Tasks
- **Weekly:** Update dependencies, review security alerts
- **Monthly:** Clean up old analysis results, backup data
- **Quarterly:** Review and archive old experiments
- **Yearly:** Major version updates, architecture review

### Backup Strategy
- **Git:** All code and documentation
- **External:** Large models and processed data
- **Cloud:** Critical analysis results
- **Local:** Development databases

---

*This structure supports scalability, maintainability, and collaborative development.*
