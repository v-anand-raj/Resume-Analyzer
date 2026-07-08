def read_job_description(jd_path):
    with open(jd_path, "r", encoding="utf-8") as file:
        job_description = file.read()

    return job_description

def compare_skills(resume_skills, jd_skills):
    """
    Compare resume skills with job description skills.
    """

    resume_set = set(resume_skills)
    jd_set = set(jd_skills)

    matched_skills = sorted(resume_set.intersection(jd_set))
    missing_skills = sorted(jd_set.difference(resume_set))

    return matched_skills, missing_skills

def calculate_ats_score(matched_skills, jd_skills):
    """
    Calculates ATS score based on the percentage of
    job description skills found in the resume.
    """

    if len(jd_skills) == 0:
        return 0

    score = (len(matched_skills) / len(jd_skills)) * 100

    return round(score, 2)

import os

def load_all_job_descriptions(folder_path):
    """
    Reads all job description text files from a folder.

    Args:
        folder_path (str): Path to the job description folder.

    Returns:
        dict: {job_name: job_description}
    """

    job_descriptions = {}

    for file in os.listdir(folder_path):

        if file.endswith(".txt"):

            file_path = os.path.join(folder_path, file)

            with open(file_path, "r", encoding="utf-8") as f:

                job_descriptions[file] = f.read()

    return job_descriptions
from skill_extraction import extract_skills


def analyze_resume(resume_skills, job_descriptions, skills):

    ats_results = {}

    for job_name, job_description in job_descriptions.items():

        jd_skills = extract_skills(job_description, skills)

        matched_skills, missing_skills = compare_skills(
            resume_skills,
            jd_skills
        )

        ats_score = calculate_ats_score(
            matched_skills,
            jd_skills
        )

        ats_results[job_name] = {
            "score": ats_score,
            "matched": matched_skills,
            "missing": missing_skills
        }

    return ats_results

def rank_jobs(ats_results):

    sorted_results = sorted(
        ats_results.items(),
        key=lambda item: item[1]["score"],
        reverse=True
    )

    return sorted_results