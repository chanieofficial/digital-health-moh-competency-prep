import csv
import datetime
import io
import json
import pathlib
import random
import time
import streamlit as st
from content import *

st.set_page_config(
    page_title="Competency Pocket Guide",
    page_icon="📘",
    layout="centered",
    initial_sidebar_state="collapsed",
)

st.markdown("""
<style>
.block-container{padding:1rem .8rem 4rem;max-width:640px}
.stButton>button,.stDownloadButton>button{width:100%;min-height:3rem;border-radius:12px;font-weight:600}
.stTabs [data-baseweb="tab-list"]{gap:2px;overflow-x:auto}
.stTabs [data-baseweb="tab"]{padding:.6rem .7rem;font-size:.95rem}
.card{border:1px solid rgba(128,128,128,.25);border-radius:14px;padding:.9rem 1rem;margin:.5rem 0}
.timer-box{border:1px solid rgba(220,53,69,.4);background:rgba(220,53,69,.08);border-radius:10px;padding:.45rem .8rem;text-align:center;font-weight:700;margin-bottom:.6rem}
.am{opacity:.75;font-size:.9rem}
.pill{display:inline-block;padding:.1rem .6rem;border-radius:99px;background:rgba(20,150,130,.15);font-size:.8rem}
#MainMenu,footer{visibility:hidden}
</style>""", unsafe_allow_html=True)

MCQ = json.loads((pathlib.Path(__file__).parent / "data" / "mcq.json").read_text(encoding="utf-8"))
UNIT_TO_CAT = {u[1]: u[0] for u in UNITS}

# Bilingual Helper
lang = st.radio("🌐 Language / ቋንቋ", ["English", "አማርኛ (Amharic)"], horizontal=True)
IS_AM = lang.startswith("አማርኛ")

def T(en, am):
    return am if IS_AM else en

CATS_AM = {"Work": "ስራ (Work)", "Human": "ሰው (Human)", "Result": "ውጤት (Result)"}

st.title(T("📘 Competency Pocket Guide", "📘 የብቃት ምዘና መመሪያ"))
st.caption(T(
    "Behavioral competency · Emotional intelligence · Information systems",
    "የባህሪ ብቃት · ስሜታዊ ብልህነት · የመረጃ አስተዳደር ስርዓቶች"
))

# Global Grade / Role Tier Selector
tier_names = list(GRADE_TIERS.keys()) if "GRADE_TIERS" in globals() else ["All Levels (15 Units)"]
selected_tier = st.selectbox(
    T("🎯 Your Civil Service Grade / Role", "🎯 የሲቪል ሰርቪስ ደረጃ / የስራ ድርሻ"),
    tier_names,
    key="grade_tier",
)
tier_info = GRADE_TIERS.get(selected_tier, {"desc": "", "units": None}) if "GRADE_TIERS" in globals() else {"desc": "", "units": None}
allowed_units = set(tier_info["units"]) if tier_info["units"] else {u[1] for u in UNITS}

if tier_info["desc"]:
    st.caption(f"{tier_info['desc']} ({len(allowed_units)} {T('required units', 'የሚፈለጉ ምዕራፎች')})")

t_home, t_comp, t_quiz, t_ei, t_ims, t_find = st.tabs([
    T("🏠 Home", "🏠 መነሻ"),
    T("🧩 Units", "🧩 ምዕራፎች"),
    T("📝 Quiz", "📝 ፈተና"),
    T("💗 EI", "💗 ስሜታዊ ብልህነት"),
    T("🗄️ IMS", "🗄️ መረጃ ስርዓት"),
    T("🔎 Find", "🔎 ፈልግ"),
])

# ---------------- HOME
with t_home:
    st.subheader(T("Three-pillar model", "የሶስት ምሰሶዎች ሞዴል"))
    for c, e in CATS.items():
        total_n = sum(1 for u in UNITS if u[0] == c)
        req_n = sum(1 for u in UNITS if u[0] == c and u[1] in allowed_units)
        unit_word = T("units", "ምዕራፎች")
        badge = f"{req_n}/{total_n} {unit_word}" if req_n != total_n else f"{total_n} {unit_word}"
        cat_label = CATS_AM[c] if IS_AM else c
        st.markdown(
            f"<div class='card'><b>{e} {cat_label}</b> <span class='pill'>{badge}</span><br>{CAT_BLURB[c]}</div>",
            unsafe_allow_html=True,
        )
    st.subheader(T("Who needs how many?", "ለየትኛው ደረጃ ስንት ምዕራፍ ያስፈልጋል?"))
    for k, v in LEVELS.items():
        st.markdown(f"**{k}**: {v}")
    st.subheader(T("Learning domains", "የትምህርት ዘርፎች"))
    for n, d, lv in DOMAINS:
        with st.expander(n):
            st.write(d)
            st.caption(lv)
    with st.expander(T("12 technical units", "12 የቴክኒክ ምዕራፎች")):
        st.write(" · ".join(TECH_UNITS))
    st.info(T(
        "Behavioral assessment is case-based: it tests what you'd *do*, not what you can recite.",
        "የባህሪ ብቃት ምዘና በተግባራዊ ሁኔታዎች ላይ የተመሰረተ ነው፡ የሚፈትነው በተግባር ምን እንደሚያደርጉ እንጂ ቃል በቃል የሚያስታውሱትን አይደለም።"
    ))

# ---------------- UNITS
with t_comp:
    cat = st.radio("Category", ["All", *CATS], horizontal=True, label_visibility="collapsed")
    only_my_tier = st.toggle(
        T("Show only units required for my selected grade", "ለተመረጠው የስራ ደረጃ የሚፈለጉ ምዕራፎችን ብቻ አሳይ"),
        value=True,
    )
    shown = 0
    for c, name, am, desc, ind in UNITS:
        if cat != "All" and c != cat:
            continue
        if only_my_tier and name not in allowed_units:
            continue
        shown += 1
        req_tag = f" · ⭐ {T('Required', 'የሚፈለግ')}" if name in allowed_units and len(allowed_units) < len(UNITS) else ""
        header_title = f"{CATS[c]} {am} ({name}){req_tag}" if IS_AM else f"{CATS[c]} {name}{req_tag}"
        with st.expander(header_title):
            st.markdown(f"<div class='am'>{name if IS_AM else am}</div>", unsafe_allow_html=True)
            st.write(desc)
            st.markdown(f"**{T('Indicators', 'መለኪያ አመልካቾች')}**")
            for i in ind:
                st.markdown(f"- {i}")
    if not shown:
        st.info(T(
            "No units match this category for your selected grade tier. Toggle off the grade filter to view all.",
            "ለተመረጠው የስራ ደረጃ በዚህ ምድብ ምዕራፍ የለም። ሁሉንም ለማየት ማጣሪያውን ያጥፉ።"
        ))

# ---------------- QUIZ & TIMED MOCK EXAM
with t_quiz:
    S = st.session_state
    if "qz" not in S:
        S.qz = None

    if S.qz is None:
        mode = st.radio(
            T("Mode", "የፈተና አይነት"),
            [T("Practice Quiz", "ልምምድ"), T("⏱️ Timed Mock Exam", "⏱️ በሰዓት የተገደበ ሙከራ")],
            horizontal=True,
        )
        is_timed = "Timed" in mode or "በሰዓት" in mode
        filter_by_tier = st.checkbox(
            T("Filter questions to my selected civil service grade", "ጥያቄዎችን በተመረጠው የስራ ደረጃ አጣራ"),
            value=True,
        )

        base_pool = [
            q for q in MCQ
            if not filter_by_tier or q["unit"] in allowed_units or q["unit"] not in UNIT_TO_CAT
        ]
        if not base_pool:
            base_pool = MCQ

        units = sorted({q["unit"] for q in base_pool})
        all_label = T("All topics", "ሁሉም ርዕሶች")
        pick = st.selectbox(T("Topic", "ርዕስ"), [all_label, *units])
        pool_preview = [q for q in base_pool if pick == all_label or q["unit"] == pick]

        max_q = max(1, len(pool_preview))
        default_q = min(15 if is_timed else 8, max_q)
        n = st.slider(T("Questions", "የጥያቄ ብዛት"), 1, max_q, default_q) if max_q > 1 else 1

        mins_per_q = 1.0
        total_mins = int(max(1, round(n * mins_per_q)))
        if is_timed:
            st.info(T(
                f"⏱️ Exam Simulation: **{n} questions** in **{total_mins} minutes** (60 sec/question). Unanswered questions auto-submit when time runs out.",
                f"⏱️ የፈተና ልምምድ፡ **{n} ጥያቄዎች** በ **{total_mins} ደቂቃ** ውስጥ። ሰዓቱ ሲያልቅ ፈተናው በራሱ ይጠናቀቃል።"
            ))

        if st.button(T("Start ▶", "ጀምር ▶")):
            pool = list(pool_preview)
            random.shuffle(pool)
            qs = []
            for q in pool[:n]:
                order = list(range(len(q["options"])))
                random.shuffle(order)
                qs.append({**q, "order": order})
            S.qz = {
                "qs": qs,
                "i": 0,
                "score": 0,
                "ans": None,
                "log": [],
                "timed": is_timed,
                "deadline": time.time() + (total_mins * 60) if is_timed else None,
            }
            st.rerun()
        st.caption(T(
            "Tip: Add a 'rationale' field to items in data/mcq.json to display detailed explanations after each answer.",
            "ማሳሰቢያ፡ መልሶቹ ለምርምር እና ለልምምድ የተዘጋጁ ናቸው።"
        ))
    else:
        z = S.qz
        time_expired = False
        if z["timed"] and z["deadline"] is not None:
            rem = int(z["deadline"] - time.time())
            if rem <= 0:
                time_expired = True
            else:
                mins, secs = divmod(rem, 60)
                st.markdown(
                    f"<div class='timer-box'>⏱️ {T('Time Remaining', 'የቀረው ሰዓት')}: {mins:02d}:{secs:02d}</div>",
                    unsafe_allow_html=True,
                )

        if z["i"] >= len(z["qs"]) or time_expired:
            if time_expired and z["i"] < len(z["qs"]):
                st.warning(T("⏰ Time is up! Your exam has been submitted.", "⏰ ሰዓቱ አልቋል! ፈተናዎ ተጠናቋል።"))
                for rem_q in z["qs"][z["i"]:]:
                    z["log"].append((rem_q["unit"], False))
                z["i"] = len(z["qs"])

            total = len(z["qs"])
            pct = (z["score"] / total * 100) if total else 0
            st.success(f"{T('Final Score', 'አጠቃላይ ውጤት')}: {z['score']} / {total} ({pct:.0f}%)")

            # Pillar-by-pillar breakdown
            st.subheader(T("📊 Score by Competency Pillar", "📊 ውጤት በብቃት ምሰሶዎች"))
            pillar_stats = {c: list((0, 0)) for c in CATS}
            other_stats = list((0, 0))
            for u, ok in z["log"]:
                cat_name = UNIT_TO_CAT.get(u)
                if cat_name in pillar_stats:
                    pillar_stats[cat_name][1] += 1
                    if ok:
                        pillar_stats[cat_name][0] += 1
                else:
                    other_stats[1] += 1
                    if ok:
                        other_stats[0] += 1

            cols = st.columns(len(CATS))
            for idx, (c, emoji) in enumerate(CATS.items()):
                corr, tot = pillar_stats[c]
                val = f"{corr}/{tot}" if tot else "—"
                label = CATS_AM[c] if IS_AM else c
                cols[idx].metric(f"{emoji} {label}", val)

            if other_stats[1] > 0:
                st.caption(f"{T('Other / Technical topics', 'ሌሎች / ቴክኒካል ርዕሶች')}: {other_stats[0]}/{other_stats[1]}")

            with st.expander(T("Question-by-question review", "የጥያቄዎች ዝርዝር ግምገማ"), expanded=True):
                for idx, (u, ok) in enumerate(z["log"], 1):
                    st.write(f"{'✅' if ok else '❌'} **Q{idx}** · {u}")

            # Downloadable CSV Score Report
