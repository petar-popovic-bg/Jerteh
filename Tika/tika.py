import tika
from tika import parser

# Initializes Java Virtual Machine in order to run Tika server.
tika.initVM()


def extract_text(file):
    """
    Extract text from a file usinf Apache Tika software which runs on Java. Requires Java runtime to be installed.

    :param file: string (Path to file)
    :return: string (Extracted text)
    """
    return parser.from_file(file)['content']
