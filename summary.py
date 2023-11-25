from sumy.parsers.html import HtmlParser
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer as Summarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words


def summary(links):
    LANGUAGE = "german"
    SENTENCES_COUNT = 20
    for url in links:
        parser = HtmlParser.from_url(url, Tokenizer(LANGUAGE))

        stemmer = Stemmer(LANGUAGE)

        summarizer = Summarizer(stemmer)
        summarizer.stop_words = get_stop_words(LANGUAGE)

        articles = []
        for sentence in summarizer(parser.document, SENTENCES_COUNT):
            articles.append(str(sentence))
            
        return articles

