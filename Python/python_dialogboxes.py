from googletrans import Translator
text=["Namaskar","aaha","ke xa?"]
translator=Translator()
dect=translator.translate(text,'en')
for tex in dect:
    print(tex.text)