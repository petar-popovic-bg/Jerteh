# Jerteh
This is a python package of tools used for Jerteh text processing and compiling vertical files for NoSketch Engine

## Installation
###### Linux
1. pip: <code>pip install -e git+https://github.com/petar-popovic-bg/Jerteh.git#egg=Jerteh</code>
2. Edit your *treetaggerwrapper.py* file inside your virtual environment so the wrapper supports Serbian-latin and Serbian-cyrillic
  ```python
    ...
    ('slovak', 'sk'),
    ('swahili', 'sw'),
    ('serbian-lat', 'sr-lat'),
    ('serbian-cyr', 'sr-cyr')]:
    ls = g_langsupport[lang] = copy.deepcopy(g_langsupport['__base__'])
    ...
    g_langsupport['sk']['dummysentence'] = 'To je koniec . .'
    g_langsupport['sw']['dummysentence'] = 'Hii ni mwisho . .'
    g_langsupport['sr-lat']['dummysentence'] = 'Ovo je kraj . .'
    g_langsupport['sr-cyr']['dummysentence'] = 'Ово је крај . .'
    ...
  ```
3. Edit *configure.py* so it points to your local installations of TreeTagger and Unitex

  
## Instructions
Using **TreeTagger** and **Unitex** classes requires [TreeTagger](https://www.cis.uni-muenchen.de/~schmid/tools/TreeTagger/) and [Unitex](https://unitexgramlab.org/) to be installed on your machine.
