import os
import re
from google.cloud import translate_v2 as translate
from newspaper import Article
from fpdf import FPDF
import pandas as pd

# 🔁 Replace this with the name of your JSON key file
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "translation-thesis-466613-eae8275bd604.json"

client = translate.Client()

def farsi_text_to_sentences(text):
    # Split by Arabic/standard punctuation that indicates sentence endings
    sentences = re.split(r'(?<=[.!؟…])\s+', text)
    return [sentence.strip() for sentence in sentences if sentence.strip()]

def split_text_farsi(text, max_chunk_size=2000):
    import re
    sentences = re.split(r'(?<=[.!؟…])\s*', text)
    chunks = []
    current_chunk = ""
    for sentence in sentences:
        if len(current_chunk) + len(sentence) < max_chunk_size:
            current_chunk += sentence + " "
        else:
            chunks.append(current_chunk.strip())
            current_chunk = sentence + " "
    if current_chunk.strip():
        chunks.append(current_chunk.strip())
    return chunks

def translate_long_text(text, client, source='fa', target='en'):
    chunks = split_text_farsi(text)
    translated_chunks = []

    for i, chunk in enumerate(chunks):
        print(f"🔄 Translating chunk {i+1}/{len(chunks)}...")
        translated = client.translate(chunk, source_language=source, target_language=target)['translatedText']
        translated_chunks.append(translated)
    
    return "\n\n".join(translated_chunks)

# Example usage (your exact variables from notebook)
# farsi_title_islamic_identity = 'هویت اسلامی - تعداد فیش : 86 ، تعداد مقاله : 3'

# For when you have text to translate:
def main():
    # Add your farsi_title and farsi_text variables here
    # farsi_title = "your_title_here"
    # farsi_text = "your_text_here"
    
    # translated_title_long = translate_long_text(farsi_title, client)
    # translated_body_long = translate_long_text(farsi_text, client)
    
    # Save to PDF (your exact code)
    # filename = "islamic_modern_civilization.pdf"
    # pdf = FPDF()
    # pdf.add_page()
    # pdf.set_auto_page_break(auto=True, margin=15)
    
    # Add Unicode font
    # pdf.add_font('DejaVu', '', 'dejavu-fonts-ttf-2.37/ttf/DejaVuSans.ttf', uni=True)
    # pdf.add_font('DejaVu', 'B', 'dejavu-fonts-ttf-2.37/ttf/DejaVuSans-Bold.ttf', uni=True)
    # pdf.add_font('DejaVu', 'I', 'dejavu-fonts-ttf-2.37/ttf/DejaVuSans-Oblique.ttf', uni=True)
    
    # pdf.set_font('DejaVu', 'B', size=14)
    # pdf.multi_cell(0, 10, translated_title_long)
    # pdf.ln()
    
    # pdf.set_font('DejaVu', size=12)
    # pdf.multi_cell(0, 10, translated_body_long)
    
    # pdf.output(filename)
    # print(f"✅ Saved as {filename}")
    
    print("Farsi translation functions loaded successfully")

if __name__ == "__main__":
    main()
