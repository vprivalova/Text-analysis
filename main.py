from textblob import TextBlob
from googletrans import Translator, constants

text = input("Введите текст:")

translator = Translator()
translation = translator.translate(text)


if translation.src == 'ru' or translation.src == 'uk':
    text = translation.text

out = TextBlob(text).correct()

text_blob_object = TextBlob(text)
text_sentence = text_blob_object.sentences
text_words = text_blob_object.words

ton = text_blob_object.sentiment.polarity
if (ton >= -1.0) and (ton < 0):
    analysis_ton = 'Негативный'
elif (ton > 0) and (ton <= 1.0):
    analysis_ton = 'Положительный'
elif ton == 0:
    analysis_ton = 'Нейтральный'

vowels = ['E', 'Y', 'U', 'I', 'O', 'A']
text_separ = text_blob_object.words.singularize()
v_count = 0
for i in range(len(text_separ)):
    for j in text_separ[i]:
        if j in vowels or j.upper() in vowels:
            v_count += 1

ASL = len(text_words) / len(text_sentence)
ASW = v_count / len(text_words)
K = 206.835 - 1.015 * ASL - 84.6 * ASW


print('Предложений:', len(text_sentence))
print('Слов:', len(text_words))
print('Слогов:', v_count)
print('Средняя длина предложений в слогах:', ASL)
print('Средняя длина слов в слогах:', ASW)
print('Индекс удобочитаемости Флеша:', K)

if K > 50:
    if K > 80:
        print('Текст очень легко читается (для младших классов)')
    else:
        print('Простой текст (для школьников)')
else:
    if K > 25:
        print('Текст немного трудно читать (для студентов)')
    else:
        print('Текст трудно читать (для выпускников ВУЗов)')

print('Тональность текста:', analysis_ton)
print('Объективность:', round(1 - TextBlob(text).subjectivity, 2) * 100, '%', sep='')
