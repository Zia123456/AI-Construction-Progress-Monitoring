# 🏗️ AI Construction Progress Monitoring

**Research prototype for AI-assisted construction progress monitoring using computer vision.**

This project investigates how construction-site imagery can be converted into an interpretable project-control signal:

> **Site Image → AI Construction-Stage Classification → Progress Estimate → Management Interpretation**

The prototype uses **Python, Streamlit, PyTorch, Hugging Face Transformers, and CLIP**.

## Research motivation

Construction progress is commonly assessed through site inspections, photographs, reports, schedules, and manually recorded quantities. This prototype explores a computer-vision component that could later be integrated with BIM models, schedules, site observations, and project-control records.

It is intentionally presented as a **research prototype**, not as a certified progress-measurement system.

## Features

- Upload construction-site images
- Zero-shot classification of five construction stages
- Estimated progress percentage derived from stage probabilities
- Human-readable interpretation for project-control use
- Streamlit web interface
- Docker deployment support
- Unit test for the project configuration

## Construction stages

| Stage | Representative progress |
|---|---:|
| Foundation / Excavation | 10% |
| Structural Frame | 35% |
| Envelope / Walls | 55% |
| MEP / Interior Works | 75% |
| Finishing / Completion | 95% |

The percentage is a weighted research indicator. It should **not** be interpreted as a measured percentage of completed quantities.

## Technology stack

- Python 3.11
- Streamlit
- PyTorch
- Hugging Face Transformers
- OpenAI CLIP
- Pillow
- Docker

## Run locally

```bash
git clone https://github.com/YOUR_USERNAME/ai-construction-progress-monitoring.git
cd ai-construction-progress-monitoring

python -m venv .venv

# Windows
.venv\Scripts\activate

# macOS/Linux
source .venv/bin/activate

pip install -r requirements.txt
streamlit run app.py
```

On first execution, the CLIP model is downloaded from Hugging Face and cached locally.

## Deploy with Streamlit Community Cloud

1. Create a GitHub repository named `ai-construction-progress-monitoring`.
2. Upload the project files.
3. Open Streamlit Community Cloud.
4. Create a new app.
5. Select the GitHub repository and branch.
6. Set the main file to:

```text
app.py
```

7. Deploy.

Because the vision model is downloaded on first startup, the first deployment can take longer than later runs.

## Docker

```bash
docker build -t ai-construction-progress-monitoring .
docker run -p 8501:8501 ai-construction-progress-monitoring
```

Open:

```text
http://localhost:8501
```

## Research limitations

This is a proof-of-concept. CLIP is a general-purpose vision-language model rather than a construction-specific progress model. Its stage predictions should therefore be validated against annotated construction imagery and project records before any operational use.

A stronger research version would use:

1. A project-specific annotated image dataset
2. Construction-stage labels tied to schedule activities
3. BIM element quantities
4. Planned vs. actual schedule data
5. Object detection/segmentation for structural elements
6. Temporal analysis across repeated site observations
7. Calibration and uncertainty estimation
8. Human evaluation with construction professionals

## Future architecture

```text
                 ┌──────────────────┐
                 │  Site Photographs│
                 └────────┬─────────┘
                          ↓
                 ┌──────────────────┐
                 │ Computer Vision  │
                 │ Stage / Element  │
                 │ Detection        │
                 └────────┬─────────┘
                          ↓
┌──────────────┐  ┌──────────────────┐  ┌───────────────┐
│ BIM Model    │→ │ Project Data     │ ←│ Schedule      │
└──────────────┘  │ Integration      │  └───────────────┘
                  └────────┬─────────┘
                           ↓
                  ┌──────────────────┐
                  │ Progress / Risk  │
                  │ Decision Support │
                  └────────┬─────────┘
                           ↓
                  ┌──────────────────┐
                  │ Human Manager    │
                  │ Validation       │
                  └──────────────────┘
```

## Suggested PhD-CV description

**AI Construction Progress Monitoring — Research Prototype**  
Developed a Python-based computer-vision prototype for construction-stage classification and AI-assisted progress estimation from site imagery. Implemented zero-shot vision-language inference using CLIP and translated stage probabilities into an interpretable project-control indicator through a Streamlit dashboard. Designed the prototype as a foundation for future integration of BIM, schedules, and site observations.

**Technologies:** Python · PyTorch · Transformers · CLIP · Streamlit · Computer Vision

## Academic positioning

This project supports research themes in:

- Construction Informatics
- Digital Construction
- BIM and information integration
- Computer vision for construction
- Construction project control
- AI-enabled decision support
- Human-centred AI

## License

MIT License
