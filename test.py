import os
from TreeTagger.tagger import TreeTagger
from Utils.utils import get_files_from_dir
from Text.text import cyr_to_lat
from Unitex.wrapper import Unitex
from Noske.noske import create_doc, compile_vertical

files = get_files_from_dir(os.getcwd(), filter_ext=['.txt'])
data = []
for idx, file in enumerate(files):
    with open(file, 'r', encoding='utf-8') as f:
        text = f.read()

    lat_text = cyr_to_lat(text)

    with open(file, 'w', encoding='utf-8') as f:
        f.write(lat_text)

    tagged_text = TreeTagger().tag_srlat(lat_text)
    meta = Unitex('Serbian-Latin').get_stats(file)
    meta['file'] = os.path.basename(file)
    doc = create_doc(tagged_text, idx, meta)
    data.append(doc)

vertical = compile_vertical(data)

with open('mock_corpus.tt', 'w', encoding='utf-8') as f:
    f.write(vertical)

print(files)
