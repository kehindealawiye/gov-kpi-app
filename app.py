import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Government KPI Tool", layout="wide")

st.title("📊 Government Programme KPI Suggestion Tool")
st.markdown("Use this tool to generate SMART KPIs for various Government Programmes and Projects.")

# COFOG sectors
cofog_sectors = [
    "Economic Affairs", "General Public Services", "Public Order and Safety",
    "Environmental Protection", "Social Protection", "Education", "Health",
    "Housing and Community Amenities", "Recreation, Culture, and Religion"
]

# Keyword-based logic for suggesting KPIs and outcomes based on sector, project title, and details
def get_suggested_kpis_and_outcomes(cofog_sector, project_title, project_details):
    text = f"{project_title.lower()} {project_details.lower()}"

    base_kpis = {
        "Economic Affairs": [
            "Km of roads constructed",
            "Km of roads rehabilitated",
            "Number of markets constructed",
            "Number of farmers supported",
            "Number of MSMEs provided with credit",
            "Number of drugs and health commodities procured as per the procurement plan",
            "Percentage of technical health staff trained in diagnostic techniques",
            "Km of rural roads upgraded"
        ],
        "General Public Services": [
            "Number of digitized services launched",
            "Number of public servants trained",
            "Number of government portals developed",
            "Number of public outreach events conducted",
            "Number of ministries audited",
            "Number of public awareness campaigns conducted"
        ],
        "Public Order and Safety": [
            "Number of police stations built",
            "Number of CCTV cameras installed",
            "Number of officers trained in conflict resolution",
            "Number of emergency response drills conducted",
            "Number of vehicles procured for law enforcement",
            "Percentage of emergency response time reduced by trained personnel"
        ],
        "Environmental Protection": [
            "Hectares of land reforested",
            "Number of waste bins distributed",
            "Number of water bodies cleaned",
            "Tons of waste recycled",
            "Km of drainage cleared",
            "Percentage of urban waste disposed correctly"
        ],
        "Social Protection": [
            "Number of vulnerable households supported",
            "Number of cash transfers distributed",
            "Number of shelters constructed for displaced persons",
            "Number of people enrolled in social welfare programs",
            "Number of food packages distributed",
            "Percentage of enrolled beneficiaries receiving monthly assistance"
        ],
        "Education": [
            "Number of classrooms constructed",
            "Number of students receiving scholarships",
            "Number of schools renovated",
            "Number of teachers trained in modern educational techniques",
            "Number of educational devices distributed to schools",
            "Number of students trained in career-building initiatives"
        ],
        "Health": [
            "Number of health centres constructed",
            "Number of ambulances procured",
            "Number of health workers trained in emergency response",
            "Number of vaccines administered",
            "Number of beds added to hospitals",
            "Percentage of health centres meeting operational standards"
        ],
        "Housing and Community Amenities": [
            "Number of housing units built",
            "Km of streetlights installed",
            "Number of boreholes installed",
            "Number of drainage systems constructed",
            "Number of electrification projects completed",
            "Percentage of urban areas covered by new housing projects"
        ],
        "Recreation, Culture, and Religion": [
            "Number of recreational parks built",
            "Number of cultural festivals supported",
            "Number of libraries constructed",
            "Number of youth centres upgraded",
            "Number of religious centres upgraded",
            "Number of monuments and heritage sites monitored"
        ]
    }

    outcomes = {
        "Economic Affairs": "Improved economic infrastructure and increased market access for small and medium enterprises (SMEs).",
        "General Public Services": "Enhanced public service delivery and improved government transparency and accessibility.",
        "Public Order and Safety": "Increased public safety through enhanced emergency response systems and law enforcement capabilities.",
        "Environmental Protection": "Improved environmental sustainability through effective waste management and land restoration projects.",
        "Social Protection": "Increased social inclusion and enhanced safety nets for vulnerable households.",
        "Education": "Improved access to quality education and infrastructure, fostering higher student enrollment rates.",
        "Health": "Enhanced healthcare service delivery and access to quality medical facilities for all citizens.",
        "Housing and Community Amenities": "Enhanced living conditions and better urban planning through new housing and community development projects.",
        "Recreation, Culture, and Religion": "Enhanced community engagement and cultural preservation through recreational activities and religious observances."
    }

    sector_kpis = base_kpis.get(cofog_sector, [])

    # Add logic for keyword matching to suggest more KPIs
    keyword_kpi_map = {
        "road": "Km of roads constructed",
        "bridge": "Number of bridges completed",
        "renovation": "Number of facilities renovated",
        "training": "Number of people trained in career-building initiatives",
        "digital": "Number of digital platforms developed",
        "school": "Number of schools constructed",
        "hospital": "Number of health facilities constructed",
        "borehole": "Number of boreholes installed",
        "waste": "Tons of waste disposed/recycled",
        "housing": "Number of housing units built",
        "youth": "Number of youth centres upgraded",
        "security": "Number of security gadgets procured"
    }

    for keyword, kpi in keyword_kpi_map.items():
        if keyword in text and kpi not in sector_kpis:
            sector_kpis.append(kpi)

    # Ensure unique KPIs
    sector_kpis = list(set(sector_kpis))

    # Outcome statement
    if program_or_project == "Program":
        outcome_statement = f"The program will deliver: {outcomes.get(cofog_sector, 'Outcome customized based on program impact')}"
    else:
        outcome_statement = f"The project will deliver: {outcomes.get(cofog_sector, 'Outcome customized based on project impact')}"

    return {
        "KPIs": sector_kpis,
        "Outcome": outcome_statement
    }

# Sidebar input
st.sidebar.header("Project Details")
sector = st.sidebar.selectbox("Select Government Sector (COFOG)", cofog_sectors)
program_or_project = st.sidebar.selectbox("Is this a Programme or Project?", ["Programme", "Project"])
mda = st.sidebar.text_input("Enter MDA (Ministry, Department, or Agency)")
project_title = st.sidebar.text_input("Enter Project Title")
project_details = st.sidebar.text_area("Describe the Project")

if st.sidebar.button("Generate KPIs"):
    st.subheader(f"KPIs for {sector} - {programme_or_project}")
    result = get_suggested_kpis_and_outcomes(sector, project_title, project_details, programme_or_project)

    st.markdown("### Suggested Output-Based KPIs")
    for kpi in result["KPIs"]:
        st.write(f"- {kpi}")

    st.markdown("### Expected Outcome Statement")
    st.success(result["Outcome"])
    st.markdown(f"**MDA:** {mda}")