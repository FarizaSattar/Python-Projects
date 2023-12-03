import PyPDF2
from gtts import gTTS
import os

def pdf_to_text(pdf_file):
    # Open the PDF file
    with open(pdf_file, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        num_pages = len(pdf_reader.pages)

        text = ''
        # Extract text from each page
        for page_num in range(num_pages):
            page = pdf_reader.getPage(page_num)
            text += page.extractText()

    return text

def text_to_speech(text):
    # Convert text to speech using gTTS
    tts = gTTS(text=text, lang='en')

    # Save the speech as an audio file
    tts.save("output.mp3")

    # Play the speech using the default audio player
    os.system("output.mp3")

if __name__ == "__main__":
    # Replace 'input.pdf' with the path to your PDF file
    pdf_file_path = 'input.pdf'

    # Extract text from the PDF
    extracted_text = pdf_to_text(pdf_file_path)

    # Convert extracted text to speech
    text_to_speech(extracted_text)
