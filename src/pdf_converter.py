from pdf2image import convert_from_path
import os

class PdfConverter:
    def __init__(self, pdf_path, output_dir):
        self.pdf_path = pdf_path
        self.output_dir = output_dir
        os.makedirs(output_dir, exist_ok=True)
        
    def convert_pdf_to_images(self):
        """Convert PDF pages to images"""
        print(f"Converting PDF to images: {self.pdf_path}")
        
        # Extract filename without extension
        base_filename = os.path.basename(self.pdf_path).rsplit('.', 1)[0]
        
        # Specify poppler path directly
        poppler_path = r"C:\Program Files\poppler\Library\bin"
        
        # Convert PDF to images with explicit poppler path
        images = convert_from_path(
            self.pdf_path,
            poppler_path=poppler_path
        )
        
        # Save images to output directory
        image_files = []
        for i, image in enumerate(images):
            image_path = os.path.join(self.output_dir, f"{base_filename}_page_{i+1}.jpg")
            image.save(image_path, "JPEG")
            image_files.append(image_path)
            
        print(f"Created {len(image_files)} images")
        return image_files

    def extract_images(self):
        return self.convert_pdf_to_images()