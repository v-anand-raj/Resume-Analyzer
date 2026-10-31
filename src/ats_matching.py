import json
import re
import os

from skill_extraction import extract_skills


# ============================================================
# 1. OLD JOB DESCRIPTION-BASED ATS FUNCTIONS
# ============================================================

def read_job_description(jd_path):
    with open(jd_path, "r", encoding="utf-8") as file:
        return file.read()


def compare_skills(resume_skills, jd_skills):
    resume_set = set(resume_skills)
    jd_set = set(jd_skills)

    matched_skills = sorted(resume_set.intersection(jd_set))
    missing_skills = sorted(jd_set.difference(resume_set))

    return matched_skills, missing_skills


def calculate_ats_score(matched_skills, jd_skills):
    if len(jd_skills) == 0:
        return 0

    score = (len(matched_skills) / len(jd_skills)) * 100

    return round(score, 2)


def load_all_job_descriptions(folder_path):
    job_descriptions = {}

    for file in os.listdir(folder_path):
        if file.endswith(".txt"):
            file_path = os.path.join(folder_path, file)

            with open(file_path, "r", encoding="utf-8") as f:
                job_descriptions[file] = f.read()

    return job_descriptions


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


# ============================================================
# 2. ROLE PROFILE LOADING
# ============================================================

def normalize_role_name(role_name):
    return re.sub(
        r"[^a-z0-9]+",
        " ",
        role_name.lower()
    ).strip()


def load_role_profile(selected_role, knowledge_base_dir):

    aliases = {
        "software engineer": "software_engineer.json",
        "software engineer developer": "software_engineer.json",
        "ai engineer": "ai_engineer.json",
        "cybersecurity analyst": "cybersecurity_analyst.json",
        "data analyst": "data_analyst.json",
        "database administrator": "database_administrator.json",
        "penetration tester": "penetration_tester.json",
        "systems analyst": "systems_analyst.json",
        "web developer": "web_developer.json",
    }

    normalized_role = normalize_role_name(selected_role)
    filename = aliases.get(normalized_role)

    if filename is None:
        raise ValueError(
            f"Unsupported role: {selected_role}. "
            f"Available roles: {', '.join(aliases.keys())}"
        )

    file_path = os.path.join(knowledge_base_dir, filename)

    if not os.path.isfile(file_path):
        raise FileNotFoundError(
            f"Knowledge-base file not found: {file_path}"
        )

    with open(file_path, "r", encoding="utf-8") as f:
        profile = json.load(f)

    return profile


# ============================================================
# 3. TEXT NORMALIZATION
# ============================================================

def normalize_text(text):
    text = str(text).lower()

    text = text.replace("&", " and ")

    text = re.sub(
        r"[^a-z0-9+#./\s-]",
        " ",
        text
    )

    text = re.sub(r"\s+", " ", text)

    return text.strip()


# ============================================================
# 4. TECHNICAL SKILL ALIASES
# ============================================================

SKILL_ALIASES = {

    "python": [
        "python",
        "python computer programming",
        "python (computer programming)"
    ],

    "java": [
        "java",
        "oracle java",
        "java computer programming",
        "java (computer programming)"
    ],

    "sql": [
        "sql",
        "structured query language",
        "structured query language sql"
    ],

    "aws": [
        "aws",
        "amazon web services",
        "amazon web services aws software"
    ],

    "azure": [
        "azure",
        "microsoft azure",
        "microsoft azure software"
    ],

    "css": [
        "css",
        "cascading style sheets",
        "cascading style sheets css"
    ],

    "html": [
        "html",
        "hypertext markup language",
        "hypertext markup language html"
    ],

    "javascript": [
        "javascript",
        "js"
    ],

    "git": [
        "git"
    ],

    "github": [
        "github"
    ],

    "rest api": [
        "rest api",
        "restful api"
    ],

    "node.js": [
        "node.js",
        "node js"
    ],

    "power bi": [
        "power bi",
        "microsoft power bi",
        "powerbi"
    ],

    "excel": [
        "excel",
        "microsoft excel",
        "microsoft office excel"
    ],

    "pandas": [
        "pandas"
    ],

    "numpy": [
        "numpy"
    ],

    "machine learning": [
        "machine learning",
        "ml"
    ],
    "power bi": [
        "power bi",
        "microsoft power bi"
    ],

    "excel": [
        "excel",
        "microsoft excel"
    ],

    "azure": [
        "azure",
        "microsoft azure"
    ],

    "aws": [
        "aws",
        "amazon web services"
    ],

    "jira": [
        "jira",
        "atlassian jira"
    ],

    "looker": [
        "looker",
        "google looker",
        "google looker analytics"
    ],

    "sql": [
        "sql",
        "structured query language"
    ]
}


# ============================================================
# 5. REQUIREMENT ALIASES
# ============================================================

REQUIREMENT_ALIASES = {

    # Software engineering requirements

    "debug software": [
        "debugged software",
        "fixed software bugs",
        "fixed application bugs",
        "identified and fixed bugs",
        "troubleshot application errors"
    ],

    "use software libraries": [
        "used python libraries",
        "used software libraries",
        "implemented functionality using libraries"
    ],

    "computer programming": [
        "programming",
        "programmed applications",
        "developed applications using python",
        "developed applications using java",
        "wrote code in python",
        "wrote code in java"
    ],

    "use object-oriented programming": [
        "object oriented programming",
        "object-oriented programming",
        "applied oop principles",
        "used oop concepts"
    ],

    "use software design patterns": [
        "implemented software design patterns",
        "used design patterns",
        "applied design patterns"
    ],

    "create flowchart diagram": [
        "created flowcharts",
        "designed flowcharts",
        "created process flow diagrams"
    ],

    "develop software prototype": [
        "developed a software prototype",
        "built a software prototype",
        "built a prototype application",
        "created a working prototype",
        "built a prototype",
        "developed a prototype"
    ],

    "use query languages": [
        "wrote sql queries",
        "used sql queries",
        "queried relational databases"
    ],

    "utilise machine learning": [
        "used machine learning",
        "implemented machine learning models",
        "trained machine learning models"
    ],

    # Data Analyst requirements

    "data visualisation software": [
        "power bi",
        "microsoft power bi",
        "created interactive power bi dashboards"
    ],

    "use spreadsheets software": [
        "excel",
        "microsoft excel"
    ],

    "deliver visual presentation of data": [
        "created interactive power bi dashboards",
        "created data visualisations",
        "created data visualizations"
    ],

    "analyse big data": [
        "analysed big data",
        "analyzed big data",
        "big data analysis"
    ],

    "apply statistical analysis techniques": [
        "statistical analysis",
        "applied statistical techniques",
        "statistical modelling",
        "statistical modeling"
    ],

    "perform data mining": [
        "data mining",
        "performed data mining"
    ],

    "use data processing techniques": [
        "data processing",
        "data preprocessing",
        "data transformation"
    ],

    "use databases": [
        "database management",
        "mysql",
        "mongodb",
        "sql database"
    ]
}


# ============================================================
# 6. COMMON PHRASE MATCHING
# ============================================================

def contains_phrase(source, phrase):

    phrase = normalize_text(phrase)

    if not phrase:
        return False

    pattern = (
        r"(?<!\w)"
        + r"\s+".join(
            re.escape(word)
            for word in phrase.split()
        )
        + r"(?!\w)"
    )

    return re.search(pattern, source) is not None


def get_requirement_candidates(requirement, metadata=None):

    metadata = metadata or {}

    label = str(requirement).strip()
    normalized_label = normalize_text(label)

    candidates = [label]

    # Built-in requirement aliases

    candidates.extend(
        REQUIREMENT_ALIASES.get(normalized_label, [])
    )

    # JSON-defined aliases

    requirement_info = metadata.get(label, {})

    candidates.extend(
        requirement_info.get("aliases", [])
    )

    # Technical skill aliases

    for canonical, aliases in SKILL_ALIASES.items():

        names = [canonical] + aliases

        normalized_names = {
            normalize_text(name)
            for name in names
        }

        if normalized_label in normalized_names:
            candidates.extend(names)
            break

    return candidates


# ============================================================
# 7. REQUIREMENT MATCHING ENGINE
# ============================================================

def match_requirements(resume_text, requirements, metadata=None):

    metadata = metadata or {}

    text = normalize_text(resume_text)

    matched = []
    missing = []

    for requirement in requirements:

        candidates = get_requirement_candidates(
            requirement,
            metadata
        )

        is_matched = any(
            contains_phrase(text, candidate)
            for candidate in candidates
        )

        if is_matched:
            matched.append(requirement)
        else:
            missing.append(requirement)

    return matched, missing


# ============================================================
# 8. SCORING FUNCTIONS
# ============================================================
CATEGORY_POINTS = {
    "core_technical_skills": 5,
    "domain_knowledge": 3,
    "additional_skills": 1
}

def calculate_category_score(matched, total):

    if total == 0:
        return 0.0

    return round(
        (len(matched) / total) * 100,
        2
    )


def calculate_weighted_category_score(
    matched, requirements, metadata=None
):

    metadata = metadata or {}

    if not requirements:
        return 0.0

    total_weight = 0.0
    matched_weight = 0.0

    matched_set = set(matched)

    for requirement in requirements:

        info = metadata.get(str(requirement), {})

        weight = float(info.get("weight", 1.0))

        total_weight += weight

        if requirement in matched_set:
            matched_weight += weight

    if total_weight == 0:
        return 0.0

    return round(
        (matched_weight / total_weight) * 100,
        2
    )


def calculate_weighted_market_score(
    matched_skills, market_skills
):

    total_weight = sum(
        float(skill.get("percentage", 0))
        for skill in market_skills
    )

    if total_weight == 0:
        return 0.0

    matched_names = {
        normalize_text(skill)
        for skill in matched_skills
    }

    matched_weight = sum(
        float(skill.get("percentage", 0))
        for skill in market_skills
        if normalize_text(skill["name"]) in matched_names
    )

    return round(
        (matched_weight / total_weight) * 100,
        2
    )


# ============================================================
# 9. EVIDENCE EXTRACTION
# ============================================================

def find_requirement_evidence(
    resume_text, requirement, metadata=None
):

    metadata = metadata or {}

    # Split resume into sentences and lines

    sentences = re.split(
        r"(?<=[.!?])\s+|\n+",
        resume_text
    )

    candidates = get_requirement_candidates(
        requirement,
        metadata
    )

    for sentence in sentences:

        normalized_sentence = normalize_text(sentence)

        for candidate in candidates:

            if contains_phrase(
                normalized_sentence,
                candidate
            ):
                return sentence.strip()

    return None


def add_evidence_to_matches(
    resume_text, matched_requirements, metadata=None
):

    results = []

    for requirement in matched_requirements:

        evidence = find_requirement_evidence(
            resume_text,
            requirement,
            metadata
        )

        results.append({
            "requirement": requirement,
            "evidence": evidence
        })

    return results


# ============================================================
# 10. COMPLETE ROLE-BASED RESUME ANALYSIS
# ============================================================

# def analyze_resume_for_role(
#     resume_text, selected_role, knowledge_base_dir
# ):
#     """Analyze a resume against the selected role's JSON profile."""

#     profile = load_role_profile(
#         selected_role, knowledge_base_dir
#     )

#     # Load the three new categories
#     core_skills = profile.get("core_technical_skills", [])
#     domain_knowledge = profile.get("domain_knowledge", [])
#     additional_skills = profile.get("additional_skills", [])

#     # Match requirements independently
#     core_matched, core_missing = match_requirements(
#         resume_text, core_skills
#     )

#     domain_matched, domain_missing = match_requirements(
#         resume_text, domain_knowledge
#     )

#     additional_matched, additional_missing = match_requirements(
#         resume_text, additional_skills
#     )

#     # Calculate category scores
#     core_score = calculate_category_score(
#         core_matched, len(core_skills)
#     )

#     domain_score = calculate_category_score(
#         domain_matched, len(domain_knowledge)
#     )

#     additional_score = calculate_category_score(
#         additional_matched, len(additional_skills)
#     )

#     # Calculate final compatibility score
#     final_score = (
#         core_score * 0.60
#         + domain_score * 0.25
#         + additional_score * 0.15
#     )

#     return {
#         "role": profile["role"],

#         "compatibility_score": round(final_score, 2),

#         "categories": {
#             "core_technical_skills": {
#                 "score": core_score,
#                 "matched": core_matched,
#                 "missing": core_missing
#             },

#             "domain_knowledge": {
#                 "score": domain_score,
#                 "matched": domain_matched,
#                 "missing": domain_missing
#             },

#             "additional_skills": {
#                 "score": additional_score,
#                 "matched": additional_matched,
#                 "missing": additional_missing
#             }
#         }
#     }

def analyze_resume_for_role(
    resume_text, selected_role, knowledge_base_dir
):
    """Analyze resume using point-based skill matching."""

    profile = load_role_profile(
        selected_role, knowledge_base_dir
    )

    categories = {
        "core_technical_skills": profile.get(
            "core_technical_skills", []
        ),
        "domain_knowledge": profile.get(
            "domain_knowledge", []
        ),
        "additional_skills": profile.get(
            "additional_skills", []
        )
    }

    results = {}
    total_points = 0

    for category_name, requirements in categories.items():

        matched, missing = match_requirements(
            resume_text, requirements
        )

        points_per_skill = CATEGORY_POINTS[category_name]

        earned_points = len(matched) * points_per_skill

        total_points += earned_points

        results[category_name] = {
            "matched": matched,
            "missing": missing,
            "matched_count": len(matched),
            "points_per_skill": points_per_skill,
            "earned_points": earned_points
        }

    return {
        "role": profile["role"],
        "total_points": total_points,
        "categories": results
    }