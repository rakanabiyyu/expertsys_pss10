# MindCalm PSS-10: Stress Level Analysis Expert System

MindCalm PSS-10 is a web-based application (expert system) designed to help students and the general public identify and measure their stress levels using an internationally recognized standard psychological instrument, the **Perceived Stress Scale (PSS-10)**.

This application utilizes the Certainty Factor (CF) method within its expert system to not only calculate the total stress score but also determine the dominant symptom that most significantly affects the user's psychological condition, along with the degree of certainty (CF) of the result.

## Disclaimer

This expert system serves as an initial screening instrument (based on the PSS-10) and does not constitute a definitive medical or clinical diagnostic tool. If you or someone you know requires serious assistance regarding mental health, please contact a psychologist, psychiatrist, or the nearest healthcare facility immediately.

## Key Features

- **Interactive PSS-10 Questionnaire**: A modern and user-friendly interface for completing the 10 standard PSS-10 questions.
- **Automated Score Analysis**: Automatically calculates the conventional PSS-10 score, including reverse scoring for positive items.
- **Expert System with Certainty Factor**: Identifies the dominant symptom causing stress and measures the confidence percentage (CF).
- **Interpretation and Context**: Provides stress level categorization (Low, Moderate, High) along with context-specific background information.
- **Printable PDF Results**: Allows users to save and print the clinical summary report to facilitate discussions with professional counselors or psychologists.
- **Responsive and Modern Interface**: Features an aesthetically pleasing and responsive design across various devices, built with Tailwind CSS.

## Technologies Used

- **Backend**: Python 3.x, Flask (Web Framework)
- **Frontend**: HTML5, JavaScript (Vanilla), Tailwind CSS (via CDN)
- **Dependency Manager**: `uv` or `pip`

---

## System Requirements

Prior to running this application on your local machine, please ensure the following software is installed:
1. **Python** (version 3.8 or newer). Available for download at [python.org](https://www.python.org/downloads/).
2. **Git** (optional, for repository cloning).
3. **`uv`** (recommended as a fast Python package manager), although the standard Python `pip` is also fully supported.

---

## Installation and Execution Guide

Follow these comprehensive steps to run the application in your local environment:

### Step 1: Acquire the Source Code
If using Git, execute the following command in your terminal or command prompt:
```bash
git clone https://github.com/rakanabiyyu/expertsys_pss10.git
cd expertsys_pss10
```
Alternatively, you may download the repository as a `.zip` file, extract its contents, and navigate to the extracted directory within your terminal.

### Step 2: Establish a Virtual Environment (Highly Recommended)
To prevent the application's dependencies from interfering with your global Python libraries, it is strongly advised to create a virtual environment.

**Windows Users:**
```bash
python -m venv venv
venv\Scripts\activate
```

**macOS / Linux Users:**
```bash
python3 -m venv venv
source venv/bin/activate
```
Upon successful execution, your terminal prompt will display `(venv)`, indicating the virtual environment is active.

### Step 3: Install Dependencies
This application utilizes Flask as its core framework. Install the required libraries using the following command:
```bash
pip install -r requirements.txt
```
Note: If you are utilizing `uv`, you may bypass manual virtual environment activation and run the application directly via `uv run app.py`.

### Step 4: Initialize the Application
Execute the following command to start the web server:
```bash
python app.py
```

### Step 5: Access via Web Browser
Upon successful initialization, the terminal will indicate that the server is running (typically on port 5000). 
Open your preferred web browser and navigate to the following address:
**http://127.0.0.1:5000** or **http://localhost:5000**

You may now begin utilizing the MindCalm PSS-10 application.

---

## Project Directory Structure

A brief overview of the project's architecture:
- `app.py`: The primary backend application file (Flask). It contains the PSS-10 calculation logic, routing configuration, and the Certainty Factor methodology implementation.
- `requirements.txt`: The manifest of required Python dependencies.
- `templates/`: The directory housing all HTML interface files.
  - `index.html`: The primary landing page.
  - `register.html`: The registration form presented prior to initiating the assessment.
  - `test.html`: The interactive PSS-10 questionnaire interface.
  - `result.html`: The page displaying the assessment results and corresponding stress level analysis.
  - `print.html`: The specialized layout designed for generating printable PDF reports.
  - `education.html`: The informational page containing educational resources regarding stress management.


