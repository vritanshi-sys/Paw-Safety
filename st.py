import streamlit as st
import pandas as pd
from datetime import datetime
import uuid

# =====================================================
# PAGE SETUP
# =====================================================
st.set_page_config(
    page_title="Paw Safety",
    page_icon="🐾",
    layout="wide"
)

# =====================================================
# SESSION DATA
# =====================================================
if "reports" not in st.session_state:
    st.session_state.reports = []

if "food_requests" not in st.session_state:
    st.session_state.food_requests = []

if "help_requests" not in st.session_state:
    st.session_state.help_requests = []


def create_id(prefix="PG"):
    return f"{prefix}-{str(uuid.uuid4())[:6].upper()}"


# ================= COLOR DESIGN =================
st.markdown("""
<style>

/* MAIN BACKGROUND */
.stApp {
    background: linear-gradient(135deg, #FFF3E0 0%, #E3F2FD 100%) !important;
}

/* MAIN TITLES */
h1 {
    color: #000000 !important;
    font-weight: 900 !important;
}

h2 {
    color: #1565C0 !important;
    font-weight: 900 !important;
}

h3 {
    color: #E65100 !important;
    font-weight: 900 !important;
}

/* SIDEBAR */
section[data-testid="stSidebar"] {
    background: #FFFFFF !important;
    border-right: 5px solid #1565C0 !important;
}

/* SIDEBAR TITLE */
section[data-testid="stSidebar"] h1 {
    color: #000000 !important;
    font-size: 30px !important;
    font-weight: 900 !important;
}

/* SIDEBAR TEXT */
section[data-testid="stSidebar"] p,
section[data-testid="stSidebar"] label,
section[data-testid="stSidebar"] span {
    color: #000000 !important;
    font-weight: 700 !important;
}

/* RADIO MENU */
section[data-testid="stSidebar"] div[role="radiogroup"] label {
    color: #000000 !important;
    font-weight: 700 !important;
}

/* BUTTONS */
.stButton > button,
.stFormSubmitButton > button {
    background: #FF6D00 !important;
    color: #FFFFFF !important;
    border: 2px solid #E65100 !important;
    border-radius: 10px !important;
    font-weight: 900 !important;
}

/* BUTTON HOVER */
.stButton > button:hover,
.stFormSubmitButton > button:hover {
    background: #D84315 !important;
    color: #FFFFFF !important;
}

/* CARDS */
.card {
    background: #FFFFFF !important;
    color: #000000 !important;
    padding: 20px !important;
    margin: 10px 0 !important;
    border-radius: 15px !important;
    border-left: 8px solid #FF6D00 !important;
    box-shadow: 0 5px 15px rgba(0,0,0,0.20) !important;
}

.card h3 {
    color: #1565C0 !important;
}

.card p {
    color: #000000 !important;
    font-weight: 600 !important;
}

/* METRICS */
div[data-testid="stMetric"] {
    background: #FFFFFF !important;
    border: 3px solid #1565C0 !important;
    border-radius: 12px !important;
    padding: 15px !important;
}

div[data-testid="stMetricLabel"] {
    color: #1565C0 !important;
    font-weight: 900 !important;
}

div[data-testid="stMetricValue"] {
    color: #D50000 !important;
    font-weight: 900 !important;
}

/* INPUT LABELS */
label {
    color: #000000 !important;
    font-weight: 800 !important;
}

/* INFO */
div[data-testid="stAlert"] {
    font-weight: 700 !important;
}

/* DATAFRAME */
div[data-testid="stDataFrame"] {
    border: 3px solid #1565C0 !important;
    border-radius: 10px !important;
}

</style>
""", unsafe_allow_html=True)


# ================= SIDEBAR TITLE =================
st.sidebar.markdown(
    '<h1 style="color:#000000 !important;">🐾 Paw Safety</h1>',
    unsafe_allow_html=True
)

st.sidebar.markdown(
    '<p style="color:#000000 !important;font-weight:800;">'
    'Safety for Students. Care for Animals.'
    '</p>',
    unsafe_allow_html=True
)

st.sidebar.divider()




# =====================================================
# SIDEBAR
# =====================================================

# 🖤 PAW SAFETY IN BLACK
st.sidebar.markdown(
    '<h1 style="color:#000000 !important;">🐾 Paw Safety</h1>',
    unsafe_allow_html=True
)

st.sidebar.write("**Safety for Students. Care for Animals.**")
st.sidebar.divider()

page = st.sidebar.radio(
    "📌 MENU",
    [
        "🏠 Home",
        "📝 Report Problem",
        "🎙️ Voice Report",
        "🍲 Food & Water",
        "🏠 Shelters",
        "🚑 Animal Help",
        "📊 Dashboard",
        "🔎 All Reports",
        "🛡️ Admin Panel",
        "ℹ️ About"
    ]
)


# =====================================================
# HOME
# =====================================================
if page == "🏠 Home":

    st.title("🐾 Paw Safety")
    st.subheader("🛡️ Safety for Students. Care for Animals.")

    st.write(
        "A smart campus platform for reporting animal-related "
        "issues and coordinating food, shelter and emergency help."
    )

    st.divider()

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("📝 Reports", len(st.session_state.reports))
    c2.metric("🍲 Food Requests", len(st.session_state.food_requests))
    c3.metric("🚑 Help Requests", len(st.session_state.help_requests))

    c4.metric(
        "⚡ Active Cases",
        sum(
            r["Status"] != "Resolved"
            for r in st.session_state.reports
        )
    )

    st.markdown("## 🌟 Paw Safety Features")

    a, b, c = st.columns(3)

    with a:
        st.markdown("""
        <div class="card">
        <h3>📝 Smart Reporting</h3>
        <p>Report animal-related problems with location,
        severity and photos.</p>
        </div>
        """, unsafe_allow_html=True)

    with b:
        st.markdown("""
        <div class="card">
        <h3>🎙️ Voice Reporting</h3>
        <p>Record a voice message instead of typing
        a complete report.</p>
        </div>
        """, unsafe_allow_html=True)

    with c:
        st.markdown("""
        <div class="card">
        <h3>🍲 Animal Care</h3>
        <p>Report food, water, shelter and medical requirements.</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("## 🔄 How It Works")

    st.info(
        "📍 Select Location → 📝 Report → 🛡️ Admin Review "
        "→ 🐾 Action → ✅ Resolved"
    )


# =====================================================
# REPORT PROBLEM
# =====================================================
elif page == "📝 Report Problem":

    st.title("📝 Report a Campus Problem")

    with st.form("report_form"):

        col1, col2 = st.columns(2)

        with col1:
            hostel = st.text_input("🏠 Hostel / Building")
            block = st.text_input("🏢 Block")
            floor = st.text_input("🔢 Floor")
            room = st.text_input("🚪 Room Number")

        with col2:
            location = st.text_input("📍 Specific Location")

            problem = st.selectbox(
                "⚠️ Problem Type",
                [
                    "Dog entering area",
                    "Aggressive behaviour",
                    "Injured animal",
                    "Stray animal issue",
                    "Animal disturbing students",
                    "Other"
                ]
            )

            severity = st.selectbox(
                "🚨 Severity",
                ["Low", "Medium", "High", "Emergency"]
            )

            animals = st.number_input(
                "🐕 Number of Animals",
                min_value=1,
                max_value=50,
                value=1
            )

        description = st.text_area("📝 Describe the problem")

        photo = st.file_uploader(
            "📷 Upload Photo",
            type=["jpg", "jpeg", "png"]
        )

        anonymous = st.checkbox("👤 Submit anonymously")
        priority = st.checkbox("🚨 Mark as High Priority")

        submit = st.form_submit_button("🚀 SUBMIT REPORT")

    if submit:

        report = {
            "ID": create_id(),
            "Type": "Problem",
            "Hostel": hostel,
            "Block": block,
            "Floor": floor,
            "Room": room,
            "Location": location,
            "Problem": problem,
            "Animals": animals,
            "Severity": severity,
            "Description": description,
            "Priority": priority,
            "Anonymous": anonymous,
            "Status": "Pending",
            "Time": datetime.now().strftime("%d-%m-%Y %H:%M"),
            "Photo": photo.name if photo else "No photo"
        }

        st.session_state.reports.append(report)

        st.success("✅ Report submitted successfully!")
        st.info(f"🆔 Report ID: **{report['ID']}**")


# =====================================================
# VOICE REPORT
# =====================================================
elif page == "🎙️ Voice Report":

    st.title("🎙️ Voice Report")

    st.write("Use your microphone to record an animal-safety report.")

    with st.form("voice_form"):

        location = st.text_input("📍 Location")

        problem = st.selectbox(
            "⚠️ Problem Type",
            [
                "Animal Safety Issue",
                "Aggressive Behaviour",
                "Injured Animal",
                "Food / Water Issue",
                "Other"
            ]
        )

        audio = st.audio_input("🎙️ Record Voice Report")

        details = st.text_area("📝 Additional Details")

        anonymous = st.checkbox(
            "👤 Submit anonymously",
            key="voice_anonymous"
        )

        submit = st.form_submit_button("🚨 SEND VOICE REPORT")

    if submit:

        if audio is None:

            st.warning("🎙️ Please record your voice message first.")

        else:

            report = {
                "ID": create_id("VOICE"),
                "Type": "Voice Report",
                "Location": location,
                "Problem": problem,
                "Description": details,
                "Anonymous": anonymous,
                "Status": "Pending",
                "Time": datetime.now().strftime("%d-%m-%Y %H:%M"),
                "Audio": audio
            }

            st.session_state.reports.append(report)

            st.success(
                f"✅ Voice report submitted! ID: {report['ID']}"
            )

            st.audio(audio)


# =====================================================
# FOOD & WATER
# =====================================================
elif page == "🍲 Food & Water":

    st.title("🍲 Food & Water")

    st.write(
        "Help maintain food and water availability for animals."
    )

    st.markdown("## 🥣 Campus Feeding Stations")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown("### 🏠 Hostel A")
        st.write("🍲 Food + 💧 Water")
        st.success("🟢 Available")

    with c2:
        st.markdown("### 🏠 Hostel B")
        st.write("💧 Water")
        st.warning("🟠 Needs Refill")

    with c3:
        st.markdown("### 🏫 Academic Block")
        st.write("🍲 Food")
        st.success("🟢 Available")

    st.divider()

    st.subheader("🚰 Report Food / Water Requirement")

    with st.form("food_form"):

        location = st.text_input(
            "📍 Location",
            key="food_location"
        )

        need = st.selectbox(
            "What is needed?",
            [
                "🍲 Food",
                "💧 Water",
                "🍲 Food + 💧 Water"
            ]
        )

        condition = st.selectbox(
            "Current Condition",
            ["Empty", "Low", "Missing"]
        )

        photo = st.file_uploader(
            "📷 Upload Photo",
            type=["jpg", "jpeg", "png"],
            key="food_photo"
        )

        details = st.text_area(
            "📝 Details",
            key="food_details"
        )

        submit = st.form_submit_button(
            "🚀 SUBMIT FOOD / WATER REQUEST"
        )

    if submit:

        request = {
            "ID": create_id("FOOD"),
            "Location": location,
            "Need": need,
            "Condition": condition,
            "Details": details,
            "Status": "Reported",
            "Time": datetime.now().strftime("%d-%m-%Y %H:%M")
        }

        st.session_state.food_requests.append(request)

        st.success(
            f"✅ Request submitted! ID: {request['ID']}"
        )


# =====================================================
# SHELTERS
# =====================================================
elif page == "🏠 Shelters":

    st.title("🏠 Animal Shelters")

    c1, c2 = st.columns(2)

    with c1:
        st.markdown("""
        <div class="card">
        <h3>🐾 Campus Animal Care</h3>
        <p>📍 Campus Area</p>
        <p>🚑 Rescue • First Aid • Shelter</p>
        <p>🟢 Support Available</p>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown("""
        <div class="card">
        <h3>🐾 Animal Care Centre</h3>
        <p>📍 Nearby City</p>
        <p>🚑 Treatment • Rescue • Support</p>
        <p>🟢 Care Services</p>
        </div>
        """, unsafe_allow_html=True)

    st.divider()

    st.subheader("🆘 Request Shelter Help")

    location = st.text_input(
        "📍 Animal Location",
        key="shelter_location"
    )

    reason = st.text_area(
        "📝 Why is help needed?",
        key="shelter_reason"
    )

    if st.button("🚑 REQUEST SHELTER HELP"):

        request = {
            "ID": create_id("SHELTER"),
            "Type": "Shelter Help",
            "Location": location,
            "Details": reason,
            "Status": "Pending",
            "Time": datetime.now().strftime("%d-%m-%Y %H:%M")
        }

        st.session_state.help_requests.append(request)

        st.success(
            f"✅ Shelter request created: {request['ID']}"
        )


# =====================================================
# ANIMAL HELP
# =====================================================
elif page == "🚑 Animal Help":

    st.title("🚑 Animal Help Center")

    help_type = st.selectbox(
        "🆘 Help Required",
        [
            "Medical Help",
            "Injured Animal",
            "Rescue Assistance",
            "Lost Animal",
            "Found Animal"
        ]
    )

    location = st.text_input(
        "📍 Animal Location",
        key="help_location"
    )

    details = st.text_area(
        "📝 Details",
        key="help_details"
    )

    photo = st.file_uploader(
        "📷 Upload Photo",
        type=["jpg", "jpeg", "png"],
        key="help_photo"
    )

    if st.button("🚑 REQUEST HELP"):

        request = {
            "ID": create_id("HELP"),
            "Type": help_type,
            "Location": location,
            "Details": details,
            "Status": "Pending",
            "Time": datetime.now().strftime("%d-%m-%Y %H:%M")
        }

        st.session_state.help_requests.append(request)

        st.success(
            f"🆔 Help Request ID: {request['ID']}"
        )


# =====================================================
# DASHBOARD
# =====================================================
elif page == "📊 Dashboard":

    st.title("📊 Campus Safety Dashboard")

    reports = st.session_state.reports

    total = len(reports)

    pending = sum(
        r["Status"] == "Pending"
        for r in reports
    )

    resolved = sum(
        r["Status"] == "Resolved"
        for r in reports
    )

    emergency = sum(
        r.get("Severity") == "Emergency"
        for r in reports
    )

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("📝 Total", total)
    c2.metric("🟠 Pending", pending)
    c3.metric("🟢 Resolved", resolved)
    c4.metric("🚨 Emergency", emergency)

    if reports:

        df = pd.DataFrame(reports)

        st.subheader("📈 Reports by Problem")

        if "Problem" in df.columns:
            st.bar_chart(
                df["Problem"].value_counts()
            )

        st.subheader("📋 Report Data")

        st.dataframe(
            df.drop(
                columns=["Audio"],
                errors="ignore"
            ),
            use_container_width=True
        )

    else:
        st.info("No reports available yet.")


# =====================================================
# ALL REPORTS
# =====================================================
elif page == "🔎 All Reports":

    st.title("🔎 Search Reports")

    search = st.text_input(
        "Search by ID, location, hostel or problem"
    )

    reports = st.session_state.reports

    if search:

        reports = [
            r for r in reports
            if search.lower() in str(r).lower()
        ]

    if reports:

        df = pd.DataFrame(reports)

        st.dataframe(
            df.drop(
                columns=["Audio"],
                errors="ignore"
            ),
            use_container_width=True
        )

    else:
        st.info("🔍 No reports found.")


# =====================================================
# ADMIN PANEL
# =====================================================
elif page == "🛡️ Admin Panel":

    st.title("🛡️ Admin Control Panel")

    st.warning(
        "Prototype admin panel — production version should "
        "use university authentication."
    )

    st.subheader("📝 Problem Reports")

    if not st.session_state.reports:
        st.info("No reports yet.")

    for report in st.session_state.reports:

        st.markdown(
            f"### 🆔 {report['ID']}"
        )

        st.write(
            f"⚠️ **Problem:** "
            f"{report.get('Problem', 'Voice Report')}"
        )

        st.write(
            f"📍 **Location:** "
            f"{report.get('Location', 'Not specified')}"
        )

        st.write(
            f"🚨 **Status:** {report['Status']}"
        )

        status = st.selectbox(
            "Update Status",
            [
                "Pending",
                "In Progress",
                "Resolved"
            ],
            index=[
                "Pending",
                "In Progress",
                "Resolved"
            ].index(report["Status"]),
            key="admin_" + report["ID"]
        )

        report["Status"] = status

        if report.get("Audio") is not None:
            st.audio(report["Audio"])

        st.divider()

    st.subheader("🍲 Food / Water Requests")

    for request in st.session_state.food_requests:

        st.write(
            f"🆔 **{request['ID']}** | "
            f"📍 {request['Location']} | "
            f"{request['Need']} | "
            f"Status: **{request['Status']}**"
        )

    st.subheader("🚑 Animal Help Requests")

    for request in st.session_state.help_requests:

        st.write(
            f"🆔 **{request['ID']}** | "
            f"{request['Type']} | "
            f"📍 {request['Location']} | "
            f"Status: **{request['Status']}**"
        )


# =====================================================
# ABOUT
# =====================================================
elif page == "ℹ️ About":

    st.title("ℹ️ About Paw Safety")

    st.markdown("""
    ### 🐾 Our Mission

    **Paw Safety** is a campus safety and animal-welfare
    platform designed to connect students, university
    administration and animal-care services.

    ### 💡 Technology

    🐍 **Python**  
    🎨 **Streamlit**  
    📊 **Pandas**  
    🎙️ **Microphone / Audio Input**  
    📷 **Image Upload**  
    💾 **Session State**

    ### 🚀 Future Scope

    🔐 University Login  
    ☁️ Firebase / PostgreSQL Database  
    🔔 Notifications  
    🤖 AI Voice-to-Text  
    🤖 AI Report Classification  
    🔍 Duplicate Report Detection  
    📊 Advanced Analytics
    """)

    st.success(
        "🐾 Paw Safety — Making campuses safer for students "
        "while caring for animals."
    )


# =====================================================
# FOOTER
# =====================================================
st.sidebar.divider()
st.sidebar.success("🐾 Paw Safety Active")
st.sidebar.caption("Campus Safety + Animal Welfare")