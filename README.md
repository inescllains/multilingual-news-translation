# Multilingual News Translation for Academic Research

This project automates the translation of Farsi (Persian) and Arabic news articles using Google Cloud Translation API. Developed for Master's thesis research on Middle Eastern media discourse analysis.

## Project Overview

- **Purpose**: Translate Farsi and Arabic news articles for comparative media analysis
- **Scope**: Academic research on Islamic discourse and women's rights narratives
- **Output**: Bilingual corpus with original text and English translations

## 🛠️ Technologies Used

- **Python 3.11+**
- **Google Cloud Translation API v2**
- **Jupyter Notebooks** for interactive development
- **newspaper3k** for article scraping
- **FPDF2** for PDF generation
- **Pandas** for data manipulation

## 📁 Project Structure
├── translate_farsi.ipynb # Farsi translation notebook
├── translate_arabic.ipynb # Arabic translation notebook
├── requirements.txt # Python dependencies
└── README.md # This file


## Features

### Farsi Translation (`translate_farsi.ipynb`)
- Processes Iranian media articles on topics like:
  - Islamic identity and women's rights
  - Jihad ideology and resistance movements
  - Lebanese political discourse
- Handles text chunking for Google API limits
- Generates bilingual PDF outputs

### Arabic Translation (`translate_arabic.ipynb`)
- Translates Al Jazeera articles and political documents
- Automated article scraping from URLs
- Batch processing with progress tracking
- CSV export for data analysis

## ⚙️ Setup Instructions

### Prerequisites
1. Python 3.11+
2. Google Cloud account with Translation API enabled
3. Service account JSON key file

### Installation
Clone the repository
git clone https://github.com/inescllains/multilingual-news-translation.git
cd multilingual-news-translation

Install dependencies
pip install -r requirements.txt

Set up Google Cloud credentials
export GOOGLE_APPLICATION_CREDENTIALS="path/to/your/service-account-key.json"

### Running the Translation
Start Jupyter Notebook
jupyter notebook

Open either translate_farsi.ipynb or translate_arabic.ipynb
Follow the notebook cells to process your texts


## 📊 Sample Output

The project processes articles like:
- **Original** (Farsi): "زندگی های غزه زیر تیغ قحطی می افتد"
- **Translated**: "Gaza's lives are falling under the guillotine of starvation"

## 🎓 Academic Context

This translation tool was developed for Master's thesis research at Charles University, Prague, focusing on:
- Comparative media discourse analysis
- Islamic political communication
- Gender representation in Middle Eastern media

## 🔮 Future Improvements

- [ ] Add support for batch URL processing
- [ ] Implement translation confidence scoring
- [ ] Add support for additional languages (Turkish, Hebrew)
- [ ] Create web interface for non-technical users

## 📝 License

This project is for academic research purposes. Please cite if used in academic work.

## 👤 Author

**Inês Lains**
- Master's in International Security Studies, Charles University
- Research focus: Middle Eastern politics and media analysis
- [GitHub](https://github.com/inescllains) | [Portfolio](https://inescllains.github.io)

---
*Developed during Master's thesis research, 2025*
