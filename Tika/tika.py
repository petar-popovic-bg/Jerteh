import tika
from tika import parser

tika.initVM()


def extract_text(file):
    return parser.from_file(file)['content']
