from googletrans import Translator
translation=Translator()
translated=translation.translate("Naam",dest="ne")
print(translated.text)