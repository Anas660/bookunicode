from docx import Document
import os

class DocxGenerator:
    def __init__(self, text, output_dir):
        self.text = text
        self.output_dir = output_dir
        os.makedirs(output_dir, exist_ok=True)
        
    def create_docx(self, filename):
        """Create DOCX document from text"""
        print(f"Creating DOCX file: {filename}")
        
        # Create a new Document
        document = Document()
        
        # Add the extracted text
        document.add_paragraph(self.text)
        
        # Save the document
        output_path = os.path.join(self.output_dir, filename)
        document.save(output_path)
        
        return output_path