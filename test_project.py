import os
import project
import docx

# read_pdf has problem to test
from project import check_file_existence_and_extension


def test_check_file_existence_and_extension():
    # Test with a non-existing file
    exists, error_message = check_file_existence_and_extension("non_existing_file.txt")
    assert not exists
    assert error_message == "File does not exist."


def test_read_txt():
    # Create a temporary test .txt file
    test_text = "This is a test text file."
    with open("test.txt", "w") as file:
        file.write(test_text)

    # Test reading the .txt file
    text, _ = project.read_txt("test.txt")
    assert text == test_text

    # Clean up the temporary file
    os.remove("test.txt")


def test_read_docx():
    # Create a temporary test .docx file
    test_docx = "This is a test docx file."
    doc = docx.Document()
    doc.add_paragraph(test_docx)
    doc.save("test.docx")

    # Test reading the .docx file
    text, _ = project.read_docx("test.docx")
    assert text.strip() == test_docx

    # Clean up the temporary file
    os.remove("test.docx")
