# Week 2 Challenge: Telecommunication Data Analysis

## Aim of the Challenge
The goal of this challenge is to analyze data from TellCo, a mobile service provider, to extract actionable insights on user behavior, engagement, experience, and satisfaction. The final deliverable includes a Streamlit dashboard and a written report to assist in evaluating the company’s growth potential and provide recommendations for investment.

## Environment Setup

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/Fetiya-Kedir/KAIM3-Week-2
   cd KAIM3-Week-2
   ```

2. **Set Up a Virtual Environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up the Database:**
   - Ensure PostgreSQL is installed and running.
   - Load the provided schema and data into the PostgreSQL database.
   - Update database credentials in the `src/config.py` file.

5. **Run the Application:**
   - Start the Streamlit dashboard:
     ```bash
     streamlit run src/app.py
     ```

6. **Run Tests:**
   - Execute tests to ensure the environment is set up correctly:
     ```bash
     pytest
     ```

For more details, refer to the project documentation or contact the project maintainer.
