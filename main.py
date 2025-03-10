import streamlit as st
import warnings
from crewai import Agent, Task, Crew
import os
import numpy as np
import os
import pandas as pd
import requests
from dotenv import load_dotenv

warnings.filterwarnings('ignore')
st.set_page_config(page_title="AI-Driven Company Research", layout="wide")

# Load API keys
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_MODEL_NAME"] = 'gpt-3.5-turbo'



def create_agents(company):
    Research_agent = Agent(
        role="Industry & Company Researcher",
        goal=f"Research about the {company} and which industry it belongs to.",
        backstory=f"Determine the industry the {company} operates"
                  f"Classify the {company} into appropriate sub-sectors if applicable.",
        allow_delegation=False,
        verbose=True
    )
    usecase_agent = Agent(
        role="Use Case Generator",
        goal=f"To identify AI, ML, and automation opportunities within the {company} industry and operations.",
        backstory=f" You are conducting an industry analysis to identify AI, ML, and automation opportunities within a {company} sector"
                  f"You base your research on industry trends, competitor benchmarks, and {company}-specific insights."
                  f"You provide objective findings on industry standards and highlight potential AI-driven improvements"
                  f"Clearly distinguishing between data-driven insights and strategic recommendations.",  
        allow_delegation=False,
        verbose=True
    )
    resource_agent = Agent(
        role="Resource Asset Collector",
        goal=f"Identify and propose AI-driven solutions that enhance the {company}'s data utilization and improve decision-making while systematically storing collected datasets in an organized text or markdown file for seamless retrieval and further research.",
        backstory=f"You are conducting a structured search to find high-quality datasets that align with the {company}'s AI/ML use cases."
                  f"Your focus is on publicly available sources such as Kaggle, Hugging Face, and GitHub."
                  f"Once the relevant datasets are identified, they must be systematically stored in a structured file, including dataset descriptions, source links, and their relevance to specific AI/ML applications for easy access and retrieval"
                  f"You now explore potential GenAI solutions that leverage these datasets"
                  f"Your focus is on use cases such as document search, automated report generation, and AI-powered chat systems.",    
        allow_delegation=False,
        verbose=True
    )
    

    return Research_agent,usecase_agent,resource_agent


def create_tasks(company, Research_agent,usecase_agent,resource_agent):
    search = Task(
        description= 
                  f"1. Determine the industry the {company} operates"
                  f"2 .Classify the {company} into appropriate sub-sectors if applicable."
                  f"3.Identify the {company} main products, services, and solutions."
                  f"4. Analyze {company} strategic focus areas"
                  f"5.Extract the {company} vision and mission statement"
                  f"6.Gather information on {company} product portfolio and major innovations."
                  f"7.Identify any unique differentiators in {company} industry",
        expected_output=f"Detailed report on {company} industry, key offerings, and strategy.",
        output_file="company_research.txt",
        agent=Research_agent,
    )

    usecase = Task(
        description=f"1. Conduct research on industry trends related to AI, ML, and automation.."
                    f"2. Analyze current industry standards, best practices, and regulatory considerations."
                    f"3.Benchmark against competitors and market leaders to identify gaps and opportunities."
                    f"4.Assess the {company} existing AI/ML adoption and automation maturity"
                    f"5.Identify challenges and inefficiencies in the {company} workflows."
                    f"4. Explore relevant GenAI, LLM, and ML applications for the {company}."
                    f"5.Map AI/ML technologies to business objectives"
                    f"6.Identify high-impact use cases for process automation, customer experience, and decision-making."
                    f"7.Suggest tools, platforms, and frameworks suitable for implementation.",
        expected_output=f"Detailed report on AI/ML use cases relevant to {company}.",
        output_file="company_usecases.txt",
        context=[search],
        agent=usecase_agent,
    )

    resource_collection = Task(
        description=f"1.Conducting a structured search to find high-quality datasets that align with AI/ML use cases identified for the {company} "
                    f"2.Focus is on publicly available original datasets from Kaggle, Hugging Face, and GitHub"
                    f"3.Will create a structured file that includes dataset descriptions, source links, and relevance to specific AI/ML use cases"
                    f"4.Explore potential GenAI solutions that leverage these datasets"
                    f"5.Focus on use cases such as document search, automated report generation, and AI-powered chat systems to improve internal and customer-facing operations",
        expected_output=f"Develop a structured proposal outlining possible GenAI applications, their feasibility, and potential business impact for the {company} while systematically organizing a well-structured .txt or .md file containing dataset names, descriptions, and links for efficient access and utilization",
        output_file="company_resources.txt",
        context=[search, usecase],
        agent=resource_agent,
    )

    return search , usecase,resource_collection


def run_agent(company):
    Research_agent,usecase_agent,resource_agent = create_agents(company)
    search,usecase,resource_collection = create_tasks(company, Research_agent, usecase_agent,resource_agent)
    
    crew = Crew(agents=[Research_agent,usecase_agent,resource_agent], tasks=[search,usecase,resource_collection], verbose=True)
    result = crew.kickoff(inputs={"company": company})
    return str(result) # Convert to string to display in Streamlit


def main():
    st.write("# AI-Driven Company Research")
    st.write("Enter a company name to analyze industry trends, AI/ML use cases, and relevant datasets.")
    
    company = st.text_input("Company Name:", "")
    if st.button("Run Analysis") and company:
        st.write(f"Analyzing {company}... Please wait.")
        result = run_agent(company)
        
        st.success("Analysis completed!")
        st.subheader("Results:")
        st.text_area("Output", result, height=300)
        
        # Save results to file
        output_file = f"{company}_analysis.txt"
        with open(output_file, "w") as f:
            f.write(result)
        
        # Download option
        with open(output_file, "rb") as f:
            st.download_button("Download Report", f, file_name=output_file, mime="text/plain")

if __name__ == "__main__":
    main()
