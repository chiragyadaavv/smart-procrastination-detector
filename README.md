# Smart Procrastination Detector

A privacy-aware Python productivity analytics system for an MCA group project. The goal is to analyze opt-in computer-activity metadata, summarize distraction patterns, calculate transparent productivity metrics, and investigate personalized procrastination-risk predictions.

> **Project status:** Early development. Features in the roadmap are planned, not yet implemented unless explicitly marked otherwise.

## Goals
- Track explicitly started study/work sessions.
- Summarize productive, distracting, and idle time using user-approved categories.
- Calculate an explainable productivity score from 0–100.
- Establish a rule-based baseline before evaluating machine-learning models.
- Explore future procrastination-risk prediction using historical, labeled sessions.
- Recommend focus and break durations based on a user's own history.
- Present insights in a Streamlit dashboard.

## Planned stack
- Python 3.12
- Pandas, NumPy
- psutil and platform-specific foreground-window APIs where supported
- scikit-learn
- SQLite and SQLAlchemy
- Streamlit and Plotly
- pytest

## Planned architecture
```text
Opt-in session
  -> Activity tracker
  -> Privacy-safe event metadata
  -> Feature extraction
  -> Productivity analytics
  -> Rule-based baseline / ML evaluation
  -> Personalized recommendations
  -> SQLite
  -> Streamlit dashboard
```

## Project structure
```text
app/
  tracker/          # Foreground-app and idle-time metadata
  analytics/        # Metrics and feature extraction
  ml/               # Training, evaluation, and inference
  recommendations/  # Focus and break suggestions
  database/         # SQLite schema and data access
  dashboard/        # Streamlit interface
data/
  raw/              # Local-only activity data; never commit it
  processed/        # Local-only derived data
models/             # Locally generated model files
tests/
docs/
main.py
requirements.txt
```

## Setup on Windows (PowerShell)
Install Python 3.12, then run:

```powershell
py -3.12 -m venv venv
.\venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python main.py
```

## Privacy by design
- Tracking must be opt-in, visible, and easy to pause or stop.
- Do not collect raw keystrokes, passwords, private messages, clipboard contents, or document text.
- Prefer application categories over full URLs or detailed browsing histories.
- Keep databases, personal activity logs, and trained model files out of Git.
- Plan controls for reviewing and deleting local data.

## ML and research integrity
Future-risk prediction requires timestamped historical sessions and a documented labeling protocol. Synthetic data can test the pipeline, but it cannot establish real-world predictive performance. Compare a rule-based baseline with Logistic Regression, Random Forest, and Gradient Boosting; evaluate using held-out sessions or time periods and report precision, recall, F1, confusion matrix, class balance, and limitations. Do not claim accuracy before testing.

## Roadmap
1. Project foundation and configuration
2. SQLite schema and session management
3. Opt-in activity tracker with privacy safeguards
4. Productivity metrics and transparent scoring
5. Rule-based baseline and user feedback
6. Dataset preparation and ML evaluation
7. Future-risk experiment and recommendations
8. Streamlit dashboard and reports
9. Tests, documentation, MCA presentation, and viva preparation

## Team roles
- **Data/ML developer:** tracking, feature engineering, scoring, ML experiments, recommendation logic.
- **Application developer:** database, session controls, dashboard, visualizations, reports, integration.
- Both team members: privacy review, testing, research methodology, and final documentation.

## License
A license has not been selected yet. Add one before encouraging reuse or redistribution.
