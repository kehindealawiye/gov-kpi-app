import streamlit as st
import json

st.set_page_config(page_title="Government KPI Directory", layout="wide")

# Add custom CSS for background image, text color, and accents
st.markdown(
    """
    <style>
        .stApp {
            background-color: #001f3f !important; /* Navy blue */
        }
        h1, h2, h3, h4, h5, h6, label, .stText, .stMarkdown, .stSelectbox > div {
            color: white !important;
        }
        input, select, textarea {
            background-color: white !important;
            color: #001f3f !important;
            font-weight: bold;
        }
        .stAlert-success {
            background-color: #ffffff !important;  /* white */
            color: white !important;
            font-weight: bold !important;
            border-radius: 5px;
            padding: 10px;
        }
    </style>
    """,
    unsafe_allow_html=True
)


# Load KPI and Outcome directory from uploaded document
kpi_directory = {
   "Economic Affairs": {
    "Office of Infrastructure": {
      "kpis": [
        "% work to be done",
        "Km of roads constructed",
        "Km of roads rehabilitated",
        "Number of pedestrian bridges constructed",
        "Number of infrastructure consultancy projects completed",
        "Number of projects completed on time"
      ],
      "outcome": "Improved road infrastructure and transportation access"
    },
    "Lagos Metropolitan Area Transport Authority (LAMATA)": {
      "kpis": [
        "Number of rail services operationalized",
        "Number of BRT terminals constructed",
        "Number of BRT vehicles procured",
        "Number of passengers served daily",
        "Number of maintenance programs completed for BRT systems"
      ],
      "outcome": "Improved mass transit efficiency and commuter satisfaction"
    },
    "Ministry of Transportation": {
      "kpis": [
        "Number of junctions upgraded",
        "Number of traffic signal lights installed",
        "Number of zebra crossings marked",
        "Km of lanes improved or added",
        "Number of traffic-related accidents reduced"
      ],
      "outcome": "Enhanced road safety and improved traffic flow"
    },
    "Office of Sustainable Development Goals (SDGs)": {
      "kpis": [
        "Number of SDG programs implemented",
        "Number of volunteers engaged in SDG projects",
        "Amount of funding mobilized for SDG initiatives",
        "Number of SDG partnership agreements signed",
        "Number of SDG awareness campaigns conducted"
      ],
      "outcome": "Strengthened local SDG implementation and awareness"
    },
    "Ministry of Waterfront Infrastructure Development": {
      "kpis": [
        "% work to be done",
        "Number of waterways channelized",
        "Number of ferry routes developed",
        "Number of jetty terminals constructed",
        "Number of floating jetties installed",
        "Number of water transport services improved"
      ],
      "outcome": "Enhanced water transportation and reduced traffic congestion"
    },
    "Office of Works": {
      "kpis": [
        "% work to be done",
        "Number of buildings renovated",
        "Number of electrical systems upgraded",
        "Number of public facilities retrofitted",
        "Number of lifts serviced or replaced",
        "Number of construction projects completed on time"
      ],
      "outcome": "Improved quality and safety of public infrastructure"
    },
    "Public Works Corporation": {
      "kpis": [
        "% work to be done",
        "Km of drainage constructed",
        "Km of drainage maintained",
        "Number of equipment refurbished",
        "Number of roads rehabilitated",
        "Number of plant and heavy equipment procured"
      ],
      "outcome": "Upgraded drainage and road infrastructure"
    },
    "Ministry of Agriculture": {
      "kpis": [
        "% work to be done",
        "Number of agricultural value chain enterprises activated",
        "Number of coconut processing Centres established",
        "Number of agro-processing units set up",
        "Number of agricultural training programs conducted",
        "Amount of rice produced (tons)",
        "Number of hectares of land afforested"
      ],
      "outcome": "Increased agricultural productivity and improved livelihoods for farmers"
    },
    "Ministry of Wealth Creation and Employment": {
      "kpis": [
        "Number of job fairs organized",
        "Number of youths trained in digital entrepreneurship",
        "Number of youth employed or self-employed post-training",
        "Number of industrial hubs established",
        "Number of people with disabilities supported",
        "Number of ICT training sessions held"
      ],
      "outcome": "Increased employment opportunities and youth empowerment"
    },
    "Ministry of Energy and Mineral Resources": {
      "kpis": [
        "% work to be done",
        "Number of abandoned oil & gas facilities rehabilitated",
        "Number of LPG retailers migrated to safer operations",
        "Amount of LPG and CNG distributed",
        "Number of solar-powered streetlights installed",
        "Number of energy audit reports completed"
      ],
      "outcome": "Improved energy efficiency and access to clean energy"
    },
    "Ministry of Commerce, Industry and Cooperatives": {
      "kpis": [
        "% work to be done",
        "Number of MSMEs supported",
        "Number of business hubs established",
        "Number of cooperatives formed or supported",
        "Number of enterprises receiving training",
        "Amount of investment attracted into the industrial zones",
        "Number of corporate assembly meetings held"
      ],
      "outcome": "Enhanced enterprise growth and economic diversification"
    },
    "Lagos State Infrastructure Asset Management Agency": {
      "kpis": [
        "% work to be done",
        "Number of state infrastructure facilities maintained",
        "Number of educational facilities upgraded",
        "Amount of savings generated through improved asset management",
        "Number of preventive maintenance programs completed"
      ],
      "outcome": "Increased lifespan and efficiency of public infrastructure"
    }
  },
  "General Public Services": {
    "Ministry of Finance": {
      "kpis": [
        "Percentage of payment disbursements made within 5 working days",
        "Percentage of insurance claims settled within 3 months",
        "Amount of revenue generated from land use charges",
        "Number of properties enumerated",
        "Percentage return on investment income",
        "Percentage of loan repayments completed on schedule"
      ],
      "outcome": "Improved financial efficiency and accountability in government operations"
    },
    "Office of the Chief of Staff": {
      "kpis": [
        "Percentage completion of police station constructions and renovations",
        "Number of renovation works completed",
        "Number of stakeholder engagement meetings held"
      ],
      "outcome": "Strengthened executive coordination and infrastructure delivery"
    },
    "Ministry of Economic Planning and Budget": {
      "kpis": [
        "Number of economic and performance reports produced",
        "Amount of development loans and grants received",
        "Number of resilience risk assessments conducted",
        "Number of social protection programs tracked",
        "Number of macroeconomic indicator reports published",
        "Percentage of project work completed"
      ],
      "outcome": "Enhanced planning, budgeting, and development coordination"
    },
    "Public Procurement Agency": {
      "kpis": [
        "Percentage of procurement records compliant with standards",
        "Number of procurement capacity-building workshops conducted",
        "Percentage of annual procurement plan submissions completed"
      ],
      "outcome": "Strengthened transparency and efficiency in public procurement"
    },
    "Office of the Deputy Governor": {
      "kpis": [
        "Number of welfare packages distributed",
        "Number of advocacy meetings held",
        "Percentage of international engagements aligned with THEMES+ Agenda"
      ],
      "outcome": "Improved community relations and policy advocacy"
    },
    "Ministry of Local Government and Community Affairs": {
      "kpis": [
        "Number of market infrastructure projects completed",
        "Number of rural electrification interventions delivered",
        "Number of community-based agriculture interventions implemented"
      ],
      "outcome": "Improved rural and community development infrastructure"
    },
    "Ministry of Information and Strategy": {
      "kpis": [
        "Number of sensitization campaigns conducted",
        "Number of media productions completed quarterly",
        "Number of social media followers on official platforms"
      ],
      "outcome": "Improved public awareness and citizen engagement"
    },
    "Ministry of Science and Technology": {
      "kpis": [
        "Kilometers of fiber optic cable laid",
        "Number of tech innovators supported",
        "Number of vehicles tracked using government systems"
      ],
      "outcome": "Expanded digital infrastructure and innovation ecosystem"
    },
    "Public Service Office": {
      "kpis": [
        "Number of MDAs participating in public service games",
        "Number of staff trained in management retreats",
        "Number of staff quarters rehabilitated"
      ],
      "outcome": "Enhanced staff welfare and performance"
    },
    "Office of Civic Engagement": {
      "kpis": [
        "Number of legislative awareness campaigns conducted",
        "Number of dispute resolution meetings held",
        "Number of financial assistance cases processed"
      ],
      "outcome": "Improved civic inclusion and legal awareness"
    },
    "Ministry of Establishments and Training": {
      "kpis": [
        "Number of training sessions conducted",
        "Number of staff attending international workshops",
        "Number of staff placed for on-the-job training"
      ],
      "outcome": "Improved workforce competence and development"
    },
    "Civil Service Commission": {
      "kpis": [
        "Percentage of personnel files digitized",
        "Number of monthly digitized files",
        "Percentage of digitized files stored in central database",
        "Percentage of eligible officers trained for promotion",
        "Number of promotion interviews conducted",
        "Percentage of promotion recommendations processed on time",
        "Number of officers recruited",
        "Percentage of recruitment appeals processed within 30 days",
        "Number of recruitment campaigns conducted",
        "Percentage of officers confirmed as scheduled",
        "Number of confirmation processes completed on time",
        "Percentage of confirmed officers meeting required criteria",
        "Percentage of decisions documented within the timeline",
        "Number of decisions made monthly",
        "Percentage of decisions reviewed and approved on time",
        "Number of directives issued within the fiscal year",
        "Number of directives communicated within 30 days"
      ],
      "outcome": "Strengthened public service management and operational transparency"
    }
  },
    
  "Public Order and Safety": {
    "Lagos State Judiciary": {
      "kpis": [
        "Number of magistrate and commercial court buildings constructed or renovated annually",
        "Number of new judiciary staff recruited, documented, and onboarded",
        "Number of judiciary officers (Judges, Magistrates, Registrars) attending training, workshops, and conferences",
        "Number of disputes resolved via Alternative Dispute Resolution mechanisms",
        "Number of inmates released through legal review and decongestion initiatives",
        "Number of court divisions operational with e-Affidavit systems installed",
        "Number of High Court and Magisterial Divisions equipped with CCTV surveillance systems",
        "Number of official vehicles procured for Judges, Magistrates, and judiciary staff"
      ],
      "outcome": "Improved access to justice and judicial infrastructure efficiency"
    },
    "Ministry of Justice": {
      "kpis": [
        "Number of magistrate courts renovated to improve legal infrastructure",
        "Percentage of renovation work completed at the DNA forensic Centre",
        "Number of new Police Area Commands constructed for improved law enforcement",
        "Number of prison facilities constructed or renovated to improve inmate management"
      ],
      "outcome": "Strengthened legal infrastructure and law enforcement systems"
    },
    "Ministry of Special Duties and Intergovernmental Relations": {
      "kpis": [
        "Number of youths reached through anti-drug abuse sensitization campaigns across all LGAs",
        "Number of divisions in Lagos State sensitized on the National Population and Housing Census",
        "Number of strategic meetings mobilized for the DAWN (Development Agenda for Western Nigeria) programme",
        "Number of quarterly payments made for Command & Control Centre facility and mobile CCTV operations",
        "Number of quarterly payments for LASEMA emergency services (fleet, ambulances)",
        "Number of new fire stations or Rapid Intervention Vehicles established across Lagos",
        "Number of schools sensitized on safety protocols and fire response training",
        "Number of emergency rescue operations carried out to save lives and property",
        "Percentage increase in compliance with fire and safety standards across construction, hospitality, schools, etc.",
        "Number of Lagos youth sensitized on opportunities in the Nigerian Armed Forces and other paramilitary agencies",
        "Number of plant/rescue equipment sets procured for LASEMA and Fire Services"
      ],
      "outcome": "Enhanced emergency preparedness, public safety awareness, and disaster response capacity"
    }
  },

    "Recreation, Culture and Religion": {
        "Ministry of Home Affairs": {
            "kpis": [
                "Number of guests to attend the annual Christmas carol celebration",
                "Number of citizens to attend the National Independence Day celebration",
                "Number of attendees to participate in the Inter-Faith Parley",
                "Percentage of the invited civil servants to participate in the Annual Ramadan Tafsir",
                "Percentage of target civil servants to attend the breaking of fast during the Lenten period",
                "Number of mosques and churches to be renovated as part of religious site improvements",
                "Number of attendees expected for the Ramadan fast-breaking food distribution",
                "Number of food packs to be distributed for the Lenten fast-breaking among Christian civil servants",
                "Number of citizens to attend the Christian pilgrimage",
                "Number of citizens to participate in the Hajj operations"
            ],
            "outcome": "Promoted religious harmony and citizen engagement through faith-based events"
        },
        "Lagos State Sports Commission": {
            "kpis": [
                "Number of individuals expected to participate in community sports initiatives",
                "Percentage completion of the construction work on the stadia",
                "Number of athletes to participate in the grassroots sport competition",
                "Number of athletes to take part in the national youth games",
                "Number of runners expected to participate in the annual marathon",
                "Percentage completion of the Stadium upgrading project"
            ],
            "outcome": "Increased youth participation in sports and upgraded sports infrastructure"
        },
        "Ministry of Tourism, Arts, and Culture": {
            "kpis": [
                "Number of tourists to be attracted by the Symphony of Light event",
                "Number of tourists to attend the Greater Lagos event across multiple locations",
                "Percentage completion of the construction and fencing of the Alimosho Cultural Heritage Centre",
                "Percentage work completed on the redevelopment of the J. Randle Centre for Yoruba Culture and History",
                "Number of participants to attend the Eyo Festival",
                "Number of participants expected for the World Theatre Day celebrations",
                "Number of heritage sites and monuments to be monitored throughout the year",
                "Number of hospitality tourism establishments to be monitored for compliance with standards"
            ],
            "outcome": "Improved cultural visibility and enhanced tourism revenue"
        }
  },
  "Housing and Community Amenities": {
    "New Town Development Authority (NTDA)": {
      "kpis": [
        "% of road construction completed",
        "% of street lighting installation completed",
        "% of building construction completed"
      ],
      "outcome": "Improved urban infrastructure and development in new town areas"
    },
    "Lands Bureau": {
      "kpis": [
        "% of land acquisition process completed for areas around the train station",
        "% of compensation payments completed",
        "% of digitization process completed for automation of land processes",
        "% of perimeter fencing and signpost installation completed"
      ],
      "outcome": "Streamlined land administration and secured access to public land"
    },
    "Ministry of Physical Planning and Urban Development": {
      "kpis": [
        "% of development guide plans completed for Excised Villages",
        "% of Master Plan completed",
        "% of Model City Plan completed",
        "% of Action Area Plan completed"
      ],
      "outcome": "Enhanced spatial planning and sustainable urban development"
    },
    "Ministry of Housing": {
      "kpis": [
        "% of infrastructure work completed",
        "% of building construction completed"
      ],
      "outcome": "Increased access to quality public housing infrastructure"
    },
    "Office of the Surveyor General": {
      "kpis": [
        "Number of survey maps to be produced",
        "Number of public institutions to be surveyed",
        "Number of offices to be furnished with office equipment and furniture",
        "Number of offices to be supplied with computer hardware and office equipment",
        "Number of zonal offices to be provided with operational working tools",
        "Number of specialized operational equipment to be procured"
      ],
      "outcome": "Improved geospatial data management and institutional capacity"
    }
  },
  "Environmental Protection": {
    "Lagos State Parks and Garden Agency (LASPARK)": {
      "kpis": [
        "Total number of trees planted across all locations in Lagos State within the year",
        "Total number of parks and gardens maintained annually",
        "Total kilometres of public parks and school gardens rehabilitated by year-end",
        "Number of events and activities hosted in state parks annually",
        "Number of schools enhanced with landscaping and park features"
      ],
      "outcome": "Increased access to green spaces and environmental beautification across Lagos State"
    },
    "Office of Environmental Services": {
      "kpis": [
        "Number of public gardens surveyed for intensive maintenance in the year",
        "Total workshops conducted for environmental stakeholders statewide",
        "Number of LGAs and LCDAs reached through environmental advocacy initiatives",
        "Number of environmental impact assessments completed for infrastructure and development projects",
        "Total number of environmental education sessions held for youth audiences",
        "Number of awareness drives conducted in the 3 senatorial districts on sanitation and environmental protection",
        "Total number of community groups, NGOs, and stakeholders trained in sustainable environmental practices",
        "Number of trees tagged for ongoing growth and health monitoring",
        "Number of public schools with implemented waste sorting and recycling programs",
        "Total number of illegal dumpsites cleaned and restored"
      ],
      "outcome": "Strengthened environmental governance, advocacy, and education across communities"
    },
    "Office of Drainage Services": {
      "kpis": [
        "Total kilometres of new drainage channels built in flood-prone communities",
        "Total number of schools where flood control measures were executed",
        "Number of early warning and forecasting systems installed in high-risk zones",
        "Total number of failed or clogged drainage systems restored",
        "Number of LGAs assessed for flood risk mapping and vulnerability reporting"
      ],
      "outcome": "Improved flood resilience and drainage infrastructure in vulnerable communities"
    },
    "Lagos State Waste Management Authority (LAWMA)": {
      "kpis": [
        "Number of new gas-powered waste trucks added to the fleet",
        "Total number of unauthorized dumpsites eliminated from highways and public areas",
        "Number of MRFs and TLS facilities completed across the state",
        "Total volume (in tons) of waste collected across all streams within the year",
        "Total number of waste management and recycling campaigns conducted statewide",
        "Number of schools where waste segregation and recycling initiatives were deployed"
      ],
      "outcome": "Enhanced waste collection efficiency and recycling practices in Lagos State"
    }
  },
  "Social Protection": {
    "Ministry of Youth and Social Development": {
      "kpis": [
        "Number of parents supported through the Household Economy Strengthening Program annually",
        "Number of children rescued from abuse or destitution via emergency and destitute response operations",
        "Number of youths enrolled in state-supported vocational skill acquisition programs",
        "Number of children adopted through the Parenting for Adoption initiative",
        "Number of youths trained on mental health awareness, drug abuse prevention, and anti-crime sensitization",
        "Number of youth development centres upgraded with furnishings and functional equipment annually"
      ],
      "outcome": "Improved youth empowerment and child protection services in Lagos State"
    },
    "Ministry of Women Affairs and Poverty Alleviation (WAPA)": {
      "kpis": [
        "Number of individuals empowered through the Mega Empowerment Program and related poverty alleviation schemes",
        "Number of PLWHIV beneficiaries empowered through targeted support programs",
        "Number of individuals trained in short-term skills acquisition programs across LGAs",
        "Number of social welfare offices upgraded with functional equipment for enhanced service delivery",
        "Percentage of physical completion of the Caregivers Institute construction project",
        "Percentage of work completed on the construction of the WAPA Multi-purpose Centre",
        "Number of public toilet facilities renovated to improve sanitation access",
        "Number of government-owned shelter homes renovated for vulnerable population use",
        "Number of individuals supported through empowerment activities during the International Day celebration",
        "Number of individuals empowered during Humanitarian Day outreach events"
      ],
      "outcome": "Strengthened poverty alleviation and support systems for vulnerable groups"
    }
  },
  "Education": {
    "Ministry of Tertiary Education": {
      "kpis": [
        "% of public secondary schools rehabilitated and upgraded within the project timeline",
        "% of penultimate and final year students in state-owned tertiary institutions trained in career-building initiatives by the end of the training period",
        "% of youths in Lagos State trained in digital skills by the end of the project year"
      ],
      "outcome": "Improved quality and relevance of tertiary education and digital empowerment for youth"
    },
    "Ministry of Basic and Secondary Education": {
      "kpis": [
        "% of wall fences constructed in selected public secondary schools by the end of the project",
        "% of candidates included in the Child Guidance and Special School Project by the end of the academic year",
        "% of required science materials procured for the WASSCE examination",
        "% completion of the redesign and construction of an education complex",
        "% completion of the renovation and rehabilitation of the multilingual centre by the scheduled date",
        "% of candidates participating in the unified exam by the end of the registration period",
        "% payment of WASSCE fees for candidates before the deadline",
        "% completion of work in the construction of classroom blocks by the mid-project review",
        "% completion of work on the LMDGP classroom block by the project deadline",
        "% of SS3 candidates registered for the May/June WASSCE by the end of the registration period"
      ],
      "outcome": "Enhanced access to quality basic and secondary education across public schools"
    },
    "Special Committee on Rehabilitation of Public Schools": {
      "kpis": [
        "% of classroom blocks renovated at various primary and secondary schools in Lagos by the scheduled completion date",
        "% of units of dual single composite furniture fabricated and supplied to identified public primary schools by the end of the project",
        "% of emergency roof repairs completed on classroom blocks by the project’s close",
        "% completion of isolated toilet blocks at identified primary schools by the project’s deadline",
        "% of community primary schools rehabilitated, including classrooms and sanitation facilities, by the end of the quarter"
      ],
      "outcome": "Upgraded learning environments in public primary and secondary schools"
    }
  },
  "Health": {
    "Ministry of Health": {
      "kpis": [
        "Percentage of requested drugs and health commodities procured within the defined procurement cycle",
        "Number of patients diagnosed, treated, and dispensed with drugs using procured drugs and consumables within the fiscal year",
        "Number of sensitization programs successfully conducted, achieving a minimum of 75% participant engagement",
        "Completion rate of renovation works for health facilities and buildings within the approved project timeline",
        "Number of health facilities visited as per the scheduled quarterly assessment plan",
        "Number of water sampling sites visited for analysis as per the monthly surveillance schedule",
        "Number of illegal outlets sealed during surveillance within the specified reporting period",
        "Percentage of school-aged children participating in Mass Administration of Medicines, reaching a minimum of 80% coverage annually",
        "Response rate to disease outbreaks within 24-48 hours of detection as per the outbreak management plan",
        "Percentage of highly infectious diseases diagnosed within 24-48 hours by trained staff, ensuring early intervention",
        "Percentage of scheduled maintenance conducted for biosafety equipment within the defined annual schedule",
        "Percentage of the target population screened and treated for eye-related conditions annually, aiming for at least 70% coverage",
        "Percentage of identified patients who receive mental health services within one month of diagnosis",
        "Attendance rate at training sessions for healthcare staff, ensuring a minimum of 90% participation rate",
        "Percentage of funding requests processed within 30 days of receipt to ensure timely disbursement",
        "Number of women screened for breast and cervical cancer, achieving at least 80% of the annual target",
        "Number of newborns screened for sickle cell disorder within the first 6 weeks of birth annually",
        "Number of planned monthly outreach sessions on viral hepatitis conducted, with 100% adherence to the annual plan",
        "Number of targeted tuberculosis cases reached through active case finding, meeting annual targets",
        "Number of confirmed malaria cases treated with Artemisinin-based Combination Therapy (ACTs), reaching 90% treatment compliance",
        "Number of BCC and IEC materials produced and distributed in alignment with the health communication strategy, aiming for 100% distribution",
        "Percentage of individuals receiving Antiretroviral treatment (ART) with viral suppression, aiming for 95% viral load suppression",
        "Percentage of healthcare workers trained on Integrated Management of Childhood Illnesses (IMCI) annually, targeting 100% of the workforce",
        "Number of targeted individuals reached with nutrition interventions, meeting at least 80% of the annual target",
        "Number of public health facilities equipped with lifesaving drugs for child and newborn care, ensuring 100% coverage",
        "Number of Youth Friendly Centers (YFC) and Youth Medical Centers (YMC) operational by the end of the year, ensuring 100% functional status",
        "Number of students screened for health conditions annually, aiming for 90% coverage across all schools",
        "Number of corpses removed from healthcare facilities, ensuring adherence to national health facility protocols",
        "Percentage of medical health officers equipped with Personal Protective Equipment (PPEs) within 30 days of assignment",
        "Number of workplaces and food houses inspected for compliance with safety policies, aiming for 100% annual inspection",
        "Percentage of the workforce successfully screened for health-related materials and services annually, aiming for 95% coverage",
        "Availability of essential medical equipment, ensuring timely procurement and deployment within the approved procurement cycle",
        "Number of functional ambulance vehicles ensuring timely response within 30 minutes, with 100% operational status",
        "Percentage of data managers trained on data quality and management techniques annually, aiming for 100% training completion",
        "Percentage of activities outlined in the Digital Health strategic plan implemented within the annual operational plan",
        "Number of grant proposals submitted to partners and donors, achieving at least 75% of the annual target",
        "Percentage of performance management reports submitted within the deadline as per the reporting schedule",
        "Utilization rate of the research coordination and promotion plan, aiming for 90% utilization annually",
        "Percentage of reports submitted on schedule according to the health policy development plan, ensuring 100% on-time submission",
        "Percentage of healthcare facilities utilizing quality guidelines and documents, aiming for 100% implementation within the year",
        "Percentage of health facilities operationalizing Strategic Service Improvement Plans (SIPs), ensuring 80% completion by year-end",
        "Percentage completion rate of new secondary health facility renovations or construction, targeting 100% completion by year-end",
        "Percentage completion of ongoing secondary health facility renovations or construction, achieving 90% progress by the end of the year",
        "Percentage reduction of outstanding liabilities related to health projects, aiming for a 50% reduction within the fiscal year",
        "Completion rate of operational research reports, ensuring 100% completion within the annual reporting period",
        "Percentage of midwives who received supportive supervision visits, ensuring 100% supervision within the year",
        "Percentage increase in HIV knowledge retention post-campaign, aiming for a 20% improvement"
      ],
      "outcome": "Improved access to quality healthcare services, disease prevention, and health infrastructure"
    }
  },
  "Recreation, Culture, and Religion": {
    "Ministry of Home Affairs": {
      "kpis": [
        "Number of guests to attend the annual Christmas carol celebration",
        "Number of citizens to attend the National Independence Day celebration",
        "Number of attendees to participate in the Inter-Faith Parley",
        "Percentage of the invited civil servants to participate in the Annual Ramadan Tafsir",
        "Percentage of target civil servants to attend the breaking of fast during the Lenten period",
        "Number of mosques and churches to be renovated as part of religious site improvements",
        "Number of attendees expected for the Ramadan fast-breaking food distribution",
        "Number of food packs to be distributed for the Lenten fast-breaking among Christian civil servants",
        "Number of citizens to attend the Christian pilgrimage",
        "Number of citizens to participate in the Hajj operations"
      ],
      "outcome": "Fostered religious harmony, cultural inclusion, and spiritual engagement among citizens"
    },
    "Lagos State Sports Commission": {
      "kpis": [
        "Number of individuals expected to participate in community sports initiatives",
        "Percentage completion of the construction work on the stadia",
        "Number of athletes to participate in the grassroots sport competition",
        "Number of athletes to take part in the national youth games",
        "Number of runners expected to participate in the annual marathon",
        "Percentage completion of the Stadium upgrading project"
      ],
      "outcome": "Increased grassroots participation in sports and enhanced sports infrastructure across Lagos"
    },
    "Ministry of Tourism, Arts, and Culture": {
      "kpis": [
        "Number of tourists to be attracted by the Symphony of Light event",
        "Number of tourists to attend the Greater Lagos event across multiple locations",
        "Percentage completion of the construction and fencing of the Alimosho Cultural Heritage Centre",
        "Percentage work completed on the redevelopment of the J. Randle Centre for Yoruba Culture and History",
        "Number of participants to attend the Eyo Festival",
        "Number of participants expected for the World Theatre Day celebrations",
        "Number of heritage sites and monuments to be monitored throughout the year",
        "Number of hospitality tourism establishments to be monitored for compliance with standards"
      ],
      "outcome": "Promoted tourism, preserved cultural heritage, and supported the creative economy in Lagos"
     }
  }
}

# Header function
def header():
    st.title("📊 Government Programme/Project KPI Directory")
    st.markdown("Use this tool to generate SMART KPIs for various government projects.")

# Display header
header()

# Sector selection
sector = st.selectbox("Select Government Sector (COFOG)", list(kpi_directory.keys()))

if sector:
    mda_list = list(kpi_directory[sector].keys())
    mda = st.selectbox("Select MDA:", mda_list)

    if mda:
        st.subheader(f"Output KPIs for {mda}")
        for kpi in kpi_directory[sector][mda]["kpis"]:
            st.write(f"- {kpi}")

        st.subheader("Outcome Statement")
        st.success(kpi_directory[sector][mda]["outcome"])