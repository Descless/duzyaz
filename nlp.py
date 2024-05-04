import turkishnlp

from turkishnlp import detector
obj = detector.TurkishNLP()

obj.download()

obj.create_word_set()
def correct(cumle):
    lwords = obj.list_words(cumle)
    corrected_words = obj.auto_correct(lwords)
    corrected_string = " ".join(corrected_words)
    return corrected_string

