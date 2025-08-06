# AI-Powered Bill Extractor

This project is an AI-powered bill extraction tool that leverages the capabilities of Google's Gemini Pro model to parse and extract relevant information from PDF bills. The application is built with Python and features a user-friendly web interface created using Streamlit.

## Features

*   **PDF Bill Upload**: Users can upload multiple PDF bills simultaneously.
*   **AI-Powered Data Extraction**: Utilizes Google's Gemini Pro to intelligently extract key information from the bills, including:
    *   Invoice ID
    *   Description
    *   Amount
    *   Date
    *   Due Date
    *   Billed To
    *   Payment Terms
*   **Structured Data Output**: Displays the extracted data in a clean, tabular format using a Pandas DataFrame.
*   **CSV Export**: Allows users to download the extracted bill data as a CSV file for easy integration with other systems or for record-keeping.
*   **User-Friendly Interface**: A simple and intuitive web interface built with Streamlit for a seamless user experience.

## How to Use

1.  **Upload Bills**: Click on the "Upload your bills in PDF format" button to select one or more PDF bill files from your local machine.
2.  **Extract Data**: Once the files are uploaded, click the "Extract bill data..." button to initiate the extraction process.
3.  **View and Download**: The extracted data will be displayed in a table on the web page. You can then click the "Download data as CSV" button to save the information to your computer.

## Getting Started

### Prerequisites

*   Python 3.7+
*   An environment with the required Python packages installed.
*   A Google API key with access to the Gemini Pro model.

### Installation

1.  **Clone the repository**:
    ```bash
    git clone https://github.com/tiwarikartik/bill-extractor.git
    cd bill-extractor
    ```

2.  **Create a virtual environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install the required packages**:
    ```bash
    pip install -r requirements.txt
    ```

4.  **Set up your environment variables**:
    *   Create a `.env` file in the root directory of the project.
    *   Add your Google API key to the `.env` file:
        ```
        GOOGLE_API_KEY="your-google-api-key"
        ```

5.  **Run the Streamlit application**:
    ```bash
    streamlit run main.py
    ```

## Technologies Used

*   **Python**: The core programming language for the application.
*   **Streamlit**: For building the interactive web user interface.
*   **Pandas**: For data manipulation and creating the DataFrame.
*   **PyPDF2**: For extracting text from the uploaded PDF files.
*   **Google Generative AI (Gemini Pro)**: The large language model used for intelligent data extraction.
*   **LangChain**: To streamline the interaction with the language model.
*   **Dotenv**: For managing environment variables.

## Contributing

Contributions to this project are welcome! Please feel free to fork the repository, make your changes, and submit a pull request.
