# Functions for processing files for NoSketch Engine
from xml.etree import ElementTree


def create_doc(text, identifier, meta):
    """
    Enclose text with <doc> </doc> tags and inject metadata into doc element.

    :param text: string
    :param identifier: int
    :param meta: dic
    :return: XML Element
    """
    meta['n'] = str(identifier + 1)
    for key in meta.keys():
        meta[key] = str(meta[key])
    doc = ElementTree.Element('doc', meta)
    doc.text = '\n' + text.strip('\n') + '\n'
    return doc


def compile_vertical(docs):
    """
    Compile vertical file from a list of doc elements that can be compiled with NoSketch Engine.

    :param docs: list[XML Element]
    :return: string
    """
    vertical = ''
    for doc in docs:
        doc_txt = ElementTree.tostring(doc, encoding='unicode')
        vertical = vertical + doc_txt + '\n'
    return vertical
