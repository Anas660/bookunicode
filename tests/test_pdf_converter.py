from pdf_converter import PdfConverter
from ocr_processor import OcrProcessor
from docx_generator import DocxGenerator

def test_pdf_converter():
    pdf_converter = PdfConverter()
    images = pdf_converter.extract_images("data/input_pdfs/sample.pdf")
    assert len(images) > 0  # Ensure images are extracted

def test_ocr_processor():
    ocr_processor = OcrProcessor()
    text = ocr_processor.perform_ocr("data/temp_images/sample_image.png")
    assert isinstance(text, str)  # Ensure the output is a string
    assert len(text) > 0  # Ensure some text is extracted

def test_docx_generator():
    docx_generator = DocxGenerator()
    success = docx_generator.create_docx("data/output_docx/sample.docx", "Sample Unicode Text")
    assert success is True  # Ensure the DOCX file is created successfully