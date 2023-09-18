from textblob import TextBlob
from googletrans import Translator
import ru_local as ru

RU_VOWELS = 'ЕЁУЫАОЭЯИЮёуеоаыяию'
ENG_VOWELS = 'EYUIOAeyuioa'
v_count = 0

text = input(ru.TEXT_INPUT)
text_blob_object = TextBlob(text)
text_sentence = text_blob_object.sentences
text_words = text_blob_object.words

for i in range(len(text)):
    if text[i] in RU_VOWELS or text[i] in ENG_VOWELS:
        v_count = v_count + 1

asl = len(text_words) / len(text_sentence)
aws = v_count / len(text_words)

print(ru.SENTENCES, len(text_sentence))
print(ru.WORDS, len(text_words))
print(ru.SYLLABLES, v_count)
print(ru.ASL, asl)
print(ru.AWS, aws)


translator = Translator()
detection = translator.detect(text)

if detection.lang == 'ru' or detection.lang == 'uk':
    f_index = 206.835 - 1.3*asl - 60.1*aws
else:
    f_index = 206.835 - 1.015*asl - 84.6*aws

print(ru.FLASH_INDEX, f_index)


if f_index > 50:
    if f_index > 80:
        print(ru.VERY_EASY_TEXT)
    else:
        print(ru.EASY_TEXT)
else:
    if f_index > 25:
        print(ru.HARD_TEXT)
    else:
        print(ru.VERY_HARD_TEXT)


if detection.lang == 'ru' or detection.lang == 'uk':
    translation = translator.translate(text)
    text_blob_object = TextBlob(translation.text)

ton = text_blob_object.sentiment.polarity
if (ton >= -1.0) and (ton < 0):
    analysis_ton = ru.NEGATIVE
elif (ton > 0) and (ton <= 1.0):
    analysis_ton = ru.POSITIVE
elif ton == 0:
    analysis_ton = ru.NEUTRAL

print(ru.TONALITY, analysis_ton)
print(ru.OBJECTIVITY, round(1 - text_blob_object.subjectivity, 2) * 100, '%', sep='')
