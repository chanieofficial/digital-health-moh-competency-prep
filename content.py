"""Complete static content for the Ethiopian Civil Service & MoH Competency Pocket Guide."""

# ---- 1. Three-Pillar Behavioral Model (15 Units: 4 Work, 6 Human, 5 Result)
CATS = {
    "Work": "🛠️",
    "Human": "🤝",
    "Result": "🎯",
}

CAT_BLURB = {
    "Work": "Aligning daily work with policy, innovating, building markets, engaging stakeholders.",
    "Human": "Mindset, communication, teamwork, ethics, inclusion, empowerment.",
    "Result": "Citizen service, time, value, accountability, leadership.",
}

UNITS = [
    # --- WORK (4 units) ---
    (
        "Work",
        "Strategic Thinking",
        "ስትራቴጂያዊ አስተሳሰብ",
        "See the big picture, anticipate change, and tie daily clinical or public health work to long-term institutional and national goals.",
        [
            "Connects daily tasks to Health Sector Transformation Plan (HSTP) goals",
            "Anticipates service bottlenecks & scans for public health risks",
            "Plans with epidemiological evidence, not guesswork",
            "Communicates institutional strategy to align colleagues",
        ],
    ),
    (
        "Work",
        "Innovation / Creativity",
        "ፈጠራ እና አዳዲስ አሰራሮች",
        "Question existing routines, spot service gaps, and apply practical, low-cost Kaizen improvements in healthcare delivery.",
        [
            "Identifies workflow inefficiencies in wards, clinics, or offices",
            "Proposes practical, context-appropriate solutions within budget",
            "Encourages constructive feedback to refine standard operating procedures",
            "Adapts digital tools and job aids to reduce clinical or clerical errors",
        ],
    ),
    (
        "Work",
        "Building Markets / Resource Mobilization",
        "ሀብት ማሰባሰብ እና ገበያ መገንባት",
        "Identify sustainable resource opportunities, optimize public-private partnerships, and strengthen institutional capacity.",
        [
            "Maps local and partner resources to close facility supply or service gaps",
            "Supports cost-recovery and sustainable health financing initiatives",
            "Promotes institutional services clearly to build public trust and uptake",
            "Leverages community and NGO partnerships responsibly",
        ],
    ),
    (
        "Work",
        "Stakeholder Engagement",
        "ባለድርሻ አካላትን ማሳተፍ",
        "Build collaborative relationships across health bureaus, kebele leaders, Health Extension Workers, and community structures.",
        [
            "Consults internal and external stakeholders before rolling out changes",
            "Coordinates multi-sector responses during outbreaks or health campaigns",
            "Listens actively to community feedback and patient advocacy groups",
            "Maintains transparent communication with referral facilities and partners",
        ],
    ),

    # --- HUMAN (6 units) ---
    (
        "Human",
        "Growth Mindset",
        "የእድገት አስተሳሰብ",
        "Embrace continuous learning, adapt positively to civil service reforms, and treat challenges as opportunities to improve.",
        [
            "Seeks continuous professional development (CPD) and updated clinical guidelines",
            "Accepts constructive feedback from supervisors and peers without defensiveness",
            "Adapts quickly to new digital health systems (e.g., DHIS2, EMR)",
            "Helps colleagues navigate policy and organizational transitions",
        ],
    ),
    (
        "Human",
        "Communication",
        "ውጤታማ ተግባቦት",
        "Deliver clear, empathetic, two-way communication with patients, caregivers, colleagues, and leadership.",
        [
            "Explains complex medical or administrative procedures in plain, respectful language",
            "Uses active listening and teach-back methods to confirm understanding",
            "Writes concise, accurate shift handovers, reports, and official memos",
            "Adjusts communication style across diverse cultural and linguistic backgrounds",
        ],
    ),
    (
        "Human",
        "Teamwork",
        "የቡድን ስራ",
        "Collaborate across multidisciplinary cadres to deliver seamless, patient-centered public service.",
        [
            "Shares workload fairly and supports colleagues during peak clinical volume",
            "Respects the roles of nurses, physicians, pharmacists, lab staff, and support teams",
            "Resolves interpersonal friction early through constructive dialogue",
            "Contributes actively during morning huddles and quality-improvement reviews",
        ],
    ),
    (
        "Human",
        "Ethics & Integrity",
        "ስነ-ምግባር እና ታማኝነት",
        "Uphold Civil Servants Proclamation No. 1353/2025, impartiality, patient confidentiality, and zero tolerance for corruption.",
        [
            "Treats all citizens equally regardless of personal connections or status",
            "Protects patient privacy and confidential medical/personnel records",
            "Refuses gifts, bribes, or undue influence and reports misconduct properly",
            "Declares conflicts of interest transparently before making decisions",
        ],
    ),
    (
        "Human",
        "Inclusion & Diversity",
        "አካታችነት እና ብዝሃነትን ማክበር",
        "Ensure equitable, barrier-free access to health and public services for women, elders, persons with disabilities, and underserved groups.",
        [
            "Adapts service delivery for patients with visual, hearing, or mobility impairments",
            "Challenges bias and ensures respectful care across all backgrounds",
            "Advocates for gender-sensitive and youth-friendly health services",
            "Creates a psychologically safe environment where every team member is heard",
        ],
    ),
    (
        "Human",
        "Empowerment & Emotional Intelligence",
        "ማብቃት እና ስሜታዊ ብልህነት",
        "Manage emotions under high clinical stress, show empathy toward distressed citizens, and mentor junior staff.",
        [
            "Remains calm, composed, and professional when dealing with anxious or angry patients",
            "Recognizes personal stress triggers and practices healthy emotional regulation",
            "Mentors newly deployed clinicians and delegates responsibilities clearly",
            "Builds confidence in peers by recognizing strong performance",
        ],
    ),

    # --- RESULT (5 units) ---
    (
        "Result",
        "Citizen-Centered Service",
        "ዜጋ-ተኮር አገልግሎት",
        "Put patient dignity, safety, and timely access at the center of every public health interaction.",
        [
            "Greets citizens promptly and guides them clearly through triage and referral steps",
            "Handles complaints with empathy and resolves root causes rather than shifting blame",
            "Monitors waiting times and reduces unnecessary administrative hurdles",
            "Upholds the Citizen Charter standards in daily service delivery",
        ],
    ),
    (
        "Result",
        "Time Management",
        "የጊዜ አጠቃቀም",
        "Prioritize urgent tasks, respect working hours, and meet clinical and reporting deadlines reliably.",
        [
            "Arrives punctually for shifts, handovers, and scheduled outreach",
            "Triages tasks by clinical urgency and institutional impact",
            "Submits HMIS/DHIS2 and administrative reports on or before deadlines",
            "Minimizes idle delays during patient transfers and supply requests",
        ],
    ),
    (
        "Result",
        "Value for Money",
        "ወጪ ቆጣቢነት እና ውጤታማነት",
        "Protect public funds, prevent medication and supply wastage, and maximize health impact per birr spent.",
        [
            "Applies FEFO (First-Expiry, First-Out) stock rotation to prevent drug/kit expiration",
            "Maintains medical equipment properly and reports faults early",
            "Eliminates duplicate testing, unnecessary printing, and resource misuse",
            "Justifies procurement requests with accurate consumption data",
        ],
    ),
    (
        "Result",
        "Accountability",
        "ተጠያቂነት",
        "Take personal ownership of decisions, clinical outcomes, data accuracy, and regulatory compliance.",
        [
            "Documents clinical care and public records accurately without fabrication",
            "Owns mistakes promptly, corrects errors transparently, and prevents recurrence",
            "Follows national treatment protocols and civil service directives consistently",
            "Holds self and team members to measurable performance standards",
        ],
    ),
    (
        "Result",
        "Leadership",
        "አመራርነት",
        "Inspire shared vision, drive quality improvement, and guide teams through reform and high-pressure situations.",
        [
            "Sets clear expectations and models ethical civil service behavior",
            "Makes timely, evidence-based decisions during emergencies or staffing shortages",
            "Coaches team members and resolves inter-unit bottlenecks constructively",
            "Champions continuous quality improvement (Kaizen) across the facility",
        ],
    ),
]

# ---- 2. Grade-Level / Role Tier Filtering ----
LEVELS = {
    "Junior / Officer (Grades VIII–XI)": "10 core operational, ethical & citizen-service units for frontline healthcare staff.",
    "Senior / Team Leader (Grades XII–XV)": "13 units adding strategic alignment, stakeholder engagement & empowerment.",
    "Director / Executive (Grades XVI+)": "All 15 units with full emphasis on strategy, resource mobilization & leadership.",
}

GRADE_TIERS = {
    "All Levels (15 Units)": {
        "desc": "Full behavioral competency framework across all civil service tiers.",
        "units": None,
    },
    "Junior / Officer Level (Grades VIII–XI)": {
