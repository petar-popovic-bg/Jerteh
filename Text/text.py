# Operations on raw text (string) data
import re


def convert_xml(tree, translator):
    """
    Iterates over xml tree and executes translator function on text nodes.

    :param tree: ElementTree
    :param translator: func (cyr_to_lat, asc_to_lat, ...)
    :return: ElementTree
    """
    for elem in tree.iter():
        if elem.text is not None:
            elem.text = translator(elem.text)

    return tree


def strip_xml(text, erase_newlines=True, save_tags=None):
    """
    Strip xml annotation from a text string.

    :param text: string
    :param erase_newlines: Boolean
    :param save_tags List ['<p>', '</p>', '<seg>', '</seg>', ...]
    :return: string
    """
    if erase_newlines:
        control = 12
    else:
        control = 11

    mpa = dict.fromkeys(range(0, control), " ")
    mpa.update(dict.fromkeys(range(12, 32), " "))
    text = text.translate(mpa)
    text = text.replace('<', '\n<').replace('>', '>\n')
    text = re.sub(r' +', ' ', text)
    text = re.sub(r'\n+', '\n', text)
    text = text.replace('\n \n', '\n').replace(' \n ', '\n')
    text = re.sub(r'\n+', '\n', text)

    text_lines = text.split('\n')

    del text

    novi_text_lines = []

    if save_tags is not None:
        for idx, line in enumerate(text_lines):
            if re.match(r'^.*<!--.*$|^.*-->.*$|^.*<.*>.*$', line) and line not in save_tags:
                pass
            else:
                novi_text_lines.append(text_lines[idx])
    else:
        for idx, line in enumerate(text_lines):
            if re.match(r'^.*<!--.*$|^.*-->.*$|^.*<.*>.*$', line):
                pass
            else:
                novi_text_lines.append(text_lines[idx])

    return '\n'.join(novi_text_lines)


def strip_newlines(text):
    """
    Strips leading, tailing, and inbetween multiple newline characters.

    :param text: string
    :return: string
    """
    text = text.strip('\n')
    text = re.sub(r'[\r\n]+', '\n', text)
    return text


def clean_for_xml_parser(text):
    text = text.replace('&', '&amp;')
    text = text.replace('<', '&lt;')
    text = text.replace('>', '&gt;')
    return text


def format_xml(root):
    """
    Iterates over xml Element (root) children and removes trailing and preceeding space and tab characters

    :param root: ElementTree
    :return: ElementTree
    """
    for element in root.iter():
        if element.text is not None:
            element.text = element.text.rstrip(' ').rstrip('\t')
            element.text = element.text.lstrip(' ').lstrip('\t')
    return root


def cyr_to_lat(text):
    """
    Converts sr-cyrillic script to sr-latin.

    :param text: string
    :return: string
    """
    dic = {
        '??': 'Lj',
        '??': 'Nj',
        '??': 'D??',
        '??': 'A',
        '??': 'B',
        '??': 'V',
        '??': 'G',
        '??': 'D',
        '??': '??',
        '??': 'E',
        '??': '??',
        '??': 'Z',
        '??': 'I',
        '??': 'J',
        '??': 'K',
        '??': 'L',
        '??': 'M',
        '??': 'N',
        '??': 'O',
        '??': 'P',
        '??': 'R',
        '??': 'S',
        '??': 'T',
        '??': '??',
        '??': 'U',
        '??': 'F',
        '??': 'H',
        '??': 'C',
        '??': '??',
        '??': '??',
        '??': 'lj',
        '??': 'nj',
        '??': 'd??',
        '??': 'a',
        '??': 'b',
        '??': 'v',
        '??': 'g',
        '??': 'd',
        '??': '??',
        '??': 'e',
        '??': '??',
        '??': 'z',
        '??': 'i',
        '??': 'j',
        '??': 'k',
        '??': 'l',
        '??': 'm',
        '??': 'n',
        '??': 'o',
        '??': 'p',
        '??': 'r',
        '??': 's',
        '??': 't',
        '??': '??',
        '??': 'u',
        '??': 'f',
        '??': 'h',
        '??': 'c',
        '??': '??',
        '??': '??'
    }
    for key in dic.keys():
        text = text.replace(key, dic[key])
    return text


def lat_to_cyr(text):
    """
    Converts sr-latin script to sr-cyrillic.

    :param text: string
    :return: string
    """
    dic = {
        'LJ': '??',
        'NJ': '??',
        'D??': '??',
        'Lj': '??',
        'Nj': '??',
        'D??': '??',
        'A': '??',
        'B': '??',
        'V': '??',
        'G': '??',
        'D': '??',
        '??': '??',
        'E': '??',
        '??': '??',
        'Z': '??',
        'I': '??',
        'J': '??',
        'K': '??',
        'L': '??',
        'M': '??',
        'N': '??',
        'O': '??',
        'P': '??',
        'R': '??',
        'S': '??',
        'T': '??',
        '??': '??',
        'U': '??',
        'F': '??',
        'H': '??',
        'C': '??',
        '??': '??',
        '??': '??',
        'lj': '??',
        'nj': '??',
        'd??': '??',
        'a': '??',
        'b': '??',
        'v': '??',
        'g': '??',
        'd': '??',
        '??': '??',
        'e': '??',
        '??': '??',
        'z': '??',
        'i': '??',
        'j': '??',
        'k': '??',
        'l': '??',
        'm': '??',
        'n': '??',
        'o': '??',
        'p': '??',
        'r': '??',
        's': '??',
        't': '??',
        '??': '??',
        'u': '??',
        'f': '??',
        'h': '??',
        'c': '??',
        '??': '??',
        '??': '??'
    }
    for key in dic.keys():
        text = text.replace(key, dic[key])
    return text


def asc_to_cyr(text):
    """
    Converts ASCII text to sr-cyrillic script.

    :param text: string
    :return: string
    """
    dic = {
        'LX': '??',
        'NX': '??',
        'DY': '??',
        'Lx': '??',
        'Nx': '??',
        'Dy': '??',
        'Dx': '??',
        'Zx': '??',
        'Cx': '??',
        'Cy': '??',
        'Sx': '??',
        'A': '??',
        'B': '??',
        'V': '??',
        'G': '??',
        'D': '??',
        'E': '??',
        'Z': '??',
        'I': '??',
        'J': '??',
        'K': '??',
        'L': '??',
        'M': '??',
        'N': '??',
        'O': '??',
        'P': '??',
        'R': '??',
        'S': '??',
        'T': '??',
        'U': '??',
        'F': '??',
        'H': '??',
        'C': '??',
        'lx': '??',
        'nx': '??',
        'dy': '??',
        'dx': '??',
        'zx': '??',
        'cx': '??',
        'cy': '??',
        'sx': '??',
        'a': '??',
        'b': '??',
        'v': '??',
        'g': '??',
        'd': '??',
        'e': '??',
        'z': '??',
        'i': '??',
        'j': '??',
        'k': '??',
        'l': '??',
        'm': '??',
        'n': '??',
        'o': '??',
        'p': '??',
        'r': '??',
        's': '??',
        't': '??',
        'u': '??',
        'f': '??',
        'h': '??',
        'c': '??'
    }
    for key in dic.keys():
        text = text.replace(key, dic[key])
    return text


def cyr_to_asc(text):
    """
    Converts sr-cyrillic script to ASCII text.

    :param text: string
    :return: string
    """
    dic = {
        '??': 'Lx',
        '??': 'Nx',
        '??': 'Dy',
        '??': 'A',
        '??': 'B',
        '??': 'V',
        '??': 'G',
        '??': 'D',
        '??': 'Dx',
        '??': 'E',
        '??': 'Zx',
        '??': 'Z',
        '??': 'I',
        '??': 'J',
        '??': 'K',
        '??': 'L',
        '??': 'M',
        '??': 'N',
        '??': 'O',
        '??': 'P',
        '??': 'R',
        '??': 'S',
        '??': 'T',
        '??': 'Cx',
        '??': 'U',
        '??': 'F',
        '??': 'H',
        '??': 'C',
        '??': 'Cy',
        '??': 'Sx',
        '??': 'lx',
        '??': 'nx',
        '??': 'dy',
        '??': 'a',
        '??': 'b',
        '??': 'v',
        '??': 'g',
        '??': 'd',
        '??': 'dx',
        '??': 'e',
        '??': 'zx',
        '??': 'z',
        '??': 'i',
        '??': 'j',
        '??': 'k',
        '??': 'l',
        '??': 'm',
        '??': 'n',
        '??': 'o',
        '??': 'p',
        '??': 'r',
        '??': 's',
        '??': 't',
        '??': 'cx',
        '??': 'u',
        '??': 'f',
        '??': 'h',
        '??': 'c',
        '??': 'cy',
        '??': 'sx'
    }
    for key in dic.keys():
        text = text.replace(key, dic[key])
    return text


def asc_to_lat(text):
    """
    Converts ASCII text to sr-latin script.

    :param text: string
    :return: string
    """
    dic = {
        'Dy': 'D??',
        'Lx': 'Lj',
        'Nx': 'Nj',
        'DY': 'D??',
        'LX': 'LJ',
        'NX': 'NJ',
        'lx': 'lj',
        'nx': 'nj',
        'dy': 'd??',
        'Cy': '??',
        'Cx': '??',
        'Zx': '??',
        'Dx': '??',
        'Sx': '??',
        'cy': '??',
        'cx': '??',
        'zx': '??',
        'dx': '??',
        'sx': '??'
    }
    for key in dic.keys():
        text = text.replace(key, dic[key])
    return text


def lat_to_asc(text):
    """
    Converts sr-latin script to ASCII text.

    :param text: string
    :return: string
    """
    dic = {
        'D??': 'Dy',
        'Lj': 'Lx',
        'Nj': 'Nx',
        'D??': 'DY',
        'LJ': 'LX',
        'NJ': 'NX',
        'lj': 'lx',
        'nj': 'nx',
        'd??': 'dy',
        '??': 'Cy',
        '??': 'Cx',
        '??': 'Zx',
        '??': 'Dx',
        '??': 'Sx',
        '??': 'cy',
        '??': 'cx',
        '??': 'zx',
        '??': 'dx',
        '??': 'sx'
    }
    for key in dic.keys():
        text = text.replace(key, dic[key])
    return text


def yusclat_to_lat(text):
    """
    Converts YUSCII latin text to sr-latin script.

    :param text: string
    :return: string
    """
    dic = {
        '~': '??',
        '}': '??',
        '{': '??',
        '`': '??',
        '|': '??',
        '^': '??',
        ']': '??',
        '[': '??',
        '@': '??',
        '\\': '??'
    }
    for key in dic.keys():
        text = text.replace(key, dic[key])
    return text


def yusccyr_to_lat(text):
    """
    Converts YUSCII cyrillic text to sr-latin script.

    :param text: string
    :return: string
    """
    dic = {
        '~': '??',
        '}': '??',
        '{': '??',
        '`': '??',
        '|': '??',
        '^': '??',
        ']': '??',
        '[': '??',
        '@': '??',
        '\\': '??',
        'w': 'nj',
        'W': 'Nj',
        'q': 'lj',
        'Q': 'Lj'
    }
    for key in dic.keys():
        text = text.replace(key, dic[key])
    return text
