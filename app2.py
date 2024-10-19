from dotenv import load_dotenv

load_dotenv()
#dotenv: This library loads environment variables from a .env file into the system's environment variables.
#load_dotenv(): This function reads the .env file and sets the environment variables.

import base64
import io
import streamlit as st
import os
from PIL import Image
import pdf2image
# base64: This library is used to encode and decode data in base64 format.
# io: This module provides the Python interfaces to stream handling.
# streamlit: A library for creating web apps with minimal code.
# os: Provides functions for interacting with the operating system.
# PIL (Python Imaging Library): Used for image processing.
# pdf2image: A library to convert PDF documents into images.
#----
# google.generativeai: This is the Google Generative AI library.
# genai.configure: This function configures the API key for accessing the Google Generative AI services. 
# The API key is retrieved from environment variables using os.getenv("GOOGLE_API_KEY").

import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(input, pdf_content, prompt):
    #This function interacts with the Gemini 1.5 model.
    #Initialize the model
    model=genai.GenerativeModel('gemini-1.5-flash')
    #This calls the model to generate content based on the provided input.
    response=model.generate_content([input, pdf_content[0], prompt])
    #Returns the generated text response from the model.
    return response.text

#function to handle the PDF upload
def input_pdf_setup(uploaded_file):
    #If people already uplodeaded the file 
    if uploaded_file is not None:
        #Convert PDF --> image
        #Convert the PDF file to list of images
        images = pdf2image.convert_from_bytes(uploaded_file.read())
        #take first page of images
        first_page = images[0] 

        #Convert to bytes
        #Creates a bytes buffer to hold the image.
        img_byte_arr = io.BytesIO()
        # Saves the image to the bytes buffer in JPEG format.
        first_page.save(img_byte_arr, format='JPEG')
        #Convert the image to bytes
        img_byte_arr = img_byte_arr.getvalue()

        #Prepares the PDF content for the model by including the MIME type and encoded data.
        pdf_parts = [
            {
            "mime_type":"image/jpeg",
            # Encodes the image data in base64 format.
            "data": base64.b64encode(img_byte_arr).decode()
            }
        ]
        #return the processed PDF content
        return pdf_parts
    else:
        raise FileNotFoundError("No file uploaded")
    
#Streamlit App
#Set up page title
st.set_page_config(page_title="ATS Resume ExPeRt")
#Adds header to the Streamlit app
st.header("ATS Tracking System")
#Creates a text area for the user to input the job description.
input_text=st.text_area("Job Description: ", key="input")
#Allows user to upload a PDF file
uploaded_file=st.file_uploader("Upload your resume (PDF)",type="pdf")

if uploaded_file is not None:
    st.write("PDF Uploaded Successfully")

submit1 = st.button("Tell me about the resume")

# submit2 = st.button("How can I improve my skills") - same as prompt1 (?)

submit3 = st.button("Percentage match")

input_prompt1 = """
 You are an experienced Technical Human Resource Manager in the field of Data Science or Full Stack Web development or Big Data Engineering or Devops or Data Analyst ,your task is to review the provided resume against any job description. 
  Please share your professional evaluation on whether the candidate's profile aligns with the role. 
 Highlight the strengths and weaknesses of the applicant in relation to the specified job requirements.
"""


input_prompt3 = """
You are an skilled ATS (Applicant Tracking System) scanner with a deep understanding of any one job role in the field of Data Science or Full Stack Web development or Big Data Engineering or Devops or Data Analyst, 
your task is to evaluate the resume against the provided job description. give me the percentage of match if the resume matches
the job description. First the output should come as percentage and then keywords missing and last final thoughts.
"""
#rpcessing user request
if submit1: #check if the button is pressed
    if uploaded_file is not None:
        #process the pdf file
        pdf_content=input_pdf_setup(uploaded_file)
        #get response from the model
        response=get_gemini_response(input_prompt1,pdf_content,input_text) #what's need to be done + pdf content + input (JD)
        #display the response
        st.subheader("The Repsonse is")
        st.write(response)
    else:
        st.write("Please upload the resume")

elif submit3:
    if uploaded_file is not None:
        pdf_content=input_pdf_setup(uploaded_file)
        response=get_gemini_response(input_prompt3,pdf_content,input_text)
        st.subheader("The Repsonse is")
        st.write(response)
    else:
        st.write("Please upload the resume")





