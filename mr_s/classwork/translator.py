from translate import Translator

text = "do not get me angry"
translator = Translator(to_lang='yo')
translation = translator.translate(text)
print(translation)
