import streamlit as st
import pandas as pd
import json
import requests


if "job_titles" not in st.session_state:
    st.session_state["job_titles"] = []
if "job_levels" not in st.session_state:
    st.session_state["job_levels"] = []
if "job_title_inputs" not in st.session_state:
    st.session_state["job_title_inputs"] = [""]
if "job_level_inputs" not in st.session_state:
    st.session_state["job_level_inputs"] = [""]


# Title of the app
st.title("Template Mapper")

# File upload for PMG template and client template
st.subheader("Upload Templates")
pmg_file = st.file_uploader("Upload PMG Template CSV", type=["csv"], key="pmg_template")
client_file = st.file_uploader("Upload Client Template CSV", type=["csv"], key="client_template")

vendor_workflow = st.checkbox("Is this the Vendor Workflow?", value=False)

# Load CSVs as DataFrames
if pmg_file and client_file:
    pmg_df = pd.read_csv(pmg_file)
    client_df = pd.read_csv(client_file)
    
    st.subheader("Map Columns")
    column_mappings = []
    
    # Column Mapping Section
    # Column Mapping Section
    for pmg_col in pmg_df.columns:
        if pmg_col in pmg_df.columns:  # Only proceed if PMG column exists
            selected_col = st.selectbox(f"Map '{pmg_col}' to:", [pmg_col] + list(client_df.columns), key=pmg_col)
            # Create a mapping entry only if the column is changed, otherwise retain original
            mapping = {"pmg_column": pmg_col, "client_column": selected_col}
            column_mappings.append(mapping)
        else:
            st.warning(f"'{pmg_col}' does not exist in the PMG Template and will be retained as is.")
    
    
    st.write("Mapped Columns:", column_mappings)
    
    # Display a button to finalize mappings
    if st.button("Finalize Mapping"):
        st.session_state["column_mappings"] = column_mappings
        st.success("Column mapping saved.")

# Section for Expected Job Titles
st.subheader("Add Expected Job Titles")
job_titles_bulk_input = st.text_area("Job Titles Bulk Input", value="\n".join(st.session_state.get("job_title_inputs", [])))

if st.button("Confirm Expected Job Titles"):
    st.session_state["job_title_inputs"] = [title.strip() for title in job_titles_bulk_input.split("\n") if title.strip()]
    st.session_state["job_titles"] = st.session_state["job_title_inputs"]
    st.success("Expected job titles saved!")

# Display all saved job titles
if st.session_state.get("job_titles"):
    st.write("Saved Expected Job Titles:")
    for idx, title in enumerate(st.session_state["job_titles"]):
        st.write(f"{idx + 1}. {title}")

# Section for Expected Job Levels
st.subheader("Add Expected Job Levels")
job_levels_bulk_input = st.text_area("Job Levels Bulk Input", value="\n".join(st.session_state.get("job_level_inputs", [])))

if st.button("Confirm Expected Job Levels"):
    st.session_state["job_level_inputs"] = [level.strip() for level in job_levels_bulk_input.split("\n") if level.strip()]
    st.session_state["job_levels"] = st.session_state["job_level_inputs"]
    st.success("Expected job levels saved!")

# Display all saved job levels
if st.session_state.get("job_levels"):
    st.write("Saved Expected Job Levels:")
    for idx, level in enumerate(st.session_state["job_levels"]):
        st.write(f"{idx + 1}. {level}")

# Optional: Process and Display the Final Data
if st.button("Submit"):
    # Final column mappings
    column_mappings = st.session_state.get("column_mappings", {})
    expected_job_titles = st.session_state.get("job_titles", [])
    expected_job_levels = st.session_state.get("job_levels", [])

    # Prepare data for API request
    data = {
        "expected_job_titles": json.dumps(expected_job_titles),
        "expected_job_levels": json.dumps(expected_job_levels),
        "vendorWorkflow": vendor_workflow,  # Checkbox determines this value
        "columnHeaders": json.dumps(column_mappings)
    }
    st.write("Data to be submitted:", data)
    # Send API request with PMG Template CSV file
    pmg_file.seek(0)  # Reset file pointer to the beginning
    files = {"file": ("pmg_template.csv", pmg_file, "text/csv")}
    url = "https://pmg-360-api-232752599914.us-central1.run.app/api/qc_workflow/process"

    response = requests.post(url, files=files, data=data)
    
    # Display API response
    if response.status_code == 200:
        st.success("Data submitted successfully!")
        df = pd.read_csv(response.json().get('file_url'))
        st.dataframe(df)
    else:
        st.error(f"Error {response.status_code}: Unable to submit data.")
        st.write("Response:", response.text)
