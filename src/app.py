from dotenv import load_dotenv
from pdf_converter import PdfConverter
from ocr_processor import OcrProcessor
from docx_generator import DocxGenerator
from text_enhancer import TextEnhancer
import os
import shutil

# Load environment variables from .env file
load_dotenv()

def main():
    # Change paths to be relative to the project root
    input_pdf_path = "data/input_pdfs" 
    output_docx_path = "data/output_docx"  
    temp_images_path = "data/temp_images"

    # Create all directories if they don't exist
    os.makedirs(input_pdf_path, exist_ok=True)
    os.makedirs(output_docx_path, exist_ok=True)
    os.makedirs(temp_images_path, exist_ok=True)

    # Check if we have PDF files
    pdf_files = [f for f in os.listdir(input_pdf_path) if f.lower().endswith('.pdf')]
    if not pdf_files:
        print(f"No PDF files found in {input_pdf_path}. Please add PDF files to process.")
        return

    # Process each PDF in the input directory
    for pdf_file in pdf_files:
        pdf_path = os.path.join(input_pdf_path, pdf_file)
        print(f"Processing PDF: {pdf_path}")

        # Convert PDF to images
        pdf_converter = PdfConverter(pdf_path, temp_images_path)
        image_files = pdf_converter.convert_pdf_to_images()

        # Perform OCR on the images
        ocr_processor = OcrProcessor(image_files)
        raw_text = ocr_processor.extract_text()
        
        # Enhance text with Gemini
        book_title = os.path.splitext(pdf_file)[0]
        enhancer = TextEnhancer()
        enhanced_text = enhancer.enhance_urdu_text(raw_text, book_title)

        # Generate DOCX file from the enhanced text
        docx_generator = DocxGenerator(enhanced_text, output_docx_path)
        docx_generator.create_docx(pdf_file.replace('.pdf', '.docx'))

        print(f"✅ Enhanced DOCX file created: {pdf_file.replace('.pdf', '.docx')}")
        
        # Clean up temporary image files
        for image_file in image_files:
            if os.path.exists(image_file):
                os.remove(image_file)
                
        print(f"✅ Temporary image files cleaned up")

if __name__ == "__main__":
    main()