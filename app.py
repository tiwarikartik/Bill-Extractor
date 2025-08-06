import streamlit as st
from helpers import create_docs

def main():
    st.set_page_config(page_title="Bill Extractor", page_icon=":money_with_wings:", layout="centered")
    st.title("Bill Extractor AI Assistant")
    
    pdf_files = st.file_uploader("Upload your bills in PDF format", type=["pdf"], accept_multiple_files=True)
    extract_button = st.button("Extract bill data...")
    
    if extract_button:
        with st.spinner("Extracting..."):
            data_frame = create_docs(pdf_files)
            st.write(data_frame)
            
            convert_to_csv = data_frame.to_csv(index=False).encode("utf-8")
            st.download_button("Download data as CSV", convert_to_csv, "CSV_Bills.csv", "text/csv", key="download-csv")
    
    st.success("Success!!!")
    pass

if __name__ == "__main__":
    main()