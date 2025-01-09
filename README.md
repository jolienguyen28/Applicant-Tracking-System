# ATS Resume ExPeRt

ATS Resume ExPeRt is a Streamlit-based application that leverages Google’s generative AI API to evaluate resumes against job descriptions. The tool allows users to upload a resume (PDF format) and provides feedback on the resume's alignment with specified job roles. This feedback includes an overall percentage match and a professional evaluation. Demo video: https://drive.google.com/file/d/1bn1jkH2dVbOuh8MuA-8FVjBIhS4iQWBC/view?usp=sharing

## Features

- **PDF Conversion**: Converts the first page of an uploaded resume PDF into an image for processing.
- **AI-Powered Evaluation**: Uses Google's generative AI to provide insights and matching scores for resumes based on job descriptions.
- **Streamlit Interface**: Provides an interactive and user-friendly interface for resume analysis.

## Requirements

- **Python 3.8+**
- **Google Generative AI API Key**
- **Streamlit**: Web application framework
- **Pillow**: Image processing library
- **pdf2image**: PDF to image conversion
- **dotenv**: Environment variable management

## Setup

1. **Clone the repository**:

   ```bash
   git clone <repository_url>
   cd <repository_name>
   ```

2. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**:
   - Create a `.env` file in the root directory and add your Google Generative AI API key:
     ```plaintext
     GOOGLE_API_KEY=your_api_key_here
     ```

4. **Run the application**:

   ```bash
   streamlit run <your_script_name>.py
   ```

## Usage

1. **Open the App**: Go to the URL provided by Streamlit in your terminal.
2. **Enter Job Description**: Type or paste the job description in the text area.
3. **Upload Resume**: Upload a resume in PDF format.
4. **Analyze**:
   - **Professional Evaluation**: Click "Tell me about the resume" to get detailed insights.
   - **Percentage Match**: Click "Percentage match" to see a percentage score, keywords missing, and final thoughts.

## Key Components

- **Generative AI Setup**: Configures Google's generative AI with API keys from environment variables.
- **PDF Conversion**: Converts the uploaded PDF’s first page to a base64 JPEG image.
- **Prompts for AI Evaluation**: 
  - `input_prompt1`: Provides a professional evaluation of the resume's alignment with the job description.
  - `input_prompt2`: Calculates a percentage match, highlights missing keywords, and provides final insights.

## Code Structure

```plaintext
├── .env                 # Contains API key for Google Generative AI
├── main.py              # Main script for running Streamlit app
├── requirements.txt     # Python package dependencies
```

## License

This project is licensed under the MIT License.
