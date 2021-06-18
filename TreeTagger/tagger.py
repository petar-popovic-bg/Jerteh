# Functions to use TreeTagger
# Dont forget to edit treetaggerwrapper in venv so it uses correct .par files
import treetaggerwrapper
from config import treetagger_dir


class TreeTagger:
    def __init__(self):
        self.tagdir = treetagger_dir

    def tag_srlat(self, text):
        """
        Tag Serbian language - latin script.

        :param text: string
        :return: string
        """
        tagger = treetaggerwrapper.TreeTagger(TAGLANG='sr-lat', TAGDIR=self.tagdir)
        tagged_text = '\n'.join(tagger.tag_text(text))
        return tagged_text

    def tag_srcyr(self, text):
        """
        Tag Serbian language - cyrillic script.

        :param text: string
        :return: string
        """
        tagger = treetaggerwrapper.TreeTagger(TAGLANG='sr-cyr', TAGDIR=self.tagdir)
        tagged_text = '\n'.join(tagger.tag_text(text))
        return tagged_text
