
# Job Description Generator API

## Overview
This API accepts job description data in JSON format and returns a formatted .docx file.

## How to Deploy (e.g. on Render.com)
1. Upload this repo to GitHub.
2. Create a new Web Service on https://render.com
3. Use:
   - Build Command: pip install -r requirements.txt
   - Start Command: gunicorn app:app
4. Set your endpoint to: https://job-description-generator-new.onrender.com/generate-docx

## Example JSON Input
{
  "job_title": "Pharmacy Manager",
  "job_purpose": "The Pharmacy Manager is responsible for...",
  "primary_duties": "- Manage inventory\n- Supervise staff",
  "additional_duties": "- Support onboarding\n- Promote safety culture",
  "kpis": "- Zero safety incidents\n- Compliance with college regulations",
  "qualifications": "- BSc in Pharmacy\n- Licensed by provincial college",
  "working_conditions": "- May be exposed to medication storage environments"
}
