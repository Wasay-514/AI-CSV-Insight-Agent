# import os
# import pandas as pd
# import streamlit as st
# from dotenv import load_dotenv
# from openai import OpenAI

# load_dotenv()
# client = OpenAI(api_key=os.getenv("GEMINI_API_KEY"))

# st.title("AI CSV Insight Agent")

# uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

# if uploaded_file:
#     df = pd.read_csv(uploaded_file)

#     st.subheader("Dataset Preview")
#     st.dataframe(df.head())

#     st.subheader("Basic Info")
#     st.write("Rows:", df.shape[0])
#     st.write("Columns:", df.shape[1])
#     st.write("Column Names:", list(df.columns))

#     missing_values = df.isnull().sum().to_string()
#     summary = df.describe(include="all").to_string()

#     if st.button("Generate AI Insights"):
#         prompt = f"""
#         You are a data analyst agent.

#         Analyze this dataset summary and missing values.

#         Dataset shape:
#         Rows: {df.shape[0]}
#         Columns: {df.shape[1]}

#         Missing values:
#         {missing_values}

#         Summary:
#         {summary}

#         Give:
#         1. Simple dataset explanation
#         2. Missing value issues
#         3. 5 useful insights
#         4. Suggested KPIs
#         5. Power BI dashboard ideas

#         Keep answer beginner-friendly.
#         """

#         # response = client.responses.create(
#         #     # model="gpt-5"
#         #     model="gpt-4.1-mini",
#         #     input=prompt
#         # )

#         # st.subheader("AI Insights")
#         # st.write(response.output_text)
        
#         import google.generativeai as genai
#         import os
#         genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
#         model = genai.GenerativeModel("gemini-1.5-flash")
#         response = model.generate_content(prompt)
#         result = response.text




import os
import pandas as pd
import streamlit as st
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=GEMINI_API_KEY)

st.title("AI CSV Insight Agent")

uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    st.subheader("Dataset Preview")
    st.dataframe(df.head())

    st.subheader("Basic Info")
    st.write("Rows:", df.shape[0])
    st.write("Columns:", df.shape[1])
    st.write("Column Names:", list(df.columns))

    missing_values = df.isnull().sum().to_string()
    summary = df.describe(include="all").to_string()

    if st.button("Generate AI Insights"):
        if not GEMINI_API_KEY:
            st.error("GEMINI_API_KEY not found. Please add it in .env file.")
        else:
            prompt = f"""
You are a professional data analyst agent.

Analyze this dataset:

Rows: {df.shape[0]}
Columns: {df.shape[1]}

Column Names:
{list(df.columns)}

Missing Values:
{missing_values}

Dataset Summary:
{summary}

Give output in this format:

1. Dataset Overview
2. Missing Values Analysis
3. 5 Key Insights
4. Suggested KPIs
5. Power BI Dashboard Ideas
6. Business Recommendations

Keep the explanation beginner-friendly.
"""

            model = genai.GenerativeModel("gemini-flash-latest")
            response = model.generate_content(prompt)

            st.subheader("AI Insights")
            st.write(response.text)