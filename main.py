import pandas as pd
import streamlit as st

from xml_conversion import export_xml

# Set page configuration
st.set_page_config(page_title="Calvin ArmyIgnite Conversion", page_icon=":file_folder:", layout="wide")

st.title("Calvin ArmyIgnite Conversion")

# Initialize export_file variable to store the converted XML data
export_file = ''

# File uploader for CSV files
# The uploaded file is read into a DataFrame, displayed, and then converted to XML format.
# If any errors occur during the file reading or conversion process, an error message is displayed.
uploaded_file = st.file_uploader("Upload CSV File", type=["csv"])
if uploaded_file is not None:
    try:
        csv_df = pd.read_csv(
            uploaded_file, encoding="utf-8", encoding_errors="ignore"
        )
        st.write(csv_df)

        export_file = export_xml(csv_df.values.tolist())
        st.success("CSV file has been converted to XML format")
        st.metric("Total Rows Converted", len(csv_df))

    except Exception as err:
        st.error(err)

# If a file has been uploaded and successfully converted, a download button is displayed to allow the user to download the XML file.
# The download button is only shown if both the uploaded file and the export file are available.
if uploaded_file is not None and export_file:
    st.divider()

    st.info("You can download the XML file using the button below")
    st.download_button(
        "Download File", data=export_file, file_name="xml_export.xml", mime="text/xml"
    )
