import os
from pymongo import MongoClient

"I created my variable "
MONGODB_URL= os.environ.get("MONGODB_URL")
#MONGODB_URL= "mongodb+srv://academia:Alpe10017Dec@cluster0.mtpqpfb.mongodb.net/?retryWrites=true&w=majority"



def get_db():
    mongodb_client = MongoClient(MONGODB_URL)

    return mongodb_client['academia']

def insert(items: list):
    database = get_db()

    for item in items:
        database.inventory.insert_one(item)

def get():
    database = get_db()
      
    for item in database.inventory.find():
        print(item)

def delete():
    database = get_db()

    result = database.inventory.delete_one({"Brand": "DELL"})

    if result.deleted_count==1:
        print("Data deleted successfully")
    else:
        print("Bad Request")


filter={"Brand": "HP"}
new_valor={"$set": {"Model": "MX15"}}
def update():
    database = get_db()

    result = database.inventory.update_one(filter,new_valor)

    if result.modified_count==1:
        print("Success")
    else:
        print("Bad Request")



get()
""" 
delete()
update() 

"""
""" insert([
    {
        "Product": "CPU" ,
        "Brand": "DELL",
        "Model": "Optiplex",
        "SN": "3CQ9394NT4",
        "Memory RAM": "8gb",
        "HDD": "256GB",
    },
    {
        "Product": "CPU" ,
        "Brand": "HP",
        "Model": "ProDesk",
        "SN": "32121545",
        "Memory RAM": "8gb",
        "HDD": "256GB",
    },
    {
        "Product": "CPU" ,
        "Brand": "Apple",
        "Model": "MAC",
        "SN": "MAC123564",
        "Memory RAM": "30gb",
        "HDD": "1TB",
    }
]) """

"print(database)"