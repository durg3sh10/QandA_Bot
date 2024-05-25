import pdfplumber

def extract_text_from_pdf(pdf_path, chunk_size=70000):
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text()
    chunks = [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]
    #print("Len of chunkss" ,len(chunks))
    return chunks
