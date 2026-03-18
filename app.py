import streamlit as st

st.set_page_config(page_title="Palantir Healthcare Strategy: Diversion", layout="wide")

st.title("🛡️ Diversion Intelligence: Palantir Priority Alignment")
st.sidebar.header("Connected Use Cases")

# Navigation based on the Palantir Documentation
menu = ["Clinical Care", "Revenue Cycle", "Scheduling + Staffing", "Capacity & Hand-off"]
choice = st.sidebar.radio("Select Priority Area", menu)

if choice == "Clinical Care":
    st.header("✨ Automated Clinical Documentation")
    st.write("Using Algorithmic Diversion Surveillance (ADS) to reconcile the medication-use continuum[cite: 195].")
    col1, col2 = st.columns(2)
    col1.metric("Detection Accuracy", "94.3%", "Target: 95%") # [cite: 9, 96, 141]
    col2.metric("Detection Latency", "18 Mins", "Target: <1 Hour") # [cite: 10, 116, 139]

elif choice == "Revenue Cycle":
    st.header("💰 Automated Charge Capture & Loss Prevention")
    st.info("Narcotic diversion costs the U.S. healthcare system ~ billion annually[cite: 5, 45].")
    st.write("### Economic Recovery")
    st.write("- **Manual Effort Reduction:** 15-20% [cite: 11, 130]")
    st.write("- **Opportunity Cost Recovery:** ~,104–,472 per analyst/year [cite: 131, 171]")

elif choice == "Scheduling + Staffing":
    st.header("👥 Staffing Risk & 'Waste Buddy' Detection")
    st.write("Transitioning to Machine Learning (ML) to detect collusion patterns[cite: 207, 211].")
    st.warning("High-frequency dyadic witnessing is a strong predictor of procedural drift[cite: 212].")

elif choice == "Capacity & Hand-off":
    st.header("🏥 Capacity Management & Transitions of Care")
    st.write("### Nurse Hand-off Integrity")
    st.write("Identifying 'batched' documentation at shift changes to ensure safe hand-offs.")
    st.write("### Discharge Navigation")
    st.write("Ensuring therapeutic analgesia to prevent sub-therapeutic outcomes that delay discharge[cite: 148].")
