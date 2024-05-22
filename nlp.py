import time
import logging
from zemberek import TurkishMorphology, TurkishSentenceNormalizer, TurkishSpellChecker

logger = logging.getLogger(__name__)

def correct(example):
    morphology = TurkishMorphology.create_with_defaults()
    start = time.time()
    normalizer = TurkishSentenceNormalizer(morphology)
    logger.info(f"Normalization instance created in: {time.time() - start} s")

    start = time.time()
    print(example)
    print(normalizer.normalize(example), "\n")
    logger.info(f"Sentences normalized in: {time.time() - start} s")

    start = time.time()
    sc = TurkishSpellChecker(morphology)
    logger.info(f"Spell checker instance created in: {time.time() - start} s")