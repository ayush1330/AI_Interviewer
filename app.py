# app.py

import streamlit as st
from ui import show_home_page, show_resume_upload_page, show_interview_page
from agents.orchestration_agent import OrchestrationAgent


def main():
    st.set_page_config(page_title="AI Interviewer", page_icon=":briefcase:")

    # Initialize session state
    if "page" not in st.session_state:
        st.session_state["page"] = "home"

    # Create an instance of the orchestration agent
    orchestration_agent = OrchestrationAgent()

    # Navigation logic
    if st.session_state["page"] == "home":
        show_home_page()
    elif st.session_state["page"] == "upload_resume":
        show_resume_upload_page()
    elif st.session_state["page"] == "interview":
        show_interview_page(orchestration_agent)
    else:
        st.error("Unknown page")


if __name__ == "__main__":
    main()
