# Operations on raw text (string) data

def strip_xml(text):
    """
    Strip xml annotation from text string.

    :param text: string
    :return: string
    """
    # TODO: Implement xml stripping

    pass
    return text


def convert(text, ctype, direction=""):
    """
    Converts string of text to another string of text.

    :param text: string
    :param ctype: string (_to_)
    :param direction: string
    :return: string
    """
    dic = {}
    if ctype == 'YUSCLATtoLAT':
        dic = {
            '~': 'č',
            '}': 'ć',
            '{': 'š',
            '`': 'ž',
            '|': 'đ',
            '^': 'Č',
            ']': 'Ć',
            '[': 'Š',
            '@': 'Ž',
            '\\': 'Đ'
        }
    if ctype == 'YUSCCYRtoLAT':
        dic = {
            '~': 'č',
            '}': 'ć',
            '{': 'š',
            '`': 'ž',
            '|': 'đ',
            '^': 'Č',
            ']': 'Ć',
            '[': 'Š',
            '@': 'Ž',
            '\\': 'Đ',
            'w': 'nj',
            'W': 'Nj',
            'q': 'lj',
            'Q': 'Lj'
        }
    if ctype == 'LATtoASC':
        dic = {
            'Dž': 'Dy',
            'Lj': 'Lx',
            'Nj': 'Nx',
            'DŽ': 'DY',
            'LJ': 'LX',
            'NJ': 'NX',
            'lj': 'lx',
            'nj': 'nx',
            'dž': 'dy',
            'Č': 'Cy',
            'Ć': 'Cx',
            'Ž': 'Zx',
            'Đ': 'Dx',
            'Š': 'Sx',
            'č': 'cy',
            'ć': 'cx',
            'ž': 'zx',
            'đ': 'dx',
            'š': 'sx'
        }
    if ctype == 'ASCtoLAT':
        dic = {
            'Dy': 'Dž',
            'Lx': 'Lj',
            'Nx': 'Nj',
            'DY': 'DŽ',
            'LX': 'LJ',
            'NX': 'NJ',
            'lx': 'lj',
            'nx': 'nj',
            'dy': 'dž',
            'Cy': 'Č',
            'Cx': 'Ć',
            'Zx': 'Ž',
            'Dx': 'Đ',
            'Sx': 'Š',
            'cy': 'č',
            'cx': 'ć',
            'zx': 'ž',
            'dx': 'đ',
            'sx': 'š'
        }
    if ctype == 'LATtoCYR':
        dic = {
            'LJ': 'Љ',
            'NJ': 'Њ',
            'DŽ': 'Џ',
            'Lj': 'Љ',
            'Nj': 'Њ',
            'Dž': 'Џ',
            'A': 'А',
            'B': 'Б',
            'V': 'В',
            'G': 'Г',
            'D': 'Д',
            'Đ': 'Ђ',
            'E': 'Е',
            'Ž': 'Ж',
            'Z': 'З',
            'I': 'И',
            'J': 'Ј',
            'K': 'К',
            'L': 'Л',
            'M': 'М',
            'N': 'Н',
            'O': 'О',
            'P': 'П',
            'R': 'Р',
            'S': 'С',
            'T': 'Т',
            'Ć': 'Ћ',
            'U': 'У',
            'F': 'Ф',
            'H': 'Х',
            'C': 'Ц',
            'Č': 'Ч',
            'Š': 'Ш',
            'lj': 'љ',
            'nj': 'њ',
            'dž': 'џ',
            'a': 'а',
            'b': 'б',
            'v': 'в',
            'g': 'г',
            'd': 'д',
            'đ': 'ђ',
            'e': 'е',
            'ž': 'ж',
            'z': 'з',
            'i': 'и',
            'j': 'ј',
            'k': 'к',
            'l': 'л',
            'm': 'м',
            'n': 'н',
            'o': 'о',
            'p': 'п',
            'r': 'р',
            's': 'с',
            't': 'т',
            'ć': 'ћ',
            'u': 'у',
            'f': 'ф',
            'h': 'х',
            'c': 'ц',
            'č': 'ч',
            'š': 'ш'
        }
    if ctype == 'CYRtoLAT':
        dic = {
            'Љ': 'Lj',
            'Њ': 'Nj',
            'Џ': 'Dž',
            'А': 'A',
            'Б': 'B',
            'В': 'V',
            'Г': 'G',
            'Д': 'D',
            'Ђ': 'Đ',
            'Е': 'E',
            'Ж': 'Ž',
            'З': 'Z',
            'И': 'I',
            'Ј': 'J',
            'К': 'K',
            'Л': 'L',
            'М': 'M',
            'Н': 'N',
            'О': 'O',
            'П': 'P',
            'Р': 'R',
            'С': 'S',
            'Т': 'T',
            'Ћ': 'Ć',
            'У': 'U',
            'Ф': 'F',
            'Х': 'H',
            'Ц': 'C',
            'Ч': 'Č',
            'Ш': 'Š',
            'љ': 'lj',
            'њ': 'nj',
            'џ': 'dž',
            'а': 'a',
            'б': 'b',
            'в': 'v',
            'г': 'g',
            'д': 'd',
            'ђ': 'đ',
            'е': 'e',
            'ж': 'ž',
            'з': 'z',
            'и': 'i',
            'ј': 'j',
            'к': 'k',
            'л': 'l',
            'м': 'm',
            'н': 'n',
            'о': 'o',
            'п': 'p',
            'р': 'r',
            'с': 's',
            'т': 't',
            'ћ': 'ć',
            'у': 'u',
            'ф': 'f',
            'х': 'h',
            'ц': 'c',
            'ч': 'č',
            'ш': 'š'
        }
    if ctype == 'CYRtoASC':
        dic = {
            'Љ': 'Lx',
            'Њ': 'Nx',
            'Џ': 'Dy',
            'А': 'A',
            'Б': 'B',
            'В': 'V',
            'Г': 'G',
            'Д': 'D',
            'Ђ': 'Dx',
            'Е': 'E',
            'Ж': 'Zx',
            'З': 'Z',
            'И': 'I',
            'Ј': 'J',
            'К': 'K',
            'Л': 'L',
            'М': 'M',
            'Н': 'N',
            'О': 'O',
            'П': 'P',
            'Р': 'R',
            'С': 'S',
            'Т': 'T',
            'Ћ': 'Cx',
            'У': 'U',
            'Ф': 'F',
            'Х': 'H',
            'Ц': 'C',
            'Ч': 'Cy',
            'Ш': 'Sx',
            'љ': 'lx',
            'њ': 'nx',
            'џ': 'dy',
            'а': 'a',
            'б': 'b',
            'в': 'v',
            'г': 'g',
            'д': 'd',
            'ђ': 'dx',
            'е': 'e',
            'ж': 'zx',
            'з': 'z',
            'и': 'i',
            'ј': 'j',
            'к': 'k',
            'л': 'l',
            'м': 'm',
            'н': 'n',
            'о': 'o',
            'п': 'p',
            'р': 'r',
            'с': 's',
            'т': 't',
            'ћ': 'cx',
            'у': 'u',
            'ф': 'f',
            'х': 'h',
            'ц': 'c',
            'ч': 'cy',
            'ш': 'sx'
        }
    if ctype == 'ASCtoCYR':
        dic = {
            'LX': 'Љ',
            'NX': 'Њ',
            'DY': 'Џ',
            'Lx': 'Љ',
            'Nx': 'Њ',
            'Dy': 'Џ',
            'Dx': 'Ђ',
            'Zx': 'Ж',
            'Cx': 'Ћ',
            'Cy': 'Ч',
            'Sx': 'Ш',
            'A': 'А',
            'B': 'Б',
            'V': 'В',
            'G': 'Г',
            'D': 'Д',
            'E': 'Е',
            'Z': 'З',
            'I': 'И',
            'J': 'Ј',
            'K': 'К',
            'L': 'Л',
            'M': 'М',
            'N': 'Н',
            'O': 'О',
            'P': 'П',
            'R': 'Р',
            'S': 'С',
            'T': 'Т',
            'U': 'У',
            'F': 'Ф',
            'H': 'Х',
            'C': 'Ц',
            'lx': 'љ',
            'nx': 'њ',
            'dy': 'џ',
            'dx': 'ђ',
            'zx': 'ж',
            'cx': 'ћ',
            'cy': 'ч',
            'sx': 'ш',
            'a': 'а',
            'b': 'б',
            'v': 'в',
            'g': 'г',
            'd': 'д',
            'e': 'е',
            'z': 'з',
            'i': 'и',
            'j': 'ј',
            'k': 'к',
            'l': 'л',
            'm': 'м',
            'n': 'н',
            'o': 'о',
            'p': 'п',
            'r': 'р',
            's': 'с',
            't': 'т',
            'u': 'у',
            'f': 'ф',
            'h': 'х',
            'c': 'ц'
        }

    if direction == 'back':
        for key in dic.keys():
            text = text.replace(dic[key], key)
    else:
        for key in dic.keys():
            text = text.replace(key, dic[key])

    return text


def cyr_to_lat(text):
    """
    Converts sr-cyrillic script to sr-latin.

    :param text: string
    :return: string
    """
    dic = {
        'Љ': 'Lj',
        'Њ': 'Nj',
        'Џ': 'Dž',
        'А': 'A',
        'Б': 'B',
        'В': 'V',
        'Г': 'G',
        'Д': 'D',
        'Ђ': 'Đ',
        'Е': 'E',
        'Ж': 'Ž',
        'З': 'Z',
        'И': 'I',
        'Ј': 'J',
        'К': 'K',
        'Л': 'L',
        'М': 'M',
        'Н': 'N',
        'О': 'O',
        'П': 'P',
        'Р': 'R',
        'С': 'S',
        'Т': 'T',
        'Ћ': 'Ć',
        'У': 'U',
        'Ф': 'F',
        'Х': 'H',
        'Ц': 'C',
        'Ч': 'Č',
        'Ш': 'Š',
        'љ': 'lj',
        'њ': 'nj',
        'џ': 'dž',
        'а': 'a',
        'б': 'b',
        'в': 'v',
        'г': 'g',
        'д': 'd',
        'ђ': 'đ',
        'е': 'e',
        'ж': 'ž',
        'з': 'z',
        'и': 'i',
        'ј': 'j',
        'к': 'k',
        'л': 'l',
        'м': 'm',
        'н': 'n',
        'о': 'o',
        'п': 'p',
        'р': 'r',
        'с': 's',
        'т': 't',
        'ћ': 'ć',
        'у': 'u',
        'ф': 'f',
        'х': 'h',
        'ц': 'c',
        'ч': 'č',
        'ш': 'š'
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
        'LJ': 'Љ',
        'NJ': 'Њ',
        'DŽ': 'Џ',
        'Lj': 'Љ',
        'Nj': 'Њ',
        'Dž': 'Џ',
        'A': 'А',
        'B': 'Б',
        'V': 'В',
        'G': 'Г',
        'D': 'Д',
        'Đ': 'Ђ',
        'E': 'Е',
        'Ž': 'Ж',
        'Z': 'З',
        'I': 'И',
        'J': 'Ј',
        'K': 'К',
        'L': 'Л',
        'M': 'М',
        'N': 'Н',
        'O': 'О',
        'P': 'П',
        'R': 'Р',
        'S': 'С',
        'T': 'Т',
        'Ć': 'Ћ',
        'U': 'У',
        'F': 'Ф',
        'H': 'Х',
        'C': 'Ц',
        'Č': 'Ч',
        'Š': 'Ш',
        'lj': 'љ',
        'nj': 'њ',
        'dž': 'џ',
        'a': 'а',
        'b': 'б',
        'v': 'в',
        'g': 'г',
        'd': 'д',
        'đ': 'ђ',
        'e': 'е',
        'ž': 'ж',
        'z': 'з',
        'i': 'и',
        'j': 'ј',
        'k': 'к',
        'l': 'л',
        'm': 'м',
        'n': 'н',
        'o': 'о',
        'p': 'п',
        'r': 'р',
        's': 'с',
        't': 'т',
        'ć': 'ћ',
        'u': 'у',
        'f': 'ф',
        'h': 'х',
        'c': 'ц',
        'č': 'ч',
        'š': 'ш'
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
        'LX': 'Љ',
        'NX': 'Њ',
        'DY': 'Џ',
        'Lx': 'Љ',
        'Nx': 'Њ',
        'Dy': 'Џ',
        'Dx': 'Ђ',
        'Zx': 'Ж',
        'Cx': 'Ћ',
        'Cy': 'Ч',
        'Sx': 'Ш',
        'A': 'А',
        'B': 'Б',
        'V': 'В',
        'G': 'Г',
        'D': 'Д',
        'E': 'Е',
        'Z': 'З',
        'I': 'И',
        'J': 'Ј',
        'K': 'К',
        'L': 'Л',
        'M': 'М',
        'N': 'Н',
        'O': 'О',
        'P': 'П',
        'R': 'Р',
        'S': 'С',
        'T': 'Т',
        'U': 'У',
        'F': 'Ф',
        'H': 'Х',
        'C': 'Ц',
        'lx': 'љ',
        'nx': 'њ',
        'dy': 'џ',
        'dx': 'ђ',
        'zx': 'ж',
        'cx': 'ћ',
        'cy': 'ч',
        'sx': 'ш',
        'a': 'а',
        'b': 'б',
        'v': 'в',
        'g': 'г',
        'd': 'д',
        'e': 'е',
        'z': 'з',
        'i': 'и',
        'j': 'ј',
        'k': 'к',
        'l': 'л',
        'm': 'м',
        'n': 'н',
        'o': 'о',
        'p': 'п',
        'r': 'р',
        's': 'с',
        't': 'т',
        'u': 'у',
        'f': 'ф',
        'h': 'х',
        'c': 'ц'
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
        'Љ': 'Lx',
        'Њ': 'Nx',
        'Џ': 'Dy',
        'А': 'A',
        'Б': 'B',
        'В': 'V',
        'Г': 'G',
        'Д': 'D',
        'Ђ': 'Dx',
        'Е': 'E',
        'Ж': 'Zx',
        'З': 'Z',
        'И': 'I',
        'Ј': 'J',
        'К': 'K',
        'Л': 'L',
        'М': 'M',
        'Н': 'N',
        'О': 'O',
        'П': 'P',
        'Р': 'R',
        'С': 'S',
        'Т': 'T',
        'Ћ': 'Cx',
        'У': 'U',
        'Ф': 'F',
        'Х': 'H',
        'Ц': 'C',
        'Ч': 'Cy',
        'Ш': 'Sx',
        'љ': 'lx',
        'њ': 'nx',
        'џ': 'dy',
        'а': 'a',
        'б': 'b',
        'в': 'v',
        'г': 'g',
        'д': 'd',
        'ђ': 'dx',
        'е': 'e',
        'ж': 'zx',
        'з': 'z',
        'и': 'i',
        'ј': 'j',
        'к': 'k',
        'л': 'l',
        'м': 'm',
        'н': 'n',
        'о': 'o',
        'п': 'p',
        'р': 'r',
        'с': 's',
        'т': 't',
        'ћ': 'cx',
        'у': 'u',
        'ф': 'f',
        'х': 'h',
        'ц': 'c',
        'ч': 'cy',
        'ш': 'sx'
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
        'Dy': 'Dž',
        'Lx': 'Lj',
        'Nx': 'Nj',
        'DY': 'DŽ',
        'LX': 'LJ',
        'NX': 'NJ',
        'lx': 'lj',
        'nx': 'nj',
        'dy': 'dž',
        'Cy': 'Č',
        'Cx': 'Ć',
        'Zx': 'Ž',
        'Dx': 'Đ',
        'Sx': 'Š',
        'cy': 'č',
        'cx': 'ć',
        'zx': 'ž',
        'dx': 'đ',
        'sx': 'š'
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
        'Dž': 'Dy',
        'Lj': 'Lx',
        'Nj': 'Nx',
        'DŽ': 'DY',
        'LJ': 'LX',
        'NJ': 'NX',
        'lj': 'lx',
        'nj': 'nx',
        'dž': 'dy',
        'Č': 'Cy',
        'Ć': 'Cx',
        'Ž': 'Zx',
        'Đ': 'Dx',
        'Š': 'Sx',
        'č': 'cy',
        'ć': 'cx',
        'ž': 'zx',
        'đ': 'dx',
        'š': 'sx'
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
        '~': 'č',
        '}': 'ć',
        '{': 'š',
        '`': 'ž',
        '|': 'đ',
        '^': 'Č',
        ']': 'Ć',
        '[': 'Š',
        '@': 'Ž',
        '\\': 'Đ'
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
        '~': 'č',
        '}': 'ć',
        '{': 'š',
        '`': 'ž',
        '|': 'đ',
        '^': 'Č',
        ']': 'Ć',
        '[': 'Š',
        '@': 'Ž',
        '\\': 'Đ',
        'w': 'nj',
        'W': 'Nj',
        'q': 'lj',
        'Q': 'Lj'
    }
    for key in dic.keys():
        text = text.replace(key, dic[key])
    return text
