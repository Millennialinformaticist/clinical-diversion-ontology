import streamlit as st

st.set_page_config(page_title="Diversion Logic Framework", layout="wide")

st.title("📄 Technical Documentation: Algorithmic Diversion Detection")
st.markdown("""
### Overview
This framework documents the **Diversion Triangulation** methodology used to reconcile 
Automated Dispensing Cabinet (ADC) data with Electronic Medication Administration Records (eMAR).
""") # [cite: 8, 27]

tab1, tab2, tab3 = st.tabs(["Data Lineage", "Performance Metrics", "Governance"])

with tab1:
    st.header("The Ontology Mapping")
    st.write("Mapping raw SQL/HL7 data to USCDI standards for interoperability.") # [cite: 220, 221]
    st.code("""
    Pyxis_User_ID   -> Care Team Member (USCDI)
    Drug_Name/NDC   -> Medication (USCDI)
    Admin_Timestamp -> Administration Step
    """) # [cite: 223, 224, 225, 226]

with tab2:
    st.header("Validation Benchmarks")
    col1, col2 = st.columns(2)
    col1.metric("Detection Accuracy", "94.3%", "Target: >95%") # [cite: 9, 88]
    col2.metric("Positive Predictive Value", "87.4%", "Goal: Minimize Fatigue") # [cite: 9, 145]
    st.info("Detection latency averaged 18 minutes, a significant shift from 24-hour forensics.") # [cite: 10, 116]

with tab3:
    st.header("Interdisciplinary Governance")
    st.write("Technical systems fail without the 'Human-in-the-loop'.") # [cite: 56, 139]
    st.markdown("""
    - **Pharmacy Informatics:** Reduced manual reconciliation by 15-20%. [cite: 11, 130]
    - **Nursing Leadership:** Iterative feedback reduced false positives from 12% to 6.8%. [cite: 97, 126]
    - **Safe Reporting:** Microsoft Teams alerts bypassed traditional reporting barriers. [cite: 33, 63]
    """)
