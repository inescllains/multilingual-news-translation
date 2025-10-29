# Multilingual News Translation for Academic Research

This project automates the translation and processing of Farsi (Persian) and Arabic news articles utilizing the Google Cloud Translation API. Originally developed for a Master's thesis at Charles University, it streamlines multilingual media analysis through translation, text extraction, and structured data export.

## 🎯 Project Overview

- **Purpose**: Translate and analyze Farsi and Arabic news articles for comparative media and discourse research
- **Scope**: Islamic discourse, women's rights, political communication in the Middle East
- **Output**: Bilingual corpus with original content, English translations, and structured CSV datasets

## 🚀 Quick Start

1. **Clone and install:**
git clone https://github.com/inescllains/multilingual-news-translation.git
cd multilingual-news-translation
pip install -r requirements.txt

2. **Set up Google Cloud credentials:**
export GOOGLE_APPLICATION_CREDENTIALS="path/to/your/service-account-key.json"

3. **Run translation scripts:**
Translate Farsi content --------- python translate_farsi.py

Translate Arabic articles ------  python translate_arabic.py

Process PDF files to text ------- python convert_txt.py


## 🛠️ Technologies Used

- **Python 3.11+**
- **Google Cloud Translation API v2**
- **newspaper3k** for web article scraping
- **FPDF2** for PDF generation
- **pdfplumber** and **re** for PDF-to-text conversion
- **Pandas** for data processing

## 📁 Project Structure
├── translate_farsi.py # Farsi translation tool
├── translate_arabic.py # Arabic translation tool
├── convert_txt.py # PDF-to-text batch conversion and CSV analysis
├── requirements.txt # Python dependencies
├── data/ # Sample datasets (CSV files)
│ └── processed_women_statements.csv
└── README.md # Project documentation


## ✨ Features

### 🇮🇷 Farsi Translation (`translate_farsi.py`)
- Processes Iranian media articles and extracts thematic content:
  - Islamic identity and women's rights
  - Jihad ideology and resistance movements
- Smart chunking to respect Google API limits
- Generates bilingual PDFs with translated and original content

### 🇸🇦 Arabic Translation (`translate_arabic.py`)
- Scrapes and translates online Arabic articles (e.g., Al Jazeera, party documents)
- Handles batch translation with clear progress feedback
- Exports translated results as structured CSV files

### 📄 PDF Text Processing (`convert_txt.py`)
- Converts source PDFs to clean text format
- Extracts statements, dates, and main content using regular expressions
- Aggregates and analyzes multiple documents, with output as annotated CSV files for further analysis

## ⚙️ Installation & Setup

### Prerequisites
- Python 3.11+
- Google Cloud account with Translation API enabled
- Service account JSON key file for authentication

### Step-by-Step Installation

1. **Clone the repository:**
git clone https://github.com/inescllains/multilingual-news-translation.git
cd multilingual-news-translation

2. **Install required libraries:**
pip install -r requirements.txt

3. **Set up Google Cloud credentials:**
Linux/Mac
export GOOGLE_APPLICATION_CREDENTIALS="path/to/your/service-account-key.json"

Windows
set GOOGLE_APPLICATION_CREDENTIALS="path/to/your/service-account-key.json"

## 🎮 Usage

### Running Individual Scripts

**Farsi Translation:**
python translate_farsi.py
- Processes Farsi text with intelligent chunking
- Outputs bilingual PDFs and translation logs

**Arabic Translation:**
python translate_arabic.py
- Scrapes Arabic articles from URLs
- Generates CSV files with original and translated content

**PDF Processing:**
python convert_txt.py
- Batch converts PDFs to text files
- Extracts structured data and exports to CSV

### Customizing Input Data

Edit the script files directly to modify:
- Input URLs (in `translate_arabic.py`)
- Text content (in `translate_farsi.py`)
- File paths (in `convert_txt.py`)

## 📊 Sample Output

### Translation Example
- **Original (Farsi):** زندگی های غزه زیر تیغ قحطی می افتد
- **English Translation:** "Gaza's lives are falling under the guillotine of starvation"

### File Outputs
- **PDFs:** Bilingual documents with original and translated content
- **CSV files:** Structured data for quantitative analysis
- **TXT files:** Clean text extraction from PDF sources

## 📚 Academic Context

This project was developed for Master's thesis research at **Charles University, Prague**, focusing on:

- **Comparative media discourse analysis**
- **Islamic political communication**
- **Gender representation in Middle Eastern media**
- **Multilingual corpus linguistics**

## 🔮 Future Improvements

- [ ] Support for batch URL processing
- [ ] Translation confidence scoring
- [ ] Additional languages (e.g., Turkish, Hebrew)
- [ ] Web interface for non-technical users
- [ ] Automated sentiment analysis integration

## 📝 Requirements.txt
google-cloud-translate==3.12.0
newspaper3k==0.2.8
fpdf2==2.7.6
pandas==2.1.0
pdfplumber==0.9.0


## 📄 License

This project is intended for **academic and research purposes**. Please cite appropriately if used in academic work.

## 👤 Author

**Inês Lains**  
🎓 Master's in International Security Studies, Charles University  
🔬 Research Focus: Middle Eastern politics, media, and discourse analysis  
🌐 [GitHub](https://github.com/inescllains) | [Portfolio](https://inescllains.github.io)

---

## 📞 Support

For questions or collaboration opportunities related to this research project:
- Open an issue in this repository
- Contact via GitHub profile

---

*Developed during Master's thesis research, 2025*



