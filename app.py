import json
import random
import pathlib
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

st.title("📘 Competency Pocket Guide")
st.caption("Behavioral competency · Emotional intelligence · Information systems")

# Global Grade / Role Tier Selector
tier_names = list(GRADE_TIERS.keys()) if "GRADE_TIERS" in globals() else ["All Levels (15 Units)"]
selected_tier = st.selectbox("🎯 Your Civil Service Grade / Role", tier_names, key="grade_tier")
tier_info = GRADE_TIERS.get(selected_tier, {"desc": "", "units": None}) if "GRADE_TIERS" in globals() else {"desc": "", "units": None}
allowed_units = set(tier_info["units"]) if tier_info["units"] else {u[1] for u in UNITS}

if tier_info["desc"]:
    st.caption(f"{tier_info['desc']} ({len(allowed_units)} required units)")

t_home, t_comp, t_quiz, t_ei, t_ims, t_find = st.tabs(
    ["🏠 Home", "🧩 Units", "📝 Quiz", "💗 EI", "🗄️ IMS", "🔎 Find"]
)

# ---------------- HOME
with t_home:
    st.subheader("Three-pillar model")
    for c, e in CATS.items():
        total_n = sum(1 for u in UNITS if u[0] == c)
        req_n = sum(1 for u in UNITS if u[0] == c and u[1] in allowed_units)
        badge = f"{req_n}/{total_n} units for your tier" if req_n != total_n else f"{total_n} units"
        st.markdown(
            f"<div class='card'><b>{e} {c}</b> <span class='pill'>{badge}</span><br>{CAT_BLURB[c]}</div>",
            unsafe_allow_html=True,
        )
    st.subheader("Who needs how many?")
    for k, v in LEVELS.items():
        st.markdown(f"**{k}**: {v}")
    st.subheader("Learning domains")
    for n, d, lv in DOMAINS:
        with st.expander(n):
            st.write(d)
            st.caption(lv)
    with st.expander("12 technical units"):
        st.write(" · ".join(TECH_UNITS))
    st.info("Behavioral assessment is case-based: it tests what you'd *do*, not what you can recite.")

# ---------------- UNITS
with t_comp:
    cat = st.radio("Category", ["All", *CATS], horizontal=True, label_visibility="collapsed")
    only_my_tier = st.toggle("Show only units required for my selected grade", value=True)
    shown = 0
    for c, name, am, desc, ind in UNITS:
        if cat != "All" and c != cat:
            continue
        if only_my_tier and name not in allowed_units:
            continue
        shown += 1
        req_tag = " · ⭐ Required" if name in allowed_units and len(allowed_units) < len(UNITS) else ""
        with st.expander(f"{CATS[c]} {name}{req_tag}"):
            st.markdown(f"<div class='am'>{am}</div>", unsafe_allow_html=True)
            st.write(desc)
            st.markdown("**Indicators**")
            for i in ind:
                st.markdown(f"- {i}")
    if not shown:
        st.info("No units match this category for your selected grade tier. Toggle off the grade filter to view all.")

# ---------------- QUIZ & TIMED MOCK EXAM
with t_quiz:
    S = st.session_state
    if "qz" not in S:
        S.qz = None

    if S.qz is None:
        mode = st.radio("Mode", ["Practice Quiz", "⏱️ Timed Mock Exam"], horizontal=True)
        filter_by_tier = st.checkbox("Filter questions to my selected civil service grade", value=True)

        base_pool = [
            q for q in MCQ
            if not filter_by_tier or q["unit"] in allowed_units or q["unit"] not in UNIT_TO_CAT
        ]
        if not base_pool:
            base_pool = MCQ

        units = sorted({q["unit"] for q in base_pool})
        pick = st.selectbox("Topic", ["All topics", *units])
        pool_preview = [q for q in base_pool if pick == "All topics" or q["unit"] == pick]

        max_q = max(1, len(pool_preview))
        default_q = min(15 if "Timed" in mode else 8, max_q)
        n = st.slider("Questions", 1, max_q, default_q) if max_q > 1 else 1

        mins_per_q = 1.0
        total_mins = int(max(1, round(n * mins_per_q)))
        if "Timed" in mode:
            st.info(
                f"⏱️ Exam Simulation: **{n} questions** in **{total_mins} minutes** (60 sec/question). "
                "Unanswered questions auto-submit when time runs out."
            )

        if st.button("Start ▶"):
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
                "timed": "Timed" in mode,
                "deadline": time.time() + (total_mins * 60) if "Timed" in mode else None,
            }
            st.rerun()
        st.caption("Tip: Add a 'rationale' field to items in data/mcq.json to display detailed explanations after each answer.")
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
                    f"<div class='timer-box'>⏱️ Time Remaining: {mins:02d}:{secs:02d}</div>",
                    unsafe_allow_html=True,
                )

        if z["i"] >= len(z["qs"]) or time_expired:
            if time_expired and z["i"] < len(z["qs"]):
                st.warning("⏰ Time is up! Your exam has been submitted.")
                for rem_q in z["qs"][z["i"]:]:
                    z["log"].append((rem_q["unit"], False))
                z["i"] = len(z["qs"])

            total = len(z["qs"])
            pct = (z["score"] / total * 100) if total else 0
            st.success(f"Final Score: {z['score']} / {total} ({pct:.0f}%)")

            # Pillar-by-pillar breakdown
            st.subheader("📊 Score by Competency Pillar")
            pillar_stats = {c: [0, 0] for c in CATS}  # [correct, total]
            other_stats = [0, 0]
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
                cols[idx].metric(f"{emoji} {c}", val)

            if other_stats[1] > 0:
                st.caption(f"Other / Technical topics: {other_stats[0]}/{other_stats[1]}")

            with st.expander("Question-by-question review", expanded=True):
                for idx, (u, ok) in enumerate(z["log"], 1):
                    st.write(f"{'✅' if ok else '❌'} **Q{idx}** · {u}")

            if st.button("New quiz / exam", key="qz_new"):
                S.qz = None
                st.rerun()
        else:
            q = z["qs"][z["i"]]
            pillar_badge = (
                f" · {CATS[UNIT_TO_CAT[q['unit']]]} {UNIT_TO_CAT[q['unit']]}"
                if q["unit"] in UNIT_TO_CAT
                else ""
            )
            st.progress(z["i"] / len(z["qs"]), text=f"Q{z['i']+1} of {len(z['qs'])} · {q['unit']}{pillar_badge}")
            st.markdown(f"**{q['q']}**")
            labels = [q["options"][k] for k in q["order"]]

            if z["ans"] is None:
                for pos, k in enumerate(q["order"]):
                    if st.button(labels[pos], key=f"o{z['i']}_{pos}"):
                        ok = k == q["answer"]
                        z["ans"] = (pos, ok)
                        z["score"] += int(ok)
                        z["log"].append((q["unit"], ok))
                        st.rerun()
            else:
                pos, ok = z["ans"]
                (st.success if ok else st.error)("Correct!" if ok else "Not quite")
                st.markdown(f"**Best answer:** {q['options'][q['answer']]}")
                if q.get("rationale"):
                    st.info(f"💡 **Why:** {q['rationale']}")
                if st.button("Next ▶", key="qz_next"):
                    z["i"] += 1
                    z["ans"] = None
                    st.rerun()

            if st.button("Quit", key="qz_quit"):
                S.qz = None
                st.rerun()

# ---------------- EI
with t_ei:
    if "ei" not in st.session_state:
        st.session_state.ei = 0
    i = st.session_state.ei
    title, body = EI[i]
    st.progress((i + 1) / len(EI), text=f"{i+1} / {len(EI)}")
    st.markdown(f"<div class='card'><h4>{title}</h4>{body}</div>", unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    if c1.button("◀ Back", key="ei_back", disabled=i == 0):
