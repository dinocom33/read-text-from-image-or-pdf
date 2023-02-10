from PIL import Image
from pytesseract import pytesseract
from PyPDF2 import PdfReader

path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


def read_image():
    print("Please enter the path to the image: ")
    image_path = input("Path: ")
    img = Image.open(image_path)
    pytesseract.tesseract_cmd = path_to_tesseract
    text = pytesseract.image_to_string(img)

    write_file(text)


def read_pdf():
    print("Please enter the path to the PDF: ")
    pdf_path = input("Path: ")
    reader = PdfReader(pdf_path)
    print(f"Number of pages to read: {len(reader.pages)}")
    page = reader.pages[len(reader.pages) - 1]
    text = page.extract_text()

    write_file(text)


def write_file(text):
    # print("Please enter the file name: ")
    # file_name = input()
    with open("output.txt", "w") as file:
        file.writelines(text)


while True:
    print("What format will it be read from?\n1. Image\n2. PDF")

    try:
        choice = int(input("Your choice: "))
    except ValueError:
        print("The input must be a digit! Please try again.")
        continue

    if choice != 1 and choice != 2:
        print("Incorrect input! Please try again.")
    elif choice == 1:
        read_image()
        break
    elif choice == 2:
        read_pdf()
        break
