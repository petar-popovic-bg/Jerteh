# Common usecase utils
import os
import shutil
import csv


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
