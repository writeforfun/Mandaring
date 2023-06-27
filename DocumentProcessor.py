import jieba
import docx2txt
from pdfminer.high_level import extract_text
import os
import argparse


class DocumentProcessor:
    def __init__(self, filepath=None):
        self.filepath = filepath
        if filepath is not None:
            self.filetype = os.path.splitext(filepath)[1]
        else:
            self.filetype = ".txt"

    def read_file(self):
        if self.filetype == ".txt":
            if self.filepath is None:
                text = input("Please enter your text: ")
            else:
                with open(self.filepath, "r", encoding="utf8") as file:
                    text = file.read()
        elif self.filetype == ".docx":
            text = docx2txt.process(self.filepath)
        elif self.filetype == ".pdf":
            text = extract_text(self.filepath)
        else:
            raise ValueError("Unsupported file type")
        return text

    def preprocess(self):
        text = self.read_file()
        words = jieba.cut(text)
        return " ".join(words)

# 這是一個使用範例：
# processor = DocumentProcessor()
# processed_text = processor.preprocess()
# print(processed_text)

def main():
    parser = argparse.ArgumentParser(description='讀取並印出文字檔案內容')
    parser.add_argument('filename', help='要讀取的文字檔案名稱')

    args = parser.parse_args()

    with open(args.filename, 'r', encoding='utf-8') as file:
        content = file.read()

    print(content)

if __name__ == "__main__":
    main()