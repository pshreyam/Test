from python_connecttodatabase import Database
db=Database('localhost','root','smartward')
name=input("Enter the wada name:")
address=input("Enter the address:")
info=input("Enter the info:")
db.insertToWadaTable(name,address,info)
db.setWard(name)