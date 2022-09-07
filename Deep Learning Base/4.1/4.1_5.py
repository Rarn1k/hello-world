def process(sentences):
    """
    Дан список текстов, слова в которых разделены пробелами (можно считать, что знаков препинания нет). Часть слов
    является "мусорными": в них присутствуют цифры и спецсимволы. Отфильтруйте такие слова из каждого текста.
    :param sentences: ['1 thousand devils', 'My name is 9Pasha', 'Room #125 costs $100', '888']
    :return: ['thousand devils', 'My name is', 'Room costs', '']
    """
    result = [' '.join([word for word in phrase.split(' ') if word.isalpha()]) for phrase in sentences]
    return result


print(process(['1 thousand devils', 'My name is 9Pasha', 'Room #125 costs $100', '888']))
