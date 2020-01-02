import threading
s=5.0

def session():
  threading.Timer(s, session).start()
  c=0
  print(++c)

session()

