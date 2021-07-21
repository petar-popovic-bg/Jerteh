import tika
from tika import parser
import re

# Initializes Java Virtual Machine in order to run Tika server.
tika.initVM()


def extract_text(file):
    """
    Extract text from a file using Apache Tika software which runs on Java. Requires Java runtime to be installed. Reads
    different file formats like .pdf, .doc, .docx, etc.

    :param file: string (Path to file to read)
    :return: string (Extracted text)
    """
    text = parser.from_file(file)['content']
    text = text.strip('\n')
    text = re.sub(r'PAGE\s*[\r\n]+\d+', '', text)
    text = re.sub(r'[\r\n]+', '\n', text)
    return text
