This version saves the .docx file to a public static directory and returns a download link.

Deployment Notes:
- Ensure Render allows public static file access from the `static_docs` folder.
- Output is a JSON response like: { "download_url": "https://..." }
