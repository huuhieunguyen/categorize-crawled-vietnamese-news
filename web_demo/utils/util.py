import re
import underthesea

def preprocess(txt, lower=True):
    txt = re.sub(r'[^\w\s]', '', txt)
    txt = re.sub(r'[\d]', '', txt)
    txt = re.sub('\s+', ' ', txt)
    txt = txt.strip()
    if lower:
        txt = txt.lower()
    txt = underthesea.word_tokenize(txt, format='text')
    return txt