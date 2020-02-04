import json
word=input("Enter a word: ").strip().lower()
try:
    fileobj=open("text.json",'r')
    read=json.load(fileobj)
    words=read
except Exception:
    words=[]

similar=[]


for text in words:
    if text==word:
        print ("Text already inserted.")
    elif (word in text) or (text in word):
        words.append(word)
        similar.append(text)
    else:
        words.append(word)
        
print("Similar Words: {}".format(similar))

fileobj=open("text.json",'w')
json.dump(words,fileobj)



