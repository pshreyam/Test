try:
    filename="Hello.txt"
    with open(filename) as file:
        contents=file.read()
        print(contents)
        #file.write("Hello")
except FileNotFoundError as fnf:
    print("Sorry,the file'",filename,"' was not found.")
print("")
line="row Row ROW roW your boat."
count_of_word_row=line.lower().count("row")
print (count_of_word_row)
