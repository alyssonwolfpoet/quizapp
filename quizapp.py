import streamlit as st
import json
import os
from dotenv import load_dotenv

from openai import OpenAI

OpenAI.api_key=os.getenv("OPENAΙ_ΑΡΙ_ΚΕΥ")

client = OpenAI()

def fetch_questions(text_content, quiz_level):
    RESPONSE_JSON = {
        "mcqs": [
            {
                "mcq": "multiple choice question1",
                "options": {
                    "a": "choice here1",
                    "b": "choice here2",
                    "c": "choice here3",
                    "d": "choice here4"
                },
                "correct": "correct choice option"
            },
            {
                "mcq": "multiple choice question2",
                "options": {
                    "a": "choice here",
                    "b": "choice here",
                    "c": "choice here",
                    "d": "choice here"
                },
                "correct": "correct choice option"
            },
            {
                "mcq": "multiple choice question3",
                "options": {
                    "a": "choice here",
                    "b": "choice here",
                    "c": "choice here",
                    "d": "choice here"
                },
                "correct": "correct choice option"
            }
        ]
    }

    
    PROMPT_TEMPLATE= """
    Text: {text_content}
    You are an expert in generating MCQ type quiz on the basis of provided content.
    Given the above text, create a quiz of 3 multiple choice questions keeping difficulty level as {quiz_level}.
    Make sure the questions are not repeated and check all the questions to be conforming the text as well.
    Make sure to format your response like RESPONSE_JSON below and use it as a guide.
    Ensure to make an array of 3 MCQs referring the following response json.
    Here is the RESPONSE_JSON:

    {RESPONSE_JSON}
        
    """
    
    formtted_template = PROMPT_TEMPLATE.format(text_content=text_content, quiz_level=quiz_level,RESPONSE_JSON = RESPONSE_JSON)
    
    response = client.chat.completions.create(model="gpt-3.5-turbo",
                                              messages=[{
                                                  "role": "user",
                                                  "content": formtted_template
                                              }],
                                              temperature=0.3,
                                              max_tokens=1000,
                                              top_p=1,
                                              frequency_penalty=0,
                                              presence_penalty=0
                                              )