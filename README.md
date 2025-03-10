# AI-Driven Company Research

## Overview
This Streamlit application leverages AI agents to conduct comprehensive research on a company, identifying its industry classification, AI/ML use case opportunities, and relevant datasets. The application automates data collection, analysis, and reporting to provide valuable insights into the company's strategic positioning and potential AI adoption.

## Features
- **Industry & Company Research:** Determines the industry and sub-sectors of a given company, identifying key products, services, and strategic areas.
- **AI/ML Use Case Identification:** Analyzes industry trends and company-specific factors to propose AI, ML, and automation opportunities.
- **Resource Collection:** Finds and organizes relevant datasets from sources like Kaggle, Hugging Face, and GitHub to support AI applications.
- **Automated Report Generation:** Generates structured reports for each research area and allows users to download the results.

## Technologies Used
- **Python**: Core programming language
- **Streamlit**: Web-based UI for user interaction
- **CrewAI**: Agent-based task automation
- **OpenAI API**: AI-powered research and analysis
- **Dotenv**: Environment variable management
- **Pandas, NumPy**: Data handling and manipulation

## Installation
### Prerequisites
Ensure you have Python installed (>=3.8) and the required dependencies.

### Setup Instructions
1. Clone the repository:
   ```sh
   git clone https://github.com/your-repo/ai-driven-company-research.git
   cd ai-driven-company-research
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Set up environment variables:
   - Create a `.env` file in the project directory.
   - Add your OpenAI API key:
     ```
     OPENAI_API_KEY=your_openai_api_key_here
     ```
4. Run the application:
   ```sh
   streamlit run app.py
   ```

## Usage
1. Enter a company name in the input field.
2. Click "Run Analysis" to initiate research.
3. View results in the text area or download the report.

## Output Files
- `company_research.txt`: Contains industry classification and key offerings.
- `company_usecases.txt`: Lists AI/ML opportunities for the company.
- `company_resources.txt`: Contains dataset sources and relevance.
- `{company}_analysis.txt`: Consolidated report for the given company.

## Author
Developed by [https://github.com/Sisira121].

## License
This project is licensed under the MIT License.


