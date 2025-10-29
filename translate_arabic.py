import os
import re
from google.cloud import translate_v2 as translate
from newspaper import Article
from fpdf import FPDF
import pandas as pd

# 🔁 Replace this with the name of your JSON key file
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "translation-thesis-466613-eae8275bd604.json"

client = translate.Client()

urls = ["https://www.aljazeera.net/encyclopedia/2009/11/30/%D8%A7%D9%84%D9%88%D8%AB%D9%8A%D9%82%D8%A9-%D8%A7%D9%84%D8%B3%D9%8A%D8%A7%D8%B3%D9%8A%D8%A9-%D9%84%D8%AD%D8%B2%D8%A8-%D8%A7%D9%84%D9%84%D9%87"]
records = []

def safe_filename(text):
    return re.sub(r'[\\/*?:"<>|]', "", text)

def split_text_arabic(text, max_chunk_size=2000):
    # Split by Arabic sentence endings
    sentences = re.split(r'(?<=[\.؟!…])\s*', text)
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

def translate_chunks(chunks, source='ar', target='en', batch_size=10):
    translated = []
    for i in range(0, len(chunks), batch_size):
        batch = chunks[i:i + batch_size]
        print(f"Translating batch {i // batch_size + 1} of {len(chunks) // batch_size + 1}...")
        result = client.translate(batch, source_language=source, target_language=target)
        translated.extend([r['translatedText'] for r in result])
    return translated

def translate_long_text(text, client, source='ar', target='en'):
    chunks = split_text_arabic(text)
    translated_chunks = []

    for i, chunk in enumerate(chunks):
        print(f"🔄 Translating chunk {i+1}/{len(chunks)}...")
        translated = client.translate(chunk, source_language=source, target_language=target)['translatedText']
        translated_chunks.append(translated)
    
    return "\n\n".join(translated_chunks)

def arabic_text_to_sentences(text):
    # Split by Arabic/standard punctuation that indicates sentence endings
    sentences = re.split(r'(?<=[.!؟…])\s+', text)
    return [sentence.strip() for sentence in sentences if sentence.strip()]

def main():
    # Your exact processing loop
    for i, url in enumerate(urls):
        try:
            article = Article(url, language='ar')
            article.download()
            article.parse()
            print('parsing')

            title = article.title or f"Article {i+1}"
            text = article.text or ""
            print('title:', title, 'text:', text[:100])

            title_chunks = split_text_arabic(title)
            body_chunks = split_text_arabic(text)
            print('Number of title chunks:', len(title_chunks), 'Number of body chunks:', len(body_chunks))

            print("Sending first translation request...")
            translated_title = translate_chunks(title_chunks, batch_size=10)
            print("Finished translating title.")
            translated_body = translate_chunks(body_chunks, batch_size=16)

            print('Translated title:', translated_title)

            records.append({
                "filename": f"article_{i+1}.pdf",
                "url": url,
                "title_translated": " ".join(translated_title),
                "text_translated": "\n\n".join(translated_body)
            })

            print(f"✅ Translated article {i+1}")

        except Exception as e:
            print(f"❌ Failed article {i+1}: {e}")

    # Save to CSV (your exact code)
    df = pd.DataFrame(records)
    df.to_csv("translated_articles.csv", index=False)
    print(df.head())

    # Generate PDFs (your exact code)
    df = pd.read_csv("translated_articles.csv")

    for i, row in df.iterrows():
        pdf = FPDF()
        pdf.add_page()
        pdf.set_auto_page_break(auto=True, margin=15)

        pdf.set_font("Arial", style='B', size=14)
        pdf.multi_cell(0, 10, row['title_translated'])
        pdf.ln()

        pdf.set_font("Arial", size=12)
        pdf.multi_cell(0, 10, row['text_translated'])

        pdf.output(row['filename'])
        print(f"📝 Saved PDF: {row['filename']}")

if __name__ == "__main__":
    main()
