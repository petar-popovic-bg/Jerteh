import re
import os
import sys
import shutil
from config import unitex_dir
from Utils.utils import read_text_file

"""
USAGE:
1. Initialize Unitex object
2. Get data with get_stats() method
"""


class Unitex:
    def __init__(self, lang, silent=False):
        """
        Initializes Unitex class and performs Unitex processing.

        :param lang: string ('English', 'Serbian-Latin', 'Serbian-Cyrillic'...) must correspond Unitex folder
        """

        self.UNITEX_DIR = unitex_dir
        self.lang = lang
        self.silent = silent
        dic_dir = unitex_dir + '/' + lang + '/Dela'
        dic_list = os.listdir(dic_dir)
        dic_list = [dic_dir + '/' + dic_file for dic_file in dic_list if dic_file.endswith('.bin')]
        self.dic_list_str = '"' + '" "'.join(dic_list) + '"'

    @staticmethod
    def cleanup(snt_dir, snt_f):
        """
        Removes directories and files created by Unitex.

        :param snt_dir: string (abs path to snt dir created by Unitex)
        :param snt_f: string (abs path to snt file created by Unitex)
        :return: Boolean
        """
        try:
            shutil.rmtree(snt_dir)
            os.remove(snt_f)
            if os.path.isfile(os.path.join(os.getcwd(), 'utx_tmp.txt')):
                os.remove(os.path.join(os.getcwd(), 'utx_tmp.txt'))
            return True
        except Exception as e:
            print(str(e))
            return False

    def __get_stats_silent(self, file=None, text=None):
        """
            Retrieves results of processing the text compiled to a dictionary.

            :param file: string (Path to file)
            :param text: string (Text to analyze)
            :return: dic
        """
        if text is not None:
            file = os.path.join(os.getcwd(), 'utx_tmp.txt')
            with open(file, 'w') as f:
                f.write(text)
        _filepath, file_extension = os.path.splitext(file)
        snt_dir = _filepath + '_snt'
        snt_f = _filepath + '.snt'

        os.system('mkdir "%s"' % snt_dir)
        os.system('%s/App/UnitexToolLogger Normalize "%s" -r"%s/%s/Norm.txt" --output_offsets="%s/normalize.out.'
                  'offsets" -qutf8-no-bom > /dev/null 2>&1' % (self.UNITEX_DIR, file, self.UNITEX_DIR, self.lang, snt_dir))
        os.system('%s/App/UnitexToolLogger Grf2Fst2 "%s/%s/Graphs/Preprocessing/Sentence/Sentence.grf" -y '
                  '--alphabet="%s/%s/Alphabet.txt" -qutf8-no-bom > /dev/null 2>&1' % (self.UNITEX_DIR, self.UNITEX_DIR, self.lang,
                                                                     self.UNITEX_DIR, self.lang))
        os.system('%s/App/UnitexToolLogger Flatten "%s/%s/Graphs/Preprocessing/Sentence/Sentence.fst2" --rtn -d5'
                  ' -qutf8-no-bom > /dev/null 2>&1' % (self.UNITEX_DIR, self.UNITEX_DIR, self.lang))
        os.system('%s/App/UnitexToolLogger Fst2Txt -t"%s" "%s/%s/Graphs/Preprocessing/Sentence/Sentence.fst2" '
                  '-a"%s/%s/Alphabet.txt" -M --input_offsets="%s/normalize.out.offsets" --output_offsets="%s/normalize.'
                  'out.offsets" -qutf8-no-bom > /dev/null 2>&1' % (self.UNITEX_DIR, snt_f, self.UNITEX_DIR, self.lang,
                                                  self.UNITEX_DIR, self.lang, snt_dir, snt_dir))
        os.system('%s/App/UnitexToolLogger Grf2Fst2 "%s/%s/Graphs/Preprocessing/Replace/Replace.grf" -y '
                  '--alphabet="%s/%s/Alphabet.txt" -qutf8-no-bom > /dev/null 2>&1' % (self.UNITEX_DIR, self.UNITEX_DIR, self.lang,
                                                                     self.UNITEX_DIR, self.lang))
        os.system('%s/App/UnitexToolLogger Fst2Txt -t"%s" "%s/%s/Graphs/Preprocessing/Replace/Replace.fst2" '
                  '-a"%s/%s/Alphabet.txt" -R --input_offsets="%s/normalize.out.offsets" --output_offsets="%s/normalize.'
                  'out.offsets" -qutf8-no-bom > /dev/null 2>&1' % (self.UNITEX_DIR, snt_f, self.UNITEX_DIR, self.lang,
                                                  self.UNITEX_DIR, self.lang, snt_dir, snt_dir))
        os.system('%s/App/UnitexToolLogger Tokenize "%s" -a"%s/%s/Alphabet.txt" --input_offsets="%s/normalize.'
                  'out.offsets" --output_offsets="%s/tokenize.out.offsets" -qutf8-no-bom > /dev/null 2>&1' % (self.UNITEX_DIR, snt_f,
                                                                                             self.UNITEX_DIR, self.lang,
                                                                                             snt_dir, snt_dir))
        if self.lang == 'Serbian-Latin':
            os.system('%s/App/UnitexToolLogger Dico -t"%s" -a"%s/%s/Alphabet.txt" %s "%s/%s/Dela/NewBrojSlovima.'
                      'fst2" "%s/%s/Dela/NewBrojSlovima_norm-z.fst2" -qutf8-no-bom > /dev/null 2>&1' % (self.UNITEX_DIR, snt_f,
                                                                                       self.UNITEX_DIR, self.lang,
                                                                                       self.dic_list_str,
                                                                                       self.UNITEX_DIR, self.lang,
                                                                                       self.UNITEX_DIR, self.lang))
        elif self.lang == 'Serbian-Cyrillic':
            os.system('%s/App/UnitexToolLogger Dico -t"%s" -a"%s/%s/Alphabet.txt" %s "%s/%s/Dela/NewBrojSlovima.'
                      'fst2" "%s/%s/Dela/NewBrojSlovima_norm-z.fst2" -qutf8-no-bom > /dev/null 2>&1' % (self.UNITEX_DIR, snt_f,
                                                                                       self.UNITEX_DIR, self.lang,
                                                                                       self.dic_list_str,
                                                                                       self.UNITEX_DIR, self.lang,
                                                                                       self.UNITEX_DIR, self.lang))
        else:
            os.system('%s/App/UnitexToolLogger Dico -t"%s" -a"%s/%s/Alphabet.txt" "%s/%s/Dela/dela-en-public.bin" '
                      '"%s/%s/Dela/Dnum.fst2" -qutf8-no-bom > /dev/null 2>&1' % (self.UNITEX_DIR, snt_f, self.UNITEX_DIR, self.lang,
                                                                self.UNITEX_DIR, self.lang, self.UNITEX_DIR, self.lang))
        os.system('%s/App/UnitexToolLogger SortTxt "%s/dlf" -l"%s/dlf.n" -o"%s/%s/Alphabet_sort.txt" -qutf8-no-bom > /dev/null 2>&1' %
                  (self.UNITEX_DIR, snt_dir, snt_dir, self.UNITEX_DIR, self.lang))
        os.system('%s/App/UnitexToolLogger SortTxt "%s/dlc" -l"%s/dlc.n" -o"%s/%s/Alphabet_sort.txt" -qutf8-no-bom > /dev/null 2>&1' %
                  (self.UNITEX_DIR, snt_dir, snt_dir, self.UNITEX_DIR, self.lang))
        os.system('%s/App/UnitexToolLogger SortTxt "%s/err" -l"%s/err.n" -o"%s/%s/Alphabet_sort.txt" -qutf8-no-bom > /dev/null 2>&1' %
                  (self.UNITEX_DIR, snt_dir, snt_dir, self.UNITEX_DIR, self.lang))
        os.system('%s/App/UnitexToolLogger SortTxt "%s/tags_err" -l"%s/tags_err.n" -o"%s/%s/Alphabet_sort.txt" '
                  '-qutf8-no-bom > /dev/null 2>&1' % (self.UNITEX_DIR, snt_dir, snt_dir, self.UNITEX_DIR, self.lang))
        with open(snt_dir + '/stats.n', 'r', encoding='utf-8') as f:
            stats_s = f.read()
        stats_reg = re.search(r'(.*) sentence delimiters?, (.*) tokens?, (.*) simple forms?, (.*) digits?', stats_s)
        with open(snt_dir + '/err.n', 'r', encoding='utf-8') as f:
            err_n = f.read().strip()
        if stats_reg and err_n:
            sent_del = stats_reg.group(1)
            tokens = stats_reg.group(2).split(' ')[0]
            unique_tokens = stats_reg.group(2).split(' ')[1][1:]
            simple_forms = stats_reg.group(3).split(' ')[0]
            unique_simple_forms = stats_reg.group(3).split(' ')[1][1:-1]
            digits = stats_reg.group(4).split(' ')[0]
            unique_digits = stats_reg.group(4).split(' ')[1][1:-1]
            word_count = int(simple_forms.split(' ')[0])
            if word_count != 0:
                unique_err_p = int(err_n) * 100 / int(unique_simple_forms)
                err_count = 0
                with open(snt_dir + '/err', 'r') as f:
                    errors = f.read().split('\n')
                with open(snt_dir + '/tok_by_freq.txt', 'r') as f:
                    lines = f.read().split('\n')
                    for line in lines:
                        lst = line.strip().split('\t')
                        try:
                            if lst[1] in errors:
                                err_count = err_count + int(lst[0])
                        except Exception as e:
                            continue
                err_p = err_count * 100 / int(simple_forms)

                # 'iz err fajla naci frekvenciju u fajlu tok_by_freq.txt i sabrati - to ej ukupan broj gresaka.' \
                # 'Taj broj * 100 / simple_forms'
            else:
                unique_err_p = 100
                err_p = 100

            stats = {'sent_del': sent_del, 'tokens': tokens, 'unique_tokens': unique_tokens,
                     'simple_forms': simple_forms, 'unique_simple_forms': unique_simple_forms, 'digits': digits,
                     'unique_digits': unique_digits, 'err_n': err_n, 'unique_err_p': str(round(unique_err_p, 2)),
                     'err_p': str(round(err_p, 2))}

            self.cleanup(snt_dir, snt_f)

            return stats

    def __get_stats_verbose(self, file=None, text=None):
        """
        Retrieves results of processing the text compiled to a dictionary.

        :param file: string (Path to file)
        :param text: string (Text to analyze)
        :return: dic
        """
        if text is not None:
            file = os.path.join(os.getcwd(), 'utx_tmp.txt')
            with open(file, 'w') as f:
                f.write(text)
        _filepath, file_extension = os.path.splitext(file)
        snt_dir = _filepath + '_snt'
        snt_f = _filepath + '.snt'

        os.system('mkdir "%s"' % snt_dir)
        os.system('%s/App/UnitexToolLogger Normalize "%s" -r"%s/%s/Norm.txt" --output_offsets="%s/normalize.out.'
                  'offsets" -qutf8-no-bom' % (self.UNITEX_DIR, file, self.UNITEX_DIR, self.lang, snt_dir))
        os.system('%s/App/UnitexToolLogger Grf2Fst2 "%s/%s/Graphs/Preprocessing/Sentence/Sentence.grf" -y '
                  '--alphabet="%s/%s/Alphabet.txt" -qutf8-no-bom' % (self.UNITEX_DIR, self.UNITEX_DIR, self.lang,
                                                                     self.UNITEX_DIR, self.lang))
        os.system('%s/App/UnitexToolLogger Flatten "%s/%s/Graphs/Preprocessing/Sentence/Sentence.fst2" --rtn -d5'
                  ' -qutf8-no-bom' % (self.UNITEX_DIR, self.UNITEX_DIR, self.lang))
        os.system('%s/App/UnitexToolLogger Fst2Txt -t"%s" "%s/%s/Graphs/Preprocessing/Sentence/Sentence.fst2" '
                  '-a"%s/%s/Alphabet.txt" -M --input_offsets="%s/normalize.out.offsets" --output_offsets="%s/normalize.'
                  'out.offsets" -qutf8-no-bom' % (self.UNITEX_DIR, snt_f, self.UNITEX_DIR, self.lang,
                                                  self.UNITEX_DIR, self.lang, snt_dir, snt_dir))
        os.system('%s/App/UnitexToolLogger Grf2Fst2 "%s/%s/Graphs/Preprocessing/Replace/Replace.grf" -y '
                  '--alphabet="%s/%s/Alphabet.txt" -qutf8-no-bom' % (self.UNITEX_DIR, self.UNITEX_DIR, self.lang,
                                                                     self.UNITEX_DIR, self.lang))
        os.system('%s/App/UnitexToolLogger Fst2Txt -t"%s" "%s/%s/Graphs/Preprocessing/Replace/Replace.fst2" '
                  '-a"%s/%s/Alphabet.txt" -R --input_offsets="%s/normalize.out.offsets" --output_offsets="%s/normalize.'
                  'out.offsets" -qutf8-no-bom' % (self.UNITEX_DIR, snt_f, self.UNITEX_DIR, self.lang,
                                                  self.UNITEX_DIR, self.lang, snt_dir, snt_dir))
        os.system('%s/App/UnitexToolLogger Tokenize "%s" -a"%s/%s/Alphabet.txt" --input_offsets="%s/normalize.'
                  'out.offsets" --output_offsets="%s/tokenize.out.offsets" -qutf8-no-bom' % (self.UNITEX_DIR, snt_f,
                                                                                             self.UNITEX_DIR, self.lang,
                                                                                             snt_dir, snt_dir))
        if self.lang == 'Serbian-Latin':
            os.system('%s/App/UnitexToolLogger Dico -t"%s" -a"%s/%s/Alphabet.txt" %s "%s/%s/Dela/NewBrojSlovima.'
                      'fst2" "%s/%s/Dela/NewBrojSlovima_norm-z.fst2" -qutf8-no-bom' % (self.UNITEX_DIR, snt_f,
                                                                                       self.UNITEX_DIR, self.lang,
                                                                                       self.dic_list_str,
                                                                                       self.UNITEX_DIR, self.lang,
                                                                                       self.UNITEX_DIR, self.lang))
        elif self.lang == 'Serbian-Cyrillic':
            os.system('%s/App/UnitexToolLogger Dico -t"%s" -a"%s/%s/Alphabet.txt" %s "%s/%s/Dela/NewBrojSlovima.'
                      'fst2" "%s/%s/Dela/NewBrojSlovima_norm-z.fst2" -qutf8-no-bom' % (self.UNITEX_DIR, snt_f,
                                                                                       self.UNITEX_DIR, self.lang,
                                                                                       self.dic_list_str,
                                                                                       self.UNITEX_DIR, self.lang,
                                                                                       self.UNITEX_DIR, self.lang))
        else:
            os.system('%s/App/UnitexToolLogger Dico -t"%s" -a"%s/%s/Alphabet.txt" "%s/%s/Dela/dela-en-public.bin" '
                      '"%s/%s/Dela/Dnum.fst2" -qutf8-no-bom' % (self.UNITEX_DIR, snt_f, self.UNITEX_DIR, self.lang,
                                                                self.UNITEX_DIR, self.lang, self.UNITEX_DIR, self.lang))
        os.system('%s/App/UnitexToolLogger SortTxt "%s/dlf" -l"%s/dlf.n" -o"%s/%s/Alphabet_sort.txt" -qutf8-no-bom' %
                  (self.UNITEX_DIR, snt_dir, snt_dir, self.UNITEX_DIR, self.lang))
        os.system('%s/App/UnitexToolLogger SortTxt "%s/dlc" -l"%s/dlc.n" -o"%s/%s/Alphabet_sort.txt" -qutf8-no-bom' %
                  (self.UNITEX_DIR, snt_dir, snt_dir, self.UNITEX_DIR, self.lang))
        os.system('%s/App/UnitexToolLogger SortTxt "%s/err" -l"%s/err.n" -o"%s/%s/Alphabet_sort.txt" -qutf8-no-bom' %
                  (self.UNITEX_DIR, snt_dir, snt_dir, self.UNITEX_DIR, self.lang))
        os.system('%s/App/UnitexToolLogger SortTxt "%s/tags_err" -l"%s/tags_err.n" -o"%s/%s/Alphabet_sort.txt" '
                  '-qutf8-no-bom' % (self.UNITEX_DIR, snt_dir, snt_dir, self.UNITEX_DIR, self.lang))
        with open(snt_dir + '/stats.n', 'r', encoding='utf-8') as f:
            stats_s = f.read()
        stats_reg = re.search(r'(.*) sentence delimiters?, (.*) tokens?, (.*) simple forms?, (.*) digits?', stats_s)
        with open(snt_dir + '/err.n', 'r', encoding='utf-8') as f:
            err_n = f.read().strip()
        if stats_reg and err_n:
            sent_del = stats_reg.group(1)
            tokens = stats_reg.group(2).split(' ')[0]
            unique_tokens = stats_reg.group(2).split(' ')[1][1:]
            simple_forms = stats_reg.group(3).split(' ')[0]
            unique_simple_forms = stats_reg.group(3).split(' ')[1][1:-1]
            digits = stats_reg.group(4).split(' ')[0]
            unique_digits = stats_reg.group(4).split(' ')[1][1:-1]
            word_count = int(simple_forms.split(' ')[0])
            if word_count != 0:
                unique_err_p = int(err_n) * 100 / int(unique_simple_forms)
                err_count = 0
                with open(snt_dir + '/err', 'r') as f:
                    errors = f.read().split('\n')
                with open(snt_dir + '/tok_by_freq.txt', 'r') as f:
                    lines = f.read().split('\n')
                    for line in lines:
                        lst = line.strip().split('\t')
                        try:
                            if lst[1] in errors:
                                err_count = err_count + int(lst[0])
                        except Exception as e:
                            continue
                err_p = err_count * 100 / int(simple_forms)

                # 'iz err fajla naci frekvenciju u fajlu tok_by_freq.txt i sabrati - to ej ukupan broj gresaka.' \
                # 'Taj broj * 100 / simple_forms'
            else:
                unique_err_p = 100
                err_p = 100

            stats = {'sent_del': sent_del, 'tokens': tokens, 'unique_tokens': unique_tokens,
                     'simple_forms': simple_forms, 'unique_simple_forms': unique_simple_forms, 'digits': digits,
                     'unique_digits': unique_digits, 'err_n': err_n, 'unique_err_p': str(round(unique_err_p, 2)),
                     'err_p': str(round(err_p, 2))}

            self.cleanup(snt_dir, snt_f)

            return stats

    def get_stats(self, file=None, text=None, verbose=False):
        if text is None and file is None:
            raise ValueError('Either file or text argument must be provided.')
        else:
            if verbose is True:
                stats = self.__get_stats_verbose(file=file, text=text)
            else:
                stats = self.__get_stats_silent(file=file, text=text)
            return stats

    def s_tag_text(self, file=None, text=None, is_xml=False):
        """
        Adds <s> and </s> xml tags at the beggining and the end of the sentence. Method returns modified text.

        :param file: string (Path to file)
        :param text: string (Text to modify)
        :param is_xml: Boolean (Is file or text xml or text)
        :return: string (Modified text)
        """

        if text is not None:
            file = os.path.join(os.getcwd(), 'utx_tmp.txt')
            with open(file, 'w') as f:
                f.write(text)
        _filepath, file_extension = os.path.splitext(file)
        snt_dir = _filepath + '_snt'
        snt_f = _filepath + '.snt'

        os.system('mkdir "%s"' % snt_dir)
        os.system('%s/App/UnitexToolLogger Normalize "%s" -r"%s/%s/Norm.txt" --output_offsets="%s/normalize.out.offsets'
                  '" -qutf-no-bom' % (self.UNITEX_DIR, file, self.UNITEX_DIR, self.lang, snt_dir))

        os.system('%s/App/UnitexToolLogger Fst2Txt -t"%s" "%s/%s/Graphs/Preprocessing/Sentence/Sentence-xml-ELTeC.fst2"'
                  ' -a"%s/%s/Alphabet.txt" -M --input_offsets="%s/normalize.out.offsets" --output_offsets="%s/normalize'
                  '.out.offsets" -qutf8-no-bom' % (self.UNITEX_DIR, snt_f, self.UNITEX_DIR, self.lang, self.UNITEX_DIR,
                                                   self.lang, snt_dir, snt_dir))

        os.system('%s/App/UnitexToolLogger Grf2Fst2 "%s/%s/Graphs/Preprocessing/Replace/Replace.grf" -y --alphabet="%s'
                  '/%s/Alphabet.txt" -qutf8-no-bom' % (self.UNITEX_DIR, self.UNITEX_DIR, self.lang, self.UNITEX_DIR,
                                                       self.lang))

        os.system('%s/App/UnitexToolLogger Fst2Grf2 -t"%s" "%s/%s/Graphs/Preprocessing/Replace/Replace.fst2" -a"%s/%s/'
                  'Aplhabet.txt" -R --input_offsets="%s/normalize.out.offsets" --output_offsets="%s/normalize.out.'
                  'offsets" -qutf8-no-bom' % (self.UNITEX_DIR, snt_f, self.UNITEX_DIR, self.lang, self.UNITEX_DIR,
                                              self.lang, snt_dir, snt_dir))

        os.system('%s/App/UnitexToolLogger Tokenize "%s" -a"%s/%s/Alphabet.txt" --input_offsets="%s/normalize.out.'
                  'offsets" --output_offsets="%s/tokenize.out.offsets" -qutf8-no-bom' % (self.UNITEX_DIR, snt_f,
                                                                                         self.UNITEX_DIR, self.lang,
                                                                                         snt_dir, snt_dir))
        text = read_text_file(snt_f)
        self.cleanup(snt_dir, snt_f)
        if is_xml:
            return '<data>' + text + '</data>'
        else:
            return '<data><s>' + text + '</s></data>'


if __name__ == '__main__':
    utx_dir = sys.argv[1]
    filepath = sys.argv[2]
    language = sys.argv[3]
    utx = Unitex(language)
    data = utx.get_stats(filepath)
    print(data)
