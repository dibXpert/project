import os
import pyttsx3
from pypdf import PdfReader
import docx


# check if file and extension exist
def check_file_existence_and_extension(file_location):
    if not os.path.exists(file_location):
        return False, "File does not exist."

    file_extension = os.path.splitext(file_location)[-1].lower()
    if file_extension not in [".txt", ".docx", ".pdf"]:
        return False, "Unsupported file extension."

    return True, file_extension


# read .txt content
def read_txt(file_location):
    with open(file_location, "r") as file:
        text = file.read()
    return text, file_location


# read .docx content
def read_docx(file_location):
    doc = docx.Document(file_location)
    text = "\n".join([para.text for para in doc.paragraphs])
    return text, file_location


# read .pdf content
def read_pdf(file_location):
    text = ""
    pdf_reader = PdfReader(file_location)
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text, file_location


# save audio to mp3
def save_audio(text, file_location):
    # naming the .mp3 file
    file_base = os.path.splitext(os.path.basename(file_location))[0]
    mp3_file_name = f"{file_base}.mp3"

    counter = 1
    while os.path.exists(mp3_file_name):
        mp3_file_name = f"{file_base}{counter}.mp3"
        counter += 1

    # text-to-speech
    engine = pyttsx3.init()
    engine.save_to_file(text, mp3_file_name)
    engine.runAndWait()
    return mp3_file_name


def main():
    # ask for file
    file_location = input("Enter file location [.txt, .docx, .pdf]: ")
    exists, error_message = check_file_existence_and_extension(file_location)

    if exists:
        if file_location.endswith(".txt"):
            text, file_location = read_txt(file_location)
        elif file_location.endswith(".docx"):
            text, file_location = read_docx(file_location)
        elif file_location.endswith(".pdf"):
            text, file_location = read_pdf(file_location)

        mp3_file_name = save_audio(text, file_location)
        print(f"Audio saved as {mp3_file_name}")

    else:
        print(error_message)


if __name__ == "__main__":
    main()
