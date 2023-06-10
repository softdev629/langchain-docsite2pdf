import os
from nbconvert import HTMLExporter, PDFExporter
import nbformat


def convert_to_pdf(src_dir):
    # Create empty list to store files to be converted
    input_files = []

    # Walk through directory tree and find all relevant files
    for dirpath, dirnames, filenames in os.walk(src_dir):
        for filename in filenames:
            if filename.endswith('.md') or filename.endswith('.mdx'):
                file_path = os.path.join(dirpath, filename)
                input_files.append(file_path)

    # Configure PDF exporter
    pdf_exporter = PDFExporter()
    pdf_exporter.template_file = 'classic'

    # Create empty list to store converted HTML files
    html_files = []
    cnt = 0
    # Convert each file to HTML format
    for file_path in input_files:

        # Check if file is a Jupyter notebook
        if file_path.endswith('.md') or file_path.endswith('.mdx'):
            html_file = file_path.replace(
                '.mdx', '.html').replace('.md', '.html')
            html_files.append(html_file)
            os.system(f"pandoc {file_path} -s -o {html_file}")
        if len(' '.join(html_files)) > 7000:
            os.system(f"wkhtmltopdf {' '.join(html_files)} output-{cnt}.pdf")
            html_files.clear()
            cnt += 1

    # Combine HTML files into single PDF
    os.system(f"wkhtmltopdf {' '.join(html_files)} output-{cnt}.pdf")

    # Delete temporary HTML files
    for html_file in html_files:
        os.remove(html_file)


# Example usage
src_dir = './js-docs'
convert_to_pdf(src_dir)
