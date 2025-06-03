import unittest
from src.docx_generator import DocxGenerator

class TestDocxGenerator(unittest.TestCase):

    def setUp(self):
        self.docx_generator = DocxGenerator()
        self.test_text = "یہ ایک ٹیسٹ ہے"  # Sample Urdu text
        self.output_file = "data/output_docx/test_output.docx"

    def test_create_docx(self):
        self.docx_generator.create_docx(self.test_text, self.output_file)
        # Check if the file was created
        self.assertTrue(os.path.exists(self.output_file))

    def test_docx_content(self):
        self.docx_generator.create_docx(self.test_text, self.output_file)
        # Check if the content of the DOCX file is correct
        doc = Document(self.output_file)
        self.assertEqual(doc.paragraphs[0].text, self.test_text)

    def tearDown(self):
        # Clean up the created DOCX file after tests
        if os.path.exists(self.output_file):
            os.remove(self.output_file)

if __name__ == '__main__':
    unittest.main()