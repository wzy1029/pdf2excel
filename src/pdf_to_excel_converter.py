import os
import camelot
import pandas as pd
from pathlib import Path

# Set the directory path
directory = '/Users/isy/Downloads/'

# Get all PDF files in the directory
pdf_files = [f for f in os.listdir(directory) if f.endswith('.pdf')]

def convert_pdf_to_excel(pdf_path, excel_path):
    try:
        # Read PDF file
        print(f"Converting {pdf_path}...")
        
        # Try lattice mode first
        tables = camelot.read_pdf(
            pdf_path,
            pages='all',
            flavor='lattice'
        )
        
        if len(tables) == 0:
            # If no tables found, try stream mode
            print("Trying stream mode...")
            tables = camelot.read_pdf(
                pdf_path,
                pages='all',
                flavor='stream'
            )
        
        # If tables were found
        if len(tables) > 0:
            # Create Excel writer object
            with pd.ExcelWriter(excel_path, engine='openpyxl') as writer:
                # Write each table to a different sheet
                for i, table in enumerate(tables):
                    df = table.df
                    if not df.empty:
                        # Clean the table data
                        df = df.fillna('')  # Replace NaN with empty string
                        df = df.replace('\r', ' ', regex=True)  # Remove carriage returns
                        df.to_excel(writer, sheet_name=f'Sheet{i+1}', index=False)
            print(f"Successfully converted to {excel_path}")
        else:
            print(f"No tables found in {pdf_path}")
            
    except Exception as e:
        print(f"Error converting {pdf_path}: {str(e)}")
        print("Please ensure:")
        print("1. The PDF is not password protected")
        print("2. Ghostscript is properly installed")
        print("3. The PDF is not corrupted")

# Process each PDF file
for pdf_file in pdf_files:
    pdf_path = os.path.join(directory, pdf_file)
    # Create Excel filename by replacing .pdf extension with .xlsx
    excel_file = pdf_file.rsplit('.', 1)[0] + '.xlsx'
    excel_path = os.path.join(directory, excel_file)
    
    convert_pdf_to_excel(pdf_path, excel_path) 