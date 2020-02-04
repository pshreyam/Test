import mysql.connector
class Database:
    def __init__(self,host,user,database,password=""):
        self.host=host
        self.user=user 
        self.database=database
        self.password=password
        try:
            self.mydb=mysql.connector.connect(
                host=self.host,
                user=self.user,
                database=self.database,
                password=self.password
            )
            print("Connected to database: "+self.database)
        except Exception:
            print("Not connected to database.")
    def insertToWadaTable(self,wada_name,wada_address,wada_info):
        self.mycursor=self.mydb.cursor()
        sql="INSERT INTO wada(wada_name,wada_address,wada_info) VALUES(%s,%s,%s)"
        val=(wada_name,wada_address,wada_info)
        self.mycursor.execute(sql,val)
        self.mydb.commit()
        self.mycursor.close()
        print("Record inserted.")
    def setWard(self,name):
        self.mycursor=self.mydb.cursor(buffered=True)
        sql="SELECT * FROM wada WHERE wada_name=%s"
        self.mycursor.execute(sql,(name,))
        records=self.mycursor.fetchall()
        #print(mycursor.rowcount)
        for row in records:
            sql="UPDATE wada SET current ='1' WHERE wada_name=%s"                        
            self.mycursor.execute(sql,(name,))            
        self.mydb.commit()
        print("Current ward :",row[1])
        sql="SELECT * FROM wada WHERE wada_name!=%s"
        self.mycursor.execute(sql,(name,))
        records=self.mycursor.fetchall()
        #print(mycursor.rowcount)
        for row in records:           
            sql="UPDATE wada SET current ='0' WHERE wada_name!=%s"            
            self.mycursor.execute(sql,(name,))
        self.mydb.commit()
        self.mycursor.close()