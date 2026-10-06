sentence = "Кот сидит на крыше"
sentenceNew = sentence.replace("Кот", 'Пес')
print(sentenceNew)

phrase = "Я люблю яблоки и яблоки - самые вкусные фрукты."
new = phrase.replace("яблоки", "бананы", 1)
print(new)

text = "Привет, мир! Привет, люди! Привет, солнце!"
textNew = text.replace("Привет", "Здравствуй") and text.replace('люди','друзья')
#greeting = text.replace('люди','друзья')
print(textNew)
