# This is a sample Python script.
from TreeTagger.tagger import TreeTagger
from Unitex.wrapper import Unitex
from Text.text import cyr_to_lat

# ttager = TreeTagger()
# utx_lat = Unitex('Serbian-Latin')

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    text = 'Istagirati ovo. Nemam latinicu na ovoj tastaturi.'
    tagged_text = TreeTagger().tag_srlat(text)
    print(tagged_text)

    filepath = '/home/petar/PycharmProjects/Jerteh/temp.txt'
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(text)

    stats = Unitex('Serbian-Latin').get_stats(filepath)
    print(stats)

    text_cyr = 'Његошева улица је доста лепа.'
    print(cyr_to_lat(text_cyr))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
