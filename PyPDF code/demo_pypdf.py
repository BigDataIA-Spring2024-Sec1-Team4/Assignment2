import os
import PyPDF2
import re
from pathlib import Path

# Create PyPDF folder if it doesn't exist
pypdf_folder = Path("PyPDF")
if not pypdf_folder.exists():
    os.makedirs(pypdf_folder)

# Open and extract text from each PDF file
pdf_files = [
    '/Users/rutu/Downloads/NEU /SEM 3/Big Data /Assignment 2/Archive 2/2024-l1-topics-combined-2.pdf', 
    '/Users/rutu/Downloads/NEU /SEM 3/Big Data /Assignment 2/Archive 2/2024-l2-topics-combined-2.pdf', 
    '/Users/rutu/Downloads/NEU /SEM 3/Big Data /Assignment 2/Archive 2/2024-l3-topics-combined-2.pdf'
]


for i, pdf_file in enumerate(pdf_files):
    with open(pdf_file, "rb") as f:
        pdf_reader = PyPDF2.PdfReader(f)
        text = ""
        for page in range(len(pdf_reader.pages)):
            text += pdf_reader.pages[page].extract_text()
            text = re.sub(r'\d+', '', text)  # remove page numbers
            text = re.sub(r'^Footer.*\n', '', text, flags=re.MULTILINE)  # remove page footers
            # Remove page numbers 
            text = re.sub(r'Page\s*\d+\s*of\s*\d+', '', text)

            header_pattern = r'© CFA Institute\. For candidate use only\. Not for distribution\.'
            bullet_pattern = r'□'
            # Remove bullet points using regular expression
            text = re.sub(bullet_pattern, '', text)
            
            # Remove header using regular expression
            text = re.sub(header_pattern, '', text)
            text = re.sub(r'[\t\n\r ]*□[\t\n\r ]*', '', text)  


    # Save text to a text file in the PyPDF folder
    year = "RR" + str(2023 + i // 3)  
    level = "Level_100" + str(i % 3 + 1)  
    text_file = pypdf_folder / f"PyPDF_{year}_{level}_combined.txt"
    with open(text_file, "w") as g:
        g.write(text)