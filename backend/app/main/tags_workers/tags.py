import shlex
from collections import Counter
from main.tags_workers.tf_idf import compute_tfidf


def get_most_3(text):
    """Возвращает 3 самых длинных слова, длиной больше 3х символов"""
    words = shlex.split(text)
    words = [word for word in words if len(word) > 3]
    return Counter(words).most_common(3)[0][0]


def get_first_word(text):
    splited = text.split()
    for w in splited:
        if len(w) > 3:
            return w


def get_tfidf(texts):
    corpus = [text['description'].split() for text in texts]

    result = compute_tfidf(corpus)

    maxes_values = {}
    for i in range(len(result)):
        max_value = 0
        max_key = ''
        for key, value in result[i].items():
            if value > max_value:
                max_value = value
                max_key = key
        maxes_values[texts[i]['id']] = max_key
    return maxes_values
