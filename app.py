from flask import Flask, request, jsonify
from docx import Document
import os
from datetime import datetime

app = Flask(__name__)

OUTPUT_DIR = "static_docs"
os.makedirs(OUTPUT_DIR, exist_ok=True)

@app.route('/generate-docx', methods=['POST'])
def generate_docx():
    data = request.json

    doc = Document()
    doc.add_heading(data.get('job_title', 'Job Title'), 0)

    def add_section(title, content):
        doc.add_heading(title, level=1)
        doc.add_paragraph("")
        doc.add_paragraph(content)

    add_section("Job Purpose", data.get("job_purpose", ""))
    add_section("Essential Duties", data.get("primary_duties", ""))
    add_section("Additional Duties", data.get("additional_duties", ""))
    add_section("KPIs", data.get("kpis", ""))
    add_section("Qualifications", data.get("qualifications", ""))
    add_section("Working Conditions", data.get("working_conditions", ""))

    doc.add_paragraph("")
    doc.add_paragraph("Disclaimer: This job description may not be inclusive of all assigned duties, responsibilities, or aspects of the job described and may be amended by the employer at its discretion.")

    timestamp = datetime.utcnow().strftime("%Y%m%d%H%M%S")
    filename = f"{data.get('job_title', 'Job_Description').replace(' ', '_')}_{timestamp}.docx"
    filepath = os.path.join(OUTPUT_DIR, filename)
    doc.save(filepath)

    public_url = f"https://job-description-generator-new.onrender.com/{OUTPUT_DIR}/{filename}"
    return jsonify({ "download_url": public_url })

if __name__ == '__main__':
    app.run(debug=True)
