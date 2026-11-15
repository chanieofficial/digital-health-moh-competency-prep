"""Static content pulled from the four uploaded files."""

# ---- MoH deck + Behavioral Competency PDF: 15 behavioral units, 3 categories
CATS = {"Work": "🛠️", "Human": "🤝", "Result": "🎯"}
CAT_BLURB = {
 "Work": "Aligning daily work with policy, innovating, building markets, engaging stakeholders.",
 "Human": "Mindset, communication, teamwork, ethics, inclusion, empowerment.",
 "Result": "Citizen service, time, value, accountability, leadership.",
}
UNITS = [
 ("Work","Strategic Thinking","ስትራቴጂያዊ አስተሳሰብ",
  "See the big picture, anticipate change, and tie daily work to long-term institutional and national goals.",
  ["Connects daily tasks to long-term goals","Anticipates change & scans for risk","Plans with evidence, not guesswork","Communicates strategy to influence others"]),
 ("Work","Innovation / Creativity","ፈጠራ",
  "Question existing ways, spot gaps, and apply new ideas in a practical, context-appropriate way.",
  ["Identifies process inefficiencies","Proposes & tests new approaches","Open to change","Recognizes others' ideas"]),
 ("Work","Market Building","የገበያ ግንባታ",
  "Understand and shape markets to serve public goals, with impartiality and accountability.",
  ["Spots market opportunities & barriers","Matches supply and demand","Encourages private-sector participation","Supports productivity and growth"]),
 ("Work","Stakeholder Leadership","የባለሚና አመራር",
  "Identify, engage and influence diverse stakeholders to deliver shared public outcomes.",
  ["Identifies all relevant stakeholders","Analyzes interests & influence","Builds partnerships","Involves stakeholders in decisions"]),
 ("Human","Communication & Influencing","ተግባቦትና ተጽዕኖ መፍጠር",
  "Clear, timely exchange of information, active listening, constructive feedback.",
  ["Listens actively","Organizes ideas verbally & in writing","Gives constructive feedback","Positively influences outcomes"]),
 ("Human","Teamwork","የቡድን ሥራ",
  "Collaborate across differences, share accountability, resolve conflict, develop colleagues.",
  ["Collaborates across differences","Resolves conflict constructively","Supports colleagues","Shared goals over individual interest"]),
 ("Human","Emotional Intelligence","ራህሮታዊ ብስለት",
  "Recognize, understand and manage your own emotions and those of others under pressure.",
  ["Self-control in stress","Empathy in public interactions","Responds sensitively to feedback","Stays composed"]),
 ("Human","Ethics & Role Modeling","ሥነ-ምግባርና ተምሳሌትነት",
  "Integrity, impartiality, transparency, and leading by example.",
  ["Personal integrity","Follows rules, reports concerns","Promotes ethical culture","Guides teams through dilemmas"]),
 ("Human","Diversity & Inclusion","ብዝሀነትና አካታችነት",
  "Embrace differences without discrimination; ensure equal rights and fair treatment.",
  ["Respect in interactions","Treats all fairly","Challenges discrimination","Builds inclusive culture"]),
 ("Human","Competence & Motivation","መብቃትና መነሳሳት",
  "Inspire and enable others: delegate, coach, recognize, build capability.",
  ["Identifies capability gaps","Coaches & mentors","Shares knowledge","Aligns motivation with mission"]),
 ("Result","Servanthood","አገልጋይነት",
  "Citizen-centered delivery; proactively meet needs of citizens, stakeholders and colleagues.",
  ["Understands client needs","Timely, accurate information","Applies service standards","Resolves issues"]),
 ("Result","Time Management","የጊዜ አጠቃቀም",
  "Prioritize, allocate resources and structure work to meet deadlines.",
  ["High-priority work on time","Plans realistically","Avoids procrastination","Eliminates time-wasters"]),
 ("Result","Value-Adding Work","ዕሴት ጨማሪ ሥራ",
  "Focus on high-impact activities that deliver efficient, sustainable public value.",
  ["Uses resources efficiently","Creates client-perceived value","Quality at lower cost/time","Improves continuously"]),
 ("Result","Discharging Responsibility","ኃላፊነትን መወጣት",
  "Ownership, reliability and accountability for duties and outcomes.",
  ["Takes ownership of outcomes","Meets standard and timeline","Doesn't shift blame","Follows through"]),
 ("Result","Leadership","መሪነት",
  "Clear direction, inspiration, inclusion, and role-modeling civil service values.",
  ["Provides clear direction","Motivates through challenges","Empowers others","Leads inclusively"]),
]
LEVELS = {"Technician":"11 behavioral units · 7 technical","Professional":"12 behavioral units · 8 technical","Leader":"15 behavioral units · 12 technical"}

TECH_UNITS = ["Strategy & Strategic Plan Preparation","Planning","Organizing Resources & Inputs","Technology Utilization",
 "Knowledge","Skill","Professional Ethics","Leading","Decision Making","Monitoring & Effective Performance","Evaluation","Feedback"]

DOMAINS = [
 ("Cognitive","Knowledge, understanding, reasoning, problem-solving.","Remember → Understand → Apply → Analyze → Evaluate → Create"),
 ("Affective","Attitudes, values, emotions, motivation, professional behavior. (Behavioral competency lives here.)","Receiving → Responding → Valuing → Organizing → Characterizing"),
 ("Psychomotor","Physical skills, technical ability, use of tools.","Perception → Set → Guided Response → Mechanism → Complex Overt Response → Adaptation → Origination"),
]

# ---- Emotional Intelligence deck
EI = [
 ("What is EI?","Ability to perceive, understand, regulate and use emotions in self and others. (Salovey & Mayer 1990; Goleman 1995)"),
 ("Core components","Self-awareness · Self-regulation · Motivation · Empathy · Social skills"),
 ("Why it matters in healthcare","Complex patient interactions · High-stress decisions · Team collaboration · Conflict management · Patient-centered care"),
 ("Evidence","Associated with better leadership, lower burnout, improved communication, higher patient satisfaction."),
 ("Clinical applications","Nursing leadership · Physician leadership · Patient counseling · Emergency care · Interprofessional teamwork"),
 ("Challenges","Work overload · Emotional fatigue · Organizational culture · Limited training"),
 ("Building EI","Coaching · Reflection · Simulation training · Mindfulness · Mentoring"),
 ("Bottom line","EI is a strategic competency for quality, safety, leadership and workforce resilience."),
]

# ---- IMS deck
IMS_LIFECYCLE = [("Capture","Data entry & creation"),("Store","Secure warehousing"),("Process","Cleaning & validation"),
 ("Share","Collaboration"),("Analyze","Generating insights"),("Archive","Long-term retention")]
IMS_PILLARS = [("🖥️ Hardware","Servers, computers, sensors: the physical infrastructure."),
 ("</> Software","DBMS, ERP and analytics tools that process raw data."),
 ("⚙️ Processes","Rules and workflows that govern data usage.")]
IMS_TYPES = [("TPS","Operators","Daily receipts / records","Unit-specific"),
 ("MIS","Middle managers","Summary reports","Departmental"),
 ("DSS","Analysts / leads","What-if predictions","Tactical"),
 ("EIS/ERP","Executives","Strategic dashboards","Enterprise-wide")]
IMS_TRENDS = [("Agentic AI","Autonomous agents handling complex information queries."),
 ("Zero Trust","Security models embedded directly in IMS data layers."),
 ("Democratization","Low-code tools so non-technical users build their own insights.")]
