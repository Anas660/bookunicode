from google.cloud import vision
import os
import io

class OcrProcessor:
    def __init__(self, image_files):
        self.image_files = image_files
        
    def extract_text(self):
        """Extract text from images using Google Cloud Vision API"""
        print("Performing OCR on images using Google Cloud Vision...")
        
        # Instantiate a client
        client = vision.ImageAnnotatorClient()
        
        all_text = []
        for image_file in self.image_files:
            try:
                # Read image file
                with io.open(image_file, 'rb') as image_file_obj:
                    content = image_file_obj.read()
                
                image = vision.Image(content=content)
                
                # Perform text detection with language hints for Urdu
                image_context = vision.ImageContext(language_hints=["ur"])
                response = client.document_text_detection(
                    image=image, 
                    image_context=image_context
                )
                
                # Get full text annotation
                text = response.full_text_annotation.text
                if text:
                    all_text.append(text)
                    print(f"OCR completed for {os.path.basename(image_file)}")
                else:
                    print(f"No text detected in {os.path.basename(image_file)}")
                
                if response.error.message:
                    print(f"Error: {response.error.message}")
                    
            except Exception as e:
                print(f"Error processing {image_file}: {str(e)}")
        
        # Join all text with double newlines between pages
        return "\n\n".join(all_text)