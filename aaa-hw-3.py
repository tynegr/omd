import re
from collections import defaultdict, OrderedDict
from typing import List


class NotFittedError(Exception):
    pass


class CountVectorizer:
    """
    CountVectorizer - это класс, предназначенный
    для преобразования текстовых данных
    в матрицу счетчиков, представляющую частоту
    встречаемости слов в корпусе текстов.

    Attributes:
        words_set (OrderedDict): Словарь, хранящий уникальные слова из корпуса.
        fitted (bool): Флаг, указывающий,
        был ли выполнен процесс подгонки (fit) CountVectorizer.

    Methods:
        fit_transform(corpus: List[str]) -> List[List[int]]:
            Метод выполняет подгонку CountVectorizer
            к заданному корпусу текстов и возвращает
            матрицу счетчиков.
            Этот метод анализирует тексты, извлекает уникальные слова
            и подсчитывает их частоту в каждом тексте.

        get_feature_names() -> List[str]:
            Метод возвращает список уникальных слов (признаков),
             которые были обнаружены
            после подгонки CountVectorizer к корпусу текстов.

    """

    def __init__(self):
        self.words_set = OrderedDict()
        self.fitted = False

    def fit_transform(self, corpus: List[str]) -> List[List[int]]:
        """
        Метод выполняет подгонку CountVectorizer
        к заданному корпусу текстов и возвращает
        матрицу счетчиков.

        Args:
            corpus (List[str]): Список текстов для анализа и преобразования.

        Returns:
            List[List[int]]: Матрица счетчиков,
            где каждая строка представляет один текст,
            а каждый столбец - частоту
            встречаемости соответствующего слова из словаря.

        Raises:
            ValueError: Вызывается, если переданный корпус текстов пуст.

        """
        self.words_set = OrderedDict()
        self.fitted = True

        if not corpus:
            raise ValueError(
                'Корпус текстов пуст. '
                'Пожалуйста, предоставьте непустой список документов.')

        pattern = re.compile(r'[!"#$%&\'()*+,\-./:;<=>?@\[\]^_`{|}~ ]')

        words_dict = defaultdict(lambda: defaultdict(int))

        for doc_index, doc in enumerate(corpus):
            words = re.split(pattern, doc)
            for word in words:
                word = word.lower()
                if word:
                    self.words_set[word] = None
                    words_dict[doc_index][word] += 1

        feature_names = list(self.words_set.keys())

        result = [[words_dict[doc_index][word] for word in feature_names] for
                  doc_index in range(len(corpus))]
        return result

    def get_feature_names(self) -> List[str]:
        """
        Метод возвращает список уникальных слов (признаков),
        которые были обнаружены
        после подгонки CountVectorizer к корпусу текстов.

        Returns:
            List[str]: Список уникальных слов, выявленных в корпусе текстов.

        Raises:
            NotFittedError: Вызывается, если CountVectorizer
            не был подогнан к корпусу текстов.

        """
        if not self.fitted:
            raise NotFittedError(
                'Словарь не был подогнан или предоставлен. '
                'Сначала выполните подгонку CountVectorizer.')
        return list(self.words_set.keys())


if __name__ == '__main__':
    text = ['Crock,  Pot Pasta Never boil pasta again',
            'Pasta Pomodoro Fresh ingredients Parmesan to taste']
    vectorizer = CountVectorizer()
    transformed = vectorizer.fit_transform(text)
    print(vectorizer.get_feature_names())
    print(transformed)
