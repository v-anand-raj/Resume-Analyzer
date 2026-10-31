from flask import Flask, render_template, request, jsonify
from werkzeug.utils import secure_filename

import os
import sys
import tempfile

app = Flask(__name__)

app.config["MAX_CONTENT_LENGTH"] = 10 * 1024 * 1024  # 10 MB

# Project directories
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

SRC_DIR = os.path.join(BASE_DIR, "src")

KNOWLEDGE_BASE_DIR = os.path.join(
    BASE_DIR,
    "data",
    "knowledge_base",
    "processed"
)

# Import existing modules
sys.path.insert(0, SRC_DIR)

from text_extraction import extract_text_from_pdf
from ats_matching import analyze_resume_for_role


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze():

    temp_path = None

    try:

        # Check uploaded file
        if "resume" not in request.files:
            return jsonify({
                "error": "No resume uploaded."
            }), 400

        resume = request.files["resume"]

        if not resume.filename:
            return jsonify({
                "error": "Please select a resume."
            }), 400

        if not resume.filename.lower().endswith(".pdf"):
            return jsonify({
                "error": "Only PDF files are supported."
            }), 400

        # Get selected role
        selected_role = request.form.get("role", "").strip()

        if not selected_role:
            return jsonify({
                "error": "Please select a job role."
            }), 400

        # Validate selected role against supported profiles
        allowed_roles = [
            "AI Engineer",
            "Cybersecurity Analyst",
            "Data Analyst",
            "Database Administrator",
            "Penetration Tester",
            "Software Engineer",
            "Systems Analyst",
            "Web Developer"
        ]

        if selected_role not in allowed_roles:
            return jsonify({
                "error": "Invalid job role selected."
            }), 400

        # Save PDF temporarily
        with tempfile.NamedTemporaryFile(
            delete=False,
            suffix=".pdf"
        ) as temp_file:

            temp_path = temp_file.name

        resume.save(temp_path)

        # Extract resume text
        resume_text = extract_text_from_pdf(temp_path)

        if not resume_text or not resume_text.strip():
            return jsonify({
                "error": "Unable to extract text from this PDF."
            }), 400

        # Run ATS analysis
        result = analyze_resume_for_role(
            resume_text,
            selected_role,
            KNOWLEDGE_BASE_DIR
        )

        # Include original filename in results
        result["filename"] = secure_filename(resume.filename)

        # Render dynamic results page
        return render_template(
            "result.html",
            result=result
        )

    except Exception:
        app.logger.exception("Resume analysis failed")

        return jsonify({
            "error": "An error occurred while analyzing the resume. Check the Flask terminal for details."
        }), 500

    finally:

        # Delete temporary PDF after analysis
        if temp_path and os.path.exists(temp_path):
            os.remove(temp_path)


@app.errorhandler(413)
def file_too_large(error):
    return jsonify({
        "error": "File size exceeds the 10 MB limit."
    }), 413


if __name__ == "__main__":
    app.run(debug=True)