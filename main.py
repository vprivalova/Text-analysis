from textblob import TextBlob


text = input('Введите текст: ')
t0 = TextBlob(text)
t = t0
ton = t.polarity
if (ton >= -1.0) and (ton < 0):
    analysis_ton = 'Негативный'
elif (ton > 0) and (ton <= 1.0):
    analysis_ton = 'Положительный'
elif ton == 0:
    analysis_ton = 'Нейтральный'

asl = float(len(t.words) / len(t.sentences))
awl = 0
flash_index = 206.835 - (1.015 * asl) - (84.6 * awl)
print('Предложений:', len(t.sentences))
print('Слов:', len(t.words))
print('Слогов:', )
print('Средняя длина предложения в словах:', asl)
print('Средняя длина слова в слогах:', awl)
print('Индекс удобочитаемости Флеша:', flash_index)
print('Как читается текст')
print('Тональность текста:', analysis_ton)
print('Обьективность: ', round(1 - TextBlob(text).subjectivity, 2) * 100, '%', sep='')
