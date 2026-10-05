#!/usr/bin/env python3
"""Convert Markdown legal reports to styled, print-ready PDF files using md-to-pdf.

Usage:
  scripts/export-pdf.py cases/applicant/report/REVIEW.md
  scripts/export-pdf.py cases/applicant/report/COVER_LETTER_v1.md
"""
import os
import pathlib
import subprocess
import sys

CSS_CONTENT = """
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

body {
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  font-size: 11pt;
  line-height: 1.5;
  color: #1e293b;
  margin: 0;
  padding: 0;
}

h1 {
  font-size: 20pt;
  font-weight: 700;
  color: #0f172a;
  border-bottom: 2px solid #e2e8f0;
  padding-bottom: 8px;
  margin-top: 0;
}

h2 {
  font-size: 14pt;
  font-weight: 600;
  color: #1e293b;
  margin-top: 20px;
  border-bottom: 1px solid #cbd5e1;
  padding-bottom: 4px;
}

h3 {
  font-size: 12pt;
  font-weight: 600;
  color: #334155;
  margin-top: 14px;
}

blockquote {
  background-color: #f8fafc;
  border-left: 4px solid #3b82f6;
  margin: 12px 0;
  padding: 10px 14px;
  font-style: italic;
  color: #334155;
  border-radius: 4px;
}

table {
  width: 100%;
  border-collapse: collapse;
  margin: 14px 0;
  font-size: 10pt;
}

th, td {
  border: 1px solid #cbd5e1;
  padding: 8px 10px;
  text-align: left;
}

th {
  background-color: #f1f5f9;
  font-weight: 600;
  color: #0f172a;
}

tr:nth-child(even) {
  background-color: #f8fafc;
}

ul, ol {
  padding-left: 20px;
  margin: 8px 0;
}

li {
  margin-bottom: 4px;
}

code {
  background-color: #f1f5f9;
  padding: 2px 5px;
  border-radius: 4px;
  font-family: monospace;
  font-size: 9.5pt;
}

pre {
  background-color: #0f172a;
  color: #f8fafc;
  padding: 12px;
  border-radius: 6px;
  overflow-x: auto;
}

hr {
  border: 0;
  height: 1px;
  background: #cbd5e1;
  margin: 20px 0;
}

/* Print/Page formatting */
@page {
  size: A4;
  margin: 18mm 16mm 18mm 16mm;
}
"""

def main() -> int:
    if len(sys.argv) < 2:
        print("Usage: scripts/export-pdf.py <file.md> [output.pdf]")
        return 1

    md_path = pathlib.Path(sys.argv[1]).resolve()
    if not md_path.exists():
        print(f"❌ Error: File not found: {md_path}")
        return 1

    pdf_path = pathlib.Path(sys.argv[2]).resolve() if len(sys.argv) > 2 else md_path.with_suffix(".pdf")
    css_path = md_path.parent / "_style.css"
    css_path.write_text(CSS_CONTENT, encoding="utf-8")

    try:
        cmd = [
            "npx", "--yes", "md-to-pdf",
            str(md_path),
            "--stylesheet", str(css_path),
            "--pdf-options", '{"format": "A4", "printBackground": true}'
        ]
        print(f"🔄 Converting {md_path.name} -> {pdf_path.name}...")
        res = subprocess.run(cmd, capture_output=True, text=True)
        if res.returncode == 0 and pdf_path.exists():
            print(f"✅ Created beautiful PDF report: {pdf_path}")
            return 0
        else:
            print(f"❌ Error generating PDF:\n{res.stderr or res.stdout}")
            return 1
    finally:
        if css_path.exists():
            css_path.unlink()

if __name__ == "__main__":
    sys.exit(main())
