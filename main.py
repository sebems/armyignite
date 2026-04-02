import streamlit as st
import pandas as pd

from xml_conversion import export_xml

st.title("Calvin CSV to XML Conversion")

export_file = ''

uploaded_file = st.file_uploader("Upload CSV File", type="csv")
if uploaded_file is not None:
    match uploaded_file.type:
        case "text/csv":
            try:
                csv_df = pd.read_csv(
                    uploaded_file, encoding="ascii", encoding_errors="ignore"
                )
                st.write(csv_df)

                export_file = export_xml(csv_df.values.tolist())
            except Exception as err:
                st.error(type(err))  # the exception type
                st.error(err.args)  # arguments stored in .args
                st.error(err)

            st.success("CSV file has been converted to XML format")
        case _:
            st.error("File given is not a CSV: ", uploaded_file.type)
            # redundant since file_uploader only takes files of csv

st.divider()


st.download_button(
    "Download File", data=export_file, file_name="xml_export.xml", mime="text/xml"
)
