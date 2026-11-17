# 📘 Digital Health MoH Competency Prep

A mobile-first study app for the **Ethiopian Civil Service Commission (FCSC)** behavioral competency assessment (**Proclamation No. 1353/2025** & **Regulation No. 584/2026**), built with Streamlit. Designed specifically for public healthcare professionals, it also covers emotional intelligence in healthcare and information management systems (IMS / DHIS2).

## ✨ Features

| Tab / Control | What it does |
|---------------|--------------|
| 🎯 **Grade Filter** | Filters units & quiz pools by civil service tier (*Junior/Officer VIII–XI*, *Senior/Team Leader XII–XV*, *Director/Executive XVI+*) |
| 🏠 **Home** | Work / Human / Result pillar breakdown for your selected grade, role levels, learning domains, and 12 technical units |
| 🧩 **Units** | All 15 behavioral competencies with Amharic names, definitions, indicators, and required-tier badges |
| 📝 **Quiz & Exam** | 48 scenario-based questions across behavioral, digital health, and aptitude topics with **Practice Mode**, **⏱️ Timed Mock Exam** (60s/question), rationales, and **Pillar-by-Pillar Score Breakdown** |
| 💗 **EI** | Emotional intelligence flashcards for high-stress healthcare environments |
| 🗄️ **IMS** | Information lifecycle, system types (TPS/MIS/DSS/ERP), DHIS2/HMIS workflows, and interactive **Data Quality Index (DQI)** calculator |
| 🔎 **Find** | Instant cross-search across all units, EI cards, IMS concepts, and quiz questions |

## 📂 Project structure

```text
├── app.py            # Streamlit app (UI, grade filter, timed exam engine, DQI calculator)
├── content.py        # Competency units, Amharic titles, grade mappings, EI, and IMS content
├── data/
│   └── mcq.json      # Scenario-based MCQs with unit tags, options, answer index, and rationales
├── requirements.txt
└── README.md
```

## 🚀 Run locally

```bash
git clone https://github.com
cd digital-health-moh-competency-prep
pip install -r requirements.txt
streamlit run app.py
```

## ☁️ Deploy (free)

1. Push this repo to GitHub.
2. Go to [share.streamlit.io](https://streamlit.io) and sign in with GitHub.
3. Click **Create app**, select this repo, and set the main file to `app.py`.
4. Open the generated URL on your phone and choose **Add to Home Screen**.

*Note: Free hosting sleeps after inactivity, so the first load may take about 30 seconds.*

## 📚 Content sources

- Federal Civil Servants Proclamation No. 1353/2025 & Regulation No. 584/2026
- MoH Behavioral Competency Training deck (Amharic and English)
- Behavioral Competency in the Workplace (PDF)
- Emotional Intelligence in Healthcare Systems (Master's-level deck)
- Information Management Systems (IMS / DHIS2) deck

## ⚠️ Important notes

- **Quiz answer key is unofficial.** The source training deck does not mark correct answers, and newly added public-health scenarios reflect best-judgment civil service and clinical governance practices. Confirm with your trainer before relying on them.
- **Statistics in the IMS deck are uncited** and are not included in the app.
- This is an independent study aid, not an official Ministry of Health or Federal Civil Service Commission product.

## 🛠️ Editing content

- **Competency, EI, grade tiers, and IMS text:** Edit `content.py`.
- **Quiz questions:** Edit `data/mcq.json`. Each item has `unit`, `q`, `options` (4 items), `answer` (0-based index of the correct option), and an optional `rationale` string.

## 🗺️ Roadmap

- Amharic / English bilingual UI toggle
- Downloadable score summary report (CSV / JSON)
- Deep-dive study cards per technical unit
