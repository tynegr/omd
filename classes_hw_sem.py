import re
from collections import defaultdict, OrderedDict
from typing import List
from math import log

# 1 задание


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
        self.result = None

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
        self.result = result
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

    # 2 задание

    def tf_transform(self, count_matrix: List[List[int]]) -> List[List[float]]:
        return [[round(num / sum(row), 3) for num in row] for row in
                count_matrix]
    # 3 задание

    def idf_transform(self, count_matrix: List[List[int]]) -> List[float]:
        length_of_row = len(count_matrix[0])
        lentgth_of_matrix = len(count_matrix)
        almost_idf = [sum([1 if row[i] else 0 for row in count_matrix]) for i
                      in range(length_of_row)]
        idf = [round(log((lentgth_of_matrix + 1) / (num + 1)) + 1, 3) for num
               in almost_idf]
        return idf

# 4 задание


class TfidfTransformer(CountVectorizer):
    def __init__(self):
        super().__init__()

    def fit_transform(self, matrix: List[List[int]]) -> List[List[float]]:
        tf_matrix = self.tf_transform(matrix)
        idf_values = self.idf_transform(matrix)
        tfidf_matrix = []
        for i in range(len(matrix)):
            tfidf_row = [round(tf_matrix[i][j] * idf_values[j], 3)
                         for j in range(len(matrix[i]))]
            tfidf_matrix.append(tfidf_row)

        return tfidf_matrix


# 5 задание

class TfidfVectorizer(CountVectorizer):
    def __init__(self, tfidf_trans=TfidfTransformer):
        super().__init__()
        self.transformer = tfidf_trans()

    def fit_transform(self, corpus: List[str]) -> List[List[float]]:
        count_matrix = super().fit_transform(corpus)
        return self.transformer.fit_transform(count_matrix)


if __name__ == '__main__':
    text = ['Crock,  Pot Pasta Never boil pasta again',
            'Pasta Pomodoro Fresh ingredients Parmesan to taste']
    count_vectorizer = CountVectorizer()
    tfidf_transformer = TfidfTransformer()
    tfidf_vectorizer = TfidfVectorizer()
    count_vectorized = count_vectorizer.fit_transform(text)
    tfidf_transformed = tfidf_transformer.fit_transform(count_vectorized)
    tfidf_vectorized = tfidf_vectorizer.fit_transform(text)
    print(count_vectorizer.get_feature_names())
    print(count_vectorized)
    print(count_vectorizer.tf_transform(count_vectorized))
    print(count_vectorizer.idf_transform(count_vectorized))
    print(tfidf_transformed)
    print(tfidf_vectorized)
