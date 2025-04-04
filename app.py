import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Government KPI Tool", layout="wide")

st.title("📊 Government Programme KPI Suggestion Tool")
st.markdown("Use this tool to generate SMART KPIs for various government projects.")

# Function to get suggested KPIs and outcomes
def get_suggested_kpis_and_outcomes(cofog_sector, project_details):
    kpi_outcome_mapping = {
        "Economic Affairs": {
            "KPIs": [
                "% of work done on road/bridge construction projects",
                "Km of new roads constructed/upgraded",
                "% increase in funding for small businesses",
                "Number of industrial zones developed",
                "% reduction in unemployment rate"
            ],
            "Outcome": "Boosted economic activities and improved infrastructure"
        },
        "General Public Services": {
            "KPIs": [
                "% of work done on government office renovations",
                "% reduction in administrative processing time",
                "Number of government services digitized",
                "% increase in citizen satisfaction surveys",
                "Number of government training programs conducted"
            ],
            "Outcome": "Enhanced government efficiency and transparency"
        },
        "Public Order and Safety": {
            "KPIs": [
                "% of work done on police/fire station upgrades",
                "% reduction in crime rate",
                "Number of CCTV cameras installed",
                "% improvement in emergency response time",
                "Number of personnel trained in safety measures"
            ],
            "Outcome": "Improved security and faster emergency response"
        },
        "Environmental Protection": {
            "KPIs": [
                "% of work done on waste management facility renovations",
                "% reduction in air/water pollution levels",
                "Number of trees planted or green spaces created",
                "Km of drainage systems constructed/rehabilitated",
                "% of drainage system constructed/rehabilitated",
                "% increase in waste recycling efficiency"
            ],
            "Outcome": "Improved environmental sustainability and public health"
        },
        "Social Protection": {
            "KPIs": [
                "% of work done on social housing renovations",
                "% increase in beneficiaries of social welfare programs",
                "Number of low-income housing units built",
                "% reduction in homelessness",
                "Number of community support centers established"
            ],
            "Outcome": "Strengthened social welfare and improved living conditions"
        },
        "Education": {
            "KPIs": [
                "% of work done on school construction/renovation",
                "% increase in student enrollment",
                "Number of digital learning facilities installed",
                "% improvement in teacher-to-student ratio",
                "Number of teachers trained/upskilled"
            ],
            "Outcome": "Improved education quality and accessibility"
        },
        "Health": {
            "KPIs": [
                "% of work done on hospital/clinic construction",
                "% reduction in patient wait times",
                "Number of healthcare professionals trained",
                "% increase in immunization coverage",
                "% decrease in disease prevalence"
            ],
            "Outcome": "Enhanced healthcare services and disease control"
        },
        "Housing and Community Amenities": {
            "KPIs": [
                "% of work done on water and sanitation projects",
                "% increase in potable water supply coverage",
                "Number of public housing units constructed",
                "% improvement in access to electricity",
                "Km of roads upgraded in residential areas"
            ],
            "Outcome": "Improved living standards and infrastructure"
        },
        "Recreation, Culture, and Religion": {
            "KPIs": [
                "% of work done on sports/cultural facility renovations",
                "% increase in tourism visits to cultural sites",
                "Number of recreational events hosted",
                "% increase in funding for cultural preservation",
                "Number of religious/community centers rehabilitated"
            ],
            "Outcome": "Enriched cultural heritage and community well-being"
        }
    }
    return kpi_outcome_mapping.get(cofog_sector, {"KPIs": ["Custom KPI based on project scope"], "Outcome": "Customized based on project"})

# Streamlit Sidebar UI
st.sidebar.header("Project Details")
cofog_sectors = [
    "Economic Affairs", "General Public Services", "Public Order and Safety",
    "Environmental Protection", "Social Protection", "Education", "Health",
    "Housing and Community Amenities", "Recreation, Culture, and Religion"
]
sector = st.sidebar.selectbox("Select Government Sector (COFOG)", cofog_sectors)
project_title = st.sidebar.text_input("Enter Project Title")
contractor_name = st.sidebar.text_input("Enter Contractor Name")
project_details = st.sidebar.text_area("Describe the Project")

if st.sidebar.button("Generate KPIs"):
    st.subheader(f"KPIs for {sector}")
    result = get_suggested_kpis_and_outcomes(sector, project_details)
    for kpi in result["KPIs"]:
        st.write(f"- {kpi}")
    
    st.subheader("Expected Outcome Statement")
    st.success(result["Outcome"])
