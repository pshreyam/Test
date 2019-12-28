from datetime import datetime
print("Logged in.")
old=datetime.now()
diff=0
while(diff<=5):    
    new=datetime.now()
    diff=(new-old).total_seconds()
print("Difference=",diff)
print("Logged Out.")
    
