# Resume Analyzer

An NLP-based Resume Analyzer that evaluates resumes against predefined job-role requirements, identifies relevant skills, and provides actionable insights to help candidates understand how well their resumes align with a target role.

**Project Status:** Under Development 🚧

## Overview

Resume Analyzer is a Python-based web application designed to analyze resumes and evaluate their compatibility with different job roles.

The system extracts text from uploaded PDF resumes, processes the extracted content, identifies relevant technical skills, and compares them against role-specific knowledge bases.

Based on the matching results, it calculates compatibility points and displays matched and missing requirements through an interactive dashboard.

## Key Features

- **PDF Text Extraction:** Extracts textual information from uploaded PDF resumes.
- **Text Preprocessing:** Cleans and normalizes extracted resume text for further processing.
- **Skill Extraction:** Identifies relevant technical skills from resume content using NLP and pattern matching.
- **Role-Based Analysis:** Evaluates resumes against predefined job-role knowledge bases.
- **ATS Compatibility Scoring:** Assigns points based on matched requirements across different skill categories.
- **Matched and Missing Skills:** Highlights the skills found in the resume and identifies areas that may need improvement.
- **Interactive Dashboard:** Displays analysis results through a Flask-based web interface.

## Technologies Used

| Category | Technologies |
|---|---|
| Programming Language | Python |
| Backend | Flask |
| Frontend | HTML, CSS, JavaScript |
| NLP | spaCy, Regular Expressions |
| PDF Extraction | pdfplumber |
| Data Processing | Pandas, NumPy |
| Data Storage | JSON |
| Development Tools | Jupyter Notebook, VS Code |

## Project Architecture

The current analysis pipeline follows these stages:

1. **Resume Upload:** The user uploads a PDF resume and selects a target job role.
2. **Text Extraction:** Text is extracted from the uploaded PDF.
3. **Text Preprocessing:** Extracted text is cleaned and normalized.
4. **Skill Extraction:** Relevant skills and technical keywords are identified.
5. **Requirement Matching:** Extracted resume content is compared against role-specific requirements.
6. **ATS Scoring:** Points are assigned based on matched requirements.
7. **Result Visualization:** Matched skills, missing requirements, and compatibility points are displayed on the dashboard.

## Scoring Methodology

The current scoring system uses an additive point-based approach.

Each matched requirement contributes a fixed number of points depending on its category.

| Category | Points per Matched Skill |
|---|---:|
| Core Technical Skills | 5 |
| Domain Knowledge | 3 |
| Additional Skills | 1 |

**Total Compatibility Points:**

`Total Points = (Core Matches × 5) + (Domain Matches × 3) + (Additional Matches × 1)`

The system currently focuses on identifying matched and missing requirements rather than generating a percentage-based ATS score.

*Note: The scoring methodology is currently being tested and refined.*

## Project Structure

```text
Resume-Analyzer/
│
├── data/
│   ├── job_descriptions/
│   ├── knowledge_base/
│   │   └── processed/
│   ├── resumes/
│   └── skills.csv
│
├── notebooks/
│   ├── 01_text_extraction.ipynb
│   ├── 02_nlp_preprocessing.ipynb
│   ├── 03_skill_extraction.ipynb
│   ├── 04_ats_matching.ipynb
│   └── 05_integrated_pipeline.ipynb
│
├── src/
│   ├── text_extraction.py
│   ├── preprocessing.py
│   ├── skill_extraction.py
│   └── ats_matching.py
│
├── static/
│   ├── css/
│   └── js/
│
├── templates/
│   ├── index.html
│   ├── loading.html
│   └── result.html
│
├── app.py
├── requirements.txt
├── resume.ipynb
└── README.md
```

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/v-anand-raj/Resume-Analyzer.git
```

### 2. Navigate to the project directory

```bash
cd Resume-Analyzer
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

Activate it:

**Windows:**
```bash
venv\Scripts\activate
```

**Linux/macOS:**
```bash
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the application

```bash
python app.py
```

Open the following URL in your browser:

```text
http://127.0.0.1:5000/
```

*Note: The role-specific JSON knowledge bases are maintained locally and are not currently included in the GitHub repository. They must be placed in the expected knowledge-base directory before running role-based analysis.*

## Future Improvements

- Refine role-specific knowledge bases and skill categorization.
- Improve semantic skill matching to recognize equivalent skills and descriptions.
- Enhance evidence extraction to identify resume sentences supporting matched skills.
- Expand support for additional job roles.
- Improve ATS scoring and evaluation methodology.
- Enhance dashboard visualizations and result presentation.
- Integrate machine learning techniques for more advanced resume analysis.

## Project Status

This project is actively under development. The current implementation includes PDF text extraction, NLP preprocessing, skill matching, role-based analysis, and point-based ATS compatibility scoring.

Further improvements are being made to the knowledge bases, matching accuracy, and overall analysis pipeline.

---

**Developed by:** [Anand Raj](https://github.com/v-anand-raj)
