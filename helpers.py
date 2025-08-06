import os, re, pandas as pd
import json
from pypdf import PdfReader
from dotenv import load_dotenv, find_dotenv
from langchain.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv(find_dotenv())
google_api_key = os.getenv("GOOGLE_API_KEY")

# Extract text from PDF
def get_pdf_text(pdf_doc):
    text = ""
    pdf_reader = PdfReader(pdf_doc)
    for page in pdf_reader.pages:
        text += page.extract_text() + "\n"
    return text
        
# Extract data from text
def extracted_data(pages_data):
    print(pages_data)
    template = """Extract the following data, Remove any currency symbols
    INVOICE ID, DESCRIPTION, AMOUNT, DATE, DUE DATE, BILL FOR, and TERMS 
    from the text:{pages}
    
    
    in the following format:
    {{"Invoice ID": 12345, "Description": "Service provided", "Amount": 1000, "Date": "2023-01-01", "Due Date": "2023-02-01", "Bill For": "Client Name", "Terms": "Pay this now"}}"""
    
    prompt_template = PromptTemplate(input_variables=["pages"], template=template)
    llm = ChatGoogleGenerativeAI(model="models/gemini-1.5-flash", temperature=0.0)
    full_response = llm.invoke(prompt_template.format(pages=pages_data))
    print(full_response)
    return full_response

# Create documents from the uploaded pdf files
def create_docs(user_pdf_list):
    df = pd.DataFrame(
        {
            "Invoice ID": pd.Series(dtype="int"),
            "Description": pd.Series(dtype="str"),
            "Amount": pd.Series(dtype="float"),
            "Date": pd.Series(dtype="datetime64[ns]"),
            "Due Date": pd.Series(dtype="datetime64[ns]"),
            "Bill For": pd.Series(dtype="str"),
            "Terms": pd.Series(dtype="str"),
        }
    )
    
    for filename in user_pdf_list:
        print(f"Processing {filename}")
        raw_data = get_pdf_text(filename)
        llm_extracted_data = extracted_data(raw_data)
        
        # Extract text from AIMessage if needed
        if hasattr(llm_extracted_data, "content"):
            llm_extracted_data = llm_extracted_data.content

        pattern = r'{(.+)}'
        if llm_extracted_data is not None:
            match = re.search(pattern, llm_extracted_data, re.DOTALL)
        else:
            match = None
        if match:
            extracted_text = "{" + match.group(1) + "}"
            try:
                data_dict = json.loads(extracted_text.replace("null", "null"))
            except json.JSONDecodeError:
                # Try to fix common issues (e.g., single quotes, trailing commas)
                fixed_text = extracted_text.replace("'", '"').replace(",}", "}").replace("null", "null")
                data_dict = json.loads(fixed_text)
            print(data_dict)
        else:
            print("No match found in the extracted data.")
            continue
            continue
    
        df = pd.concat([df, pd.DataFrame([data_dict])], ignore_index=True)
        
        print("Data extracted and added to DataFrame.")
        
    return df