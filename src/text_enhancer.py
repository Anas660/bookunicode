import google.generativeai as genai
import os

class TextEnhancer:
    def __init__(self, api_key=None):
        """Initialize with Google API key"""
        if api_key is None:
            api_key = os.getenv("GEMINI_API_KEY")
        
        # Configure the Gemini API
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-1.5-pro')
    
    def enhance_urdu_text(self, raw_text, book_title=None):
        """Enhance OCR text with proofreading and formatting"""
        print("Enhancing text with Gemini API...")
        
        # Create a prompt that instructs Gemini on what to do
        prompt = f"""
        You are an expert Urdu editor specializing in OCR correction. I have OCR-extracted text from an Urdu book that needs proofreading.

        Book Title: {book_title or "Unknown"}
        
        Instructions:
        1. Preserve 100% of the content - do NOT summarize or omit ANY information
        2. Fix all OCR errors while maintaining the exact meaning and wording
        3. Properly format the text with correct paragraph breaks and spacing
        4. Keep ALL content in Urdu exactly as presented
        5. Preserve headings, titles, sections, and chapter structure
        6. Return the complete proofread text without any additional commentary
        7. Do not add any markdown formatting in your response
        
        Here is the complete OCR text that needs proofreading:
        
        {raw_text}
        """
        
        # Get the enhanced text from Gemini
        response = self.model.generate_content(prompt)
        
        # Return the enhanced text
        if response.text:
            print("✅ Text enhancement completed")
            return response.text
        else:
            print("⚠️ Text enhancement failed")
            return raw_text  # Return original if enhancement fails