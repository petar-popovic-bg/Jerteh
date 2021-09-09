# Jerteh
This package provides utility classes and static methods for Python that make use of different third party software commonly used in text processing such as: [Unitex-GramLab](https://unitexgramlab.org/), [TreeTagger](https://www.cis.uni-muenchen.de/~schmid/tools/TreeTagger/), [Apache-Tika](https://tika.apache.org/) and [Google-Tesseract](https://opensource.google/projects/tesseract). 

## Installation
###### Linux
1. pip: `pip install -e git+https://github.com/petar-popovic-bg/Jerteh.git#egg=Jerteh`

   *update*: `pip install -e git+https://github.com/petar-popovic-bg/Jerteh.git#egg=Jerteh --upgrade`

2. Edit your *treetaggerwrapper.py* file inside your virtual environment, so the wrapper supports Serbian-latin and Serbian-cyrillic script.
    ```python
   """
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
   """
    ```

3. Edit *configure.py*, so it points to your local installations of TreeTagger and Unitex.
## Instructions
Using **TreeTagger** and **Unitex** classes requires [TreeTagger](https://www.cis.uni-muenchen.de/~schmid/tools/TreeTagger/) and [Unitex](https://unitexgramlab.org/) to be installed on your machine.
