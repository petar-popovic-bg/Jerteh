# Common usecase utils
import os
import shutil
import csv
from humanize import naturalsize


def file_size(file_path):
    """
    this function will return the file size
    """
    if os.path.isfile(file_path):
        file_info = os.stat(file_path)
        return naturalsize(file_info.st_size, gnu=True)


def read_text_file(file):
    """
    Tries to read file with different encodings in following order: utf-8, utf-16-le, latin1

    :param file: string (Path to file)
    :return: string (decoded text)
    """
    try:
        with open(file, 'r', encoding='utf-8') as f:
            text = f.read()
    except UnicodeDecodeError:
        try:
            with open(file, 'r', encoding='utf-16-le') as f:
                text = f.read()
        except UnicodeDecodeError:
            with open(file, 'r', encoding='latin1') as f:
                text = f.read()

    return text


def get_files_from_dir(dir_path, recursion=False, filter_ext=None):
    """
    Returns the list of filepaths in directory. For digging into subfolders use recursion param.

    :param dir_path: string (abs path to dir)
    :param recursion: bool (default: False)
    :param filter_ext: None or List ('.txt', '.doc', '.pdf')
    :return: list
    """
    def list_files_recursive(path):
        """
        Function that receives as a parameter a directory path.

        :param path: string (path to directory)
        :return: list
        """
        _files = []

        # r = root, d = directories, f = files
        for r, d, f in os.walk(path):
            for file in f:
                _files.append(os.path.join(r, file))

        _lst = [file for file in _files]
        return _lst

    if recursion:
        files = list_files_recursive(dir_path)
        _files = []
        if filter_ext is not None:
            for file in files:
                if os.path.splitext(file)[1] in filter_ext:
                    _files.append(file)
            return _files
        else:
            return files
    else:
        files = []
        _files = []
        lst = os.listdir(dir_path)
        for _path in lst:
            if not os.path.isdir(os.path.join(dir_path, _path)):
                files.append(os.path.join(dir_path, _path))

        if filter_ext is not None:
            for file in files:
                if os.path.splitext(file)[1] in filter_ext:
                    _files.append(file)
            return _files
        else:
            return files


def extract_files(src_dir_path, dst_dir_path, filter_ext=None, recursion=False):
    """
    Extract files from one directory to another. Filter with extensions, recursive option.

    :param src_dir_path: string (abs path to source directory)
    :param dst_dir_path: string (abs path to destination directory)
    :param filter_ext: list[string] (list of extensions to filter)
    :param recursion: boolean (Optinal recursive digging through source dir)
    :return: boolean
    """
    files = get_files_from_dir(src_dir_path, recursion=recursion, filter_ext=filter_ext)

    os.mkdir(dst_dir_path)
    for file in files:
        filename = os.path.basename(file)
        shutil.copyfile(file, os.path.join(dst_dir_path, filename))

    return True


def csv_to_dict(csv_file, delimiter='\t'):
    """
    Returns list of dictionaries (keys from header, values from rows).

    :param csv_file: string (path to csv file)
    :param delimiter: string (collumn delimiter, tab default)
    :return: list[dic]
    """
    with open(csv_file, 'r', encoding='utf-8') as f:
        meta = [{k: v for k, v in row.items()} for row in csv.DictReader(f, delimiter=delimiter)]

    return meta


def lod_to_csv(lod, delimiter='\t'):
    """
    Returns string csv file.

    :param dict: list of (flat) dictionary objects
    :param delimiter: string (collumn delimiter, tab default)
    :return: string
    """
    keys = []
    for item in lod:
        for key in item.keys():
            if key not in keys:
                keys.append(key)

    for item in lod:
        for key in keys:
            if key not in item.keys():
                item[key] = ''

    header = sorted(keys)
    lines = []
    for item in lod:
        i_keys = sorted(item.keys())
        lines.append(delimiter.join([str(item[key]) for key in i_keys]))

    return delimiter.join(header) + '\n' + '\n'.join(lines)
