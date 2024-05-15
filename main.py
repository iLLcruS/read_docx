import os
from docx import Document
from docx2txt import process


def extract_images_from_docx(docx_path, output_dir):
    if not os.path.exists(docx_path):
        print(f"File {docx_path} doesn't exists.")
        return

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    process(docx_path, output_dir)

    print(f"All images was saved to {output_dir}")


docx_path = 'file.docx'

output_dir = 'images'

extract_images_from_docx(docx_path, output_dir)
