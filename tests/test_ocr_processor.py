from ocr_processor import OcrProcessor
import unittest

class TestOcrProcessor(unittest.TestCase):

    def setUp(self):
        self.ocr_processor = OcrProcessor()

    def test_extract_text_from_image(self):
        # Assuming you have a test image in the temp_images directory
        test_image_path = 'data/temp_images/test_image.png'
        extracted_text = self.ocr_processor.extract_text_from_image(test_image_path)
        self.assertIsInstance(extracted_text, str)
        self.assertGreater(len(extracted_text), 0)

    def test_process_image(self):
        # Test the process_image method with a sample image
        test_image_path = 'data/temp_images/test_image.png'
        processed_text = self.ocr_processor.process_image(test_image_path)
        self.assertIsInstance(processed_text, str)
        self.assertGreater(len(processed_text), 0)

if __name__ == '__main__':
    unittest.main()