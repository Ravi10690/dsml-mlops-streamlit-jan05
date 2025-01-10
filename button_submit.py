import streamlit as st




# Selection page
def selection_page():
    st.title("Options Selection")

    # Checkbox options
    st.header("Checkbox Options")
    st.session_state.option1 = st.checkbox("Option 1")
    st.session_state.option2 = st.checkbox("Option 2")
    st.session_state.option3 = st.checkbox("Option 3")

    # Radio button options
    st.header("Radio Button Options")
    st.session_state.option4 = st.radio("Select an option:", ("Option A", "Option B", "Option C"))

    # Submit button
    if st.button("Submit"):
        # Navigate to the results page
        st.session_state.page = "results"
# Remove the line causing the error

# Results page
def results_page():
    st.title("Results")

    # Display selected options
    st.write("Checkbox Options:")
    if st.session_state.option1:
        st.write("- Option 1")
    if st.session_state.option2:
        st.write("- Option 2")
    if st.session_state.option3:
        st.write("- Option 3")

    st.write("Radio Button Option:")
    st.write(f"- {st.session_state.option4}")

    # Back button to return to selection page
    if st.button("Go Back"):
        st.session_state.page = "selection"
        #st.experimental_rerun()



# Set up session state for page navigation
if "page" not in st.session_state:
	st.session_state.page = "selection"  # Default to the selection page

# Page routing
if st.session_state.page == "selection":
	selection_page()
elif st.session_state.page == "results":
	results_page()
