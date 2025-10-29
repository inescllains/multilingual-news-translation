import pandas as pd
import pdfplumber
import re
import os

folder = '.'

# convert pdf to txt (your exact commented functions)
def pdf_to_txt(pdf_path, txt_path):
    with pdfplumber.open(pdf_path) as pdf:
        all_text = []
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                # Remove newlines and extra spaces
                cleaned = ' '.join(text.split())
                all_text.append(cleaned)
        # Join all pages into one line
        final_text = ' '.join(all_text)
        with open(txt_path, 'w', encoding='utf-8') as f:
            f.write(final_text)

def convert_pdfs_to_txt_in_folder(folder_path):
    for filename in os.listdir(folder_path):
        if filename.endswith(".pdf"):
            pdf_path = os.path.join(folder_path, filename)
            txt_path = os.path.join(folder_path, filename.replace(".pdf", ".txt"))
            pdf_to_txt(pdf_path, txt_path)
            print(f"Converted {filename} to TXT.")

def parse_txt_file(filepath):
    with open(filepath, encoding='utf-8') as f:
        text = f.read()

    pattern = re.compile(
        r'(Statements?.*?)(\d{2,4}/\d{2,4})(.*?)(?=Statements?|\Z)', 
        re.DOTALL | re.IGNORECASE
    )
    entries = []
    for match in pattern.finditer(text):
        title = match.group(1).strip()
        date = match.group(2).strip()
        body = match.group(3).strip()
        entries.append({'title': title, 'date': date, 'body': body})
    return entries

def process_folder(folder):
    for filename in os.listdir(folder):
        if filename.endswith('.txt'):
            filepath = os.path.join(folder, filename)
            entries = parse_txt_file(filepath)
            df = pd.DataFrame(entries)
            outname = filename.replace('.txt', '.csv')
            df.to_csv(outname, index=False, encoding='utf-8')
            print(f"✅ Saved {outname} with {len(df)} entries")

def add_filename_column(folder):
    for filename in os.listdir(folder):
        if filename.endswith('.csv'):
            filepath = os.path.join(folder, filename)
            df = pd.read_csv(filepath)
            df['filename'] = filename
            df.to_csv(filepath, index=False, encoding='utf-8')
            print(f"✅ Added filename column to {filename}")

def merge_csv_files(folder):
    all_data = []
    for filename in os.listdir(folder):
        if filename.endswith('.csv'):
            filepath = os.path.join(folder, filename)
            df = pd.read_csv(filepath)
            all_data.append(df)
    merged_df = pd.concat(all_data, ignore_index=True)
    merged_df.to_csv('merged_data.csv', index=False, encoding='utf-8')
    print("✅ Merged all CSV files into 'merged_data.csv'")

def main():
    # Load your data (your exact code from the notebook)
    df = pd.read_csv('merged_data.csv')
    
    # Your filtering logic (maintain exact column names and operations)
    # Add your specific filtering here based on your notebook
    
    # Iranian to Gregorian year mapping (your exact mapping)
    iranian_to_gregorian_years = {
        1388: "2009-2010", 1389: "2010-2011", 1390: "2011-2012",
        1391: "2012-2013", 1392: "2013-2014", 1393: "2014-2015",
        1394: "2015-2016", 1395: "2016-2017", 1396: "2017-2018",
        1397: "2018-2019", 1398: "2019-2020", 1399: "2020-2021",
        1400: "2021-2022", 1401: "2022-2023", 1402: "2023-2024",
        1403: "2024-2025"
    }
    
    iranian_months_to_gregorian = {
        1: "March-April", 2: "April-May", 3: "May-June",
        4: "June-July", 5: "July-August", 6: "August-September",
        7: "September-October", 8: "October-November", 9: "November-December",
        10: "December-January", 11: "January-February", 12: "February-March"
    }
    
    print("Text processing functions loaded successfully")

if __name__ == "__main__":
    main()
