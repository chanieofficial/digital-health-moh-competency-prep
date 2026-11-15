# Digital Health MoH Competency Prep

A mobile-first study app for Ethiopian civil service behavioral competency assessment, built with Streamlit. It also covers emotional intelligence in healthcare and information management systems.

## Features

| Tab | What it does |
|-----|--------------|
| 🏠 Home | Work / Human / Result model, role levels, learning domains, technical units |
| 🧩 Units | All 15 behavioral competencies with Amharic names, definitions and indicators |
| 📝 Quiz | 18 scenario-based questions, shuffled, scored, filterable by topic |
| 💗 EI | Emotional intelligence cards for healthcare (Salovey & Mayer, Goleman) |
| 🗄️ IMS | Information lifecycle, system types (TPS/MIS/DSS/ERP), Data Quality Index calculator |
| 🔎 Find | Search across all content |

## Project structure

```
├── app.py            # Streamlit app (UI and logic)
├── content.py        # Competency, EI and IMS content
├── data/
│   └── mcq.json      # Quiz questions
├── requirements.txt
└── README.md
```

## Run locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Deploy (free)

1. Push this repo to GitHub.
2. Go to [share.streamlit.io](https://share.streamlit.io) and sign in with GitHub.
3. Click **Create app**, select this repo, and set the main file to `app.py`.
4. Open the generated URL on your phone and choose **Add to Home Screen**.

Free hosting sleeps after inactivity, so the first load may take about 30 seconds.

## Content sources

- MoH Behavioral Competency Training deck (Amharic and English)
- Behavioral Competency in the Workplace (PDF)
- Emotional Intelligence in Healthcare Systems (Master's-level deck)
- Information Management Systems deck

## Important notes

- **Quiz answer key is unofficial.** The source training deck does not mark correct answers. The "best answer" for each question is a best-judgment pick. Confirm with your trainer before relying on it.
- **Statistics in the IMS deck are uncited** and are not included in the app.
- This is an independent study aid, not an official Ministry of Health product.

## Editing content

- Competency, EI and IMS text: edit `content.py`.
- Quiz questions: edit `data/mcq.json`. Each item has `unit`, `q`, `options` (4 items), and `answer` (0-based index of the correct option).

## Roadmap

- Deep-dive page per competency unit
- Amharic UI toggle
- Score history across sessions
