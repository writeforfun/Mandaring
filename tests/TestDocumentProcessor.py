import unittest
from src.DocumentProcessor import DocumentProcessor

class TestDocumentProcessor(unittest.TestCase):
    def test_read_file_txt(self):
        processor = DocumentProcessor('tests/test_files/test.txt')
        content = processor.read_file()
        self.assertIsNotNone(content)
        self.assertIsInstance(content, str)
        self.assertTrue(content.strip()) 

    def test_read_file_docx(self):
        processor = DocumentProcessor('tests/test_files/test.docx')
        content = processor.read_file()
        self.assertIsNotNone(content)
        self.assertIsInstance(content, str)
        self.assertTrue(content.strip()) 

    def test_read_file_pdf(self):
        processor = DocumentProcessor('tests/test_files/test.pdf')
        content = processor.read_file()
        self.assertIsNotNone(content)
        self.assertIsInstance(content, str)
        self.assertTrue(content.strip()) 

if __name__ == "__main__":
    unittest.main()
