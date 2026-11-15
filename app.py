streamlit>=1.40
import json, random, pathlib
import streamlit as st
from content import *

st.set_page_config(page_title="Competency Pocket Guide", page_icon="📘", layout="centered",
                   initial_sidebar_state="collapsed")

st.markdown("""
<style>
.block-container{padding:1rem .8rem 4rem;max-width:640px}
.stButton>button,.stDownloadButton>button{width:100%;min-height:3rem;border-radius:12px;font-weight:600}
.stTabs [data-baseweb="tab-list"]{gap:2px;overflow-x:auto}
.stTabs [data-baseweb="tab"]{padding:.6rem .7rem;font-size:.95rem}
.card{border:1px solid rgba(128,128,128,.25);border-radius:14px;padding:.9rem 1rem;margin:.5rem 0}
.am{opacity:.75;font-size:.9rem}
.pill{display:inline-block;padding:.1rem .6rem;border-radius:99px;background:rgba(20,150,130,.15);font-size:.8rem}
#MainMenu,footer{visibility:hidden}
</style>""", unsafe_allow_html=True)

MCQ = json.loads((pathlib.Path(__file__).parent/"data"/"mcq.json").read_text(encoding="utf-8"))
st.title("📘 Competency Pocket Guide")
st.caption("Behavioral competency · Emotional intelligence · Information systems")

t_home, t_comp, t_quiz, t_ei, t_ims, t_find = st.tabs(["🏠 Home","🧩 Units","📝 Quiz","💗 EI","🗄️ IMS","🔎 Find"])

# ---------------- HOME
with t_home:
    st.subheader("Three-pillar model")
    for c, e in CATS.items():
        n = sum(1 for u in UNITS if u[0]==c)
        st.markdown(f"<div class='card'><b>{e} {c}</b> <span class='pill'>{n} units</span><br>{CAT_BLURB[c]}</div>", unsafe_allow_html=True)
    st.subheader("Who needs how many?")
    for k, v in LEVELS.items():
        st.markdown(f"**{k}**: {v}")
    st.subheader("Learning domains")
    for n, d, lv in DOMAINS:
        with st.expander(n):
            st.write(d); st.caption(lv)
    with st.expander("12 technical units"):
        st.write(" · ".join(TECH_UNITS))
    st.info("Behavioral assessment is case-based: it tests what you'd *do*, not what you can recite.")

# ---------------- UNITS
with t_comp:
    cat = st.radio("Category", ["All", *CATS], horizontal=True, label_visibility="collapsed")
    for c, name, am, desc, ind in UNITS:
        if cat != "All" and c != cat: continue
        with st.expander(f"{CATS[c]} {name}"):
            st.markdown(f"<div class='am'>{am}</div>", unsafe_allow_html=True)
            st.write(desc)
            st.markdown("**Indicators**")
            for i in ind: st.markdown(f"- {i}")

# ---------------- QUIZ
with t_quiz:
    units = sorted({q["unit"] for q in MCQ})
    S = st.session_state
    if "qz" not in S: S.qz = None
    if S.qz is None:
        pick = st.selectbox("Topic", ["All topics", *units])
        n = st.slider("Questions", 3, len(MCQ), min(8, len(MCQ)))
        if st.button("Start quiz ▶"):
            pool = [q for q in MCQ if pick == "All topics" or q["unit"] == pick]
            random.shuffle(pool)
            qs = []
            for q in pool[:n]:
                order = list(range(4)); random.shuffle(order)
                qs.append({**q, "order": order})
            S.qz = {"qs": qs, "i": 0, "score": 0, "done": False, "ans": None, "log": []}
            st.rerun()
        st.caption("Answer key isn't in the source deck, so the 'correct' options are best-judgment picks. Verify with your trainer.")
    else:
        z = S.qz
        if z["i"] >= len(z["qs"]):
            st.success(f"Score: {z['score']} / {len(z['qs'])}")
            for u, ok in z["log"]:
                st.write(("✅ " if ok else "❌ ") + u)
            if st.button("New quiz", key="qz_new"): S.qz = None; st.rerun()
        else:
            q = z["qs"][z["i"]]
            st.progress(z["i"]/len(z["qs"]), text=f"Q{z['i']+1} of {len(z['qs'])} · {q['unit']}")
            st.markdown(f"**{q['q']}**")
            labels = [q["options"][k] for k in q["order"]]
            if z["ans"] is None:
                for pos, k in enumerate(q["order"]):
                    if st.button(labels[pos], key=f"o{z['i']}_{pos}"):
                        ok = k == q["answer"]
                        z["ans"] = (pos, ok); z["score"] += ok
                        z["log"].append((q["unit"], ok)); st.rerun()
            else:
                pos, ok = z["ans"]
                (st.success if ok else st.error)("Correct" if ok else "Not quite")
                st.markdown(f"**Best answer:** {q['options'][q['answer']]}")
                if st.button("Next ▶", key="qz_next"):
                    z["i"] += 1; z["ans"] = None; st.rerun()
            if st.button("Quit quiz", key="qz_quit"): S.qz = None; st.rerun()

# ---------------- EI
with t_ei:
    if "ei" not in st.session_state: st.session_state.ei = 0
    i = st.session_state.ei
    title, body = EI[i]
    st.progress((i+1)/len(EI), text=f"{i+1} / {len(EI)}")
    st.markdown(f"<div class='card'><h4>{title}</h4>{body}</div>", unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    if c1.button("◀ Back", key="ei_back", disabled=i==0): st.session_state.ei -= 1; st.rerun()
    if c2.button("Next ▶", key="ei_next", disabled=i==len(EI)-1): st.session_state.ei += 1; st.rerun()
    with st.expander("Links to the behavioral framework"):
        st.write("EI is one of the 15 behavioral units: self-control under stress, empathy in public interactions, composure with angry citizens.")

# ---------------- IMS
with t_ims:
    st.subheader("What it is")
    st.write("A structured framework of hardware, software and procedures that **captures, stores, processes and distributes** information for decision-making.")
    st.subheader("Lifecycle")
    for k, (a, b) in enumerate(IMS_LIFECYCLE, 1):
        st.markdown(f"**{k}. {a}**: {b}")
    st.subheader("Pillars")
    for a, b in IMS_PILLARS: st.markdown(f"<div class='card'><b>{a}</b><br>{b}</div>", unsafe_allow_html=True)
    st.subheader("System types")
    st.dataframe([{"System":a,"User":b,"Output":c,"Scope":d} for a,b,c,d in IMS_TYPES], hide_index=True, width="stretch")
    st.subheader("Data Quality Index")
    st.caption("DQI = (Accuracy + Completeness + Validity + Timeliness) / 4")
    sc = [st.slider(n, 0, 100, 80) for n in ("Accuracy","Completeness","Validity","Timeliness")]
    dqi = sum(sc)/4
    st.metric("DQI", f"{dqi:.1f} / 100", delta="meets 95% target" if dqi >= 95 else f"{95-dqi:.1f} below 95% target", delta_color="normal" if dqi >= 95 else "inverse")
    st.subheader("Trends")
    for a, b in IMS_TRENDS: st.markdown(f"- **{a}**: {b}")

# ---------------- FIND
with t_find:
    q = st.text_input("Search units, EI, IMS, questions", placeholder="e.g. conflict, ERP, accountability")
    if q:
        ql = q.lower(); hits = 0
        for c, name, am, desc, ind in UNITS:
            if ql in " ".join([name, am, desc, *ind]).lower():
                st.markdown(f"**{CATS[c]} {name}**: {desc}"); hits += 1
        for t, b in EI:
            if ql in (t+b).lower(): st.markdown(f"**💗 {t}**: {b}"); hits += 1
        for a, b in IMS_LIFECYCLE + IMS_PILLARS + IMS_TRENDS:
            if ql in (a+b).lower(): st.markdown(f"**🗄️ {a}**: {b}"); hits += 1
        for m in MCQ:
            if ql in (m["q"]+" ".join(m["options"])).lower():
                st.markdown(f"**📝 {m['unit']}**: {m['q'][:140]}…"); hits += 1
        if not hits: st.write("Nothing. Try a shorter word.")
          
