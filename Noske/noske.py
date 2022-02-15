# Functions for processing files for NoSketch Engine
from xml.etree import ElementTree
from xml.etree.ElementTree import Element
from Utils.utils import csv_to_dict


def create_doc(text, identifier, meta):
    """
    Enclose text with <doc> </doc> tags and inject metadata into doc element.

    :param text: string
    :param identifier: int
    :param meta: dict
    :return: XML Element
    """
    meta['n'] = str(identifier + 1)
    for key in meta.keys():
        meta[key] = str(meta[key])
    doc = ElementTree.Element('doc', meta)
    doc.text = '\n' + text.strip('\n') + '\n'
    return doc


def create_doc_from_xml(root_elem, identifier, meta):
    """
    Enclose xml root (<data>...</data>) and inject metadata into doc element.

    :param root_elem: XML Element root element containing data (p, seg, header, ...)
    :param identifier: int
    :param meta: dict metadata to insert into doc
    :return: XML Element
    """
    meta['n'] = str(identifier + 1)
    for key in meta.keys():
        meta[key] = str(meta[key])
    doc = ElementTree.Element('doc', meta)
    doc.append(root_elem)
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


def update_vertical_meta(vertical, update_with, match_by, new_vertical):
    """
    Update compiled vertical file doc attributes with new metadata. Creates new file

    :param vertical: string (path to vertical file)
    :param update_with: string (path to file with metadata to update from)
    :param match_by: string (attribut key to match docs)
    :param new_vertical: string (path to vertical file)
    """
    with open(vertical) as f:
        xml_object = ElementTree.fromstringlist(['<root>', f.read(), '</root>'])
    new_meta = csv_to_dict(update_with)

    with open(new_vertical, 'w') as g:
        for idx, doc in enumerate(xml_object):
            new_doc_meta = next((item for item in new_meta if item[match_by] == doc.attrib[match_by]), None)
            if new_doc_meta is not None:
                for key, value in new_doc_meta.items():
                    if value is None:
                        new_doc_meta[key] = ''
                doc.attrib.update(new_doc_meta)
            doc_str = ElementTree.tostring(doc, encoding='unicode')
            g.write(doc_str)
            g.flush()


def get_doc_meta(doc: Element):
    return doc.attrib


def update_doc_meta(doc: Element, new_meta: dict) -> None:
    doc.attrib.update(new_meta)
