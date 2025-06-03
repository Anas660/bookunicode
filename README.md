# Urdu PDF to DOCX Converter

Convert Urdu PDF files to editable DOCX documents with Unicode text! This project leverages advanced OCR using Google Cloud Vision API and Gemini AI for proofreading, ensuring high-quality and accurate output.

---

## Features

- **PDF to Image Conversion:** Extracts high-quality images from PDF files
- **Google Cloud Vision OCR:** Accurate Urdu text recognition
- **Gemini AI Proofreading:** Corrects OCR errors while preserving 100% of content
- **Unicode Text Generation:** Outputs properly formatted Urdu Unicode text
- **DOCX File Creation:** Saves results as editable Microsoft Word documents
- **Automatic Cleanup:** Removes temporary image files after processing

---

## Project Structure

```
urdu-pdf-to-docx
├── src
│   ├── app.py                # Main entry point for the application
│   ├── pdf_converter.py      # Handles extraction of images from PDF files
│   ├── ocr_processor.py      # Performs OCR on extracted images
│   ├── docx_generator.py     # Generates DOCX files from extracted text
│   └── text_enhancer.py      # AI text enhancement with Gemini
├── data
│   ├── input_pdfs            # Directory for input PDF files
│   ├── temp_images           # Temporary storage for extracted images
│   └── output_docx           # Directory for generated DOCX files
├── requirements.txt          # Project dependencies
├── .gitignore                # Files and directories to ignore by Git
├── README.md                 # Project documentation
└── .env                      # Environment variables
```

---

## System Requirements

- Python 3.8+
- Windows/Linux/MacOS

**External tools:**
- [Poppler](https://poppler.freedesktop.org/) (for PDF processing)
- Google Cloud account (for Vision API)
- Google AI Studio account (for Gemini API)
- Internet connection (for API access)

---

## Installation Steps

1. **Clone the repository**
    ```bash
    git clone <repository-url>
    cd urdu-pdf-to-docx
    ```

2. **Install Python dependencies**
    ```bash
    pip install -r requirements.txt
    ```
    *(Or manually: `pip install python-docx pdf2image google-cloud-vision google-generativeai python-dotenv`)*

3. **Install Poppler**

    - **Windows:**
        - Download from [poppler-windows](http://blog.alivate.com.au/poppler-windows/)
        - Extract to `C:\Program Files\poppler`
        - Add `C:\Program Files\poppler\Library\bin` to your PATH

    - **Linux:**
        ```bash
        sudo apt-get install poppler-utils
        ```

    - **MacOS:**
        ```bash
        brew install poppler
        ```

4. **Set up Google Cloud Vision API**
    - Create a Google Cloud project
    - Enable the Vision API
    - Create a service account & download JSON credentials
    - Place credentials file in the project directory

5. **Set up Gemini API**
    - Get API key from [Google AI Studio](https://aistudio.google.com/)

6. **Configure environment variables**
    - Create a `.env` file with:
    ```
    GOOGLE_APPLICATION_CREDENTIALS=path/to/your-google-credentials.json
    GEMINI_API_KEY=your-gemini-api-key
    ```

7. **Create directory structure**
    ```bash
    mkdir -p data/input_pdfs data/temp_images data/output_docx
    ```

---

## Usage

1. **Add PDF files:** Place Urdu PDF files in `data/input_pdfs` directory

2. **Run the converter:**
    ```bash
    python src/app.py
    ```

3. **Get results:** Find processed DOCX files in the `data/output_docx` directory

---

## How It Works

- **PDF Processing:** PDF files are converted to high-quality images using pdf2image and Poppler
- **OCR Processing:** Google Cloud Vision API extracts Urdu text from the images
- **Text Enhancement:** Gemini AI proofreads and corrects OCR errors while preserving content
- **Document Creation:** Final text is formatted and saved as DOCX files

---

## Troubleshooting

- **Missing Poppler:** Error about PDF2Image or Poppler not found  
  _Solution:_ Verify Poppler installation and PATH configuration

- **Authentication Error:** Issues with Google Cloud or Gemini API  
  _Solution:_ Check credentials files and environment variables

- **OCR Quality:** Poor text recognition  
  _Solution:_ Ensure PDF is high quality; try different OCR settings

---

## Contributing

Contributions are welcome! Please submit a pull request or open an issue for any enhancements or bug fixes.

---

## License

This project is licensed under the MIT License.
