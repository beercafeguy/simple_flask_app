import pymongo
client = pymongo.MongoClient(url)
db = client['crm']


def insert_user(user,collection_name):
    coll= db[collection_name]
    coll.insert_one(user)

def insert_users(users,collection_name):
    for user in users:
        insert_user(user,collection_name)
     
def find_user(user_name,collection_name):
    coll= db[collection_name]
    cur = coll.find({'user_name':user_name})
    user = None
    user_list = list(cur)
    if len(user_list) >0:
        user = user_list[0]
        del user['_id']
    return user

def find_users(collection_name):
    coll= db[collection_name]
    users = []
    for user in coll.find():
        del user['_id']
        users.append(user)
    return users

def delete_user(user_name,collection_name):
    coll= db[collection_name]
    coll.delete_many({'user_name':user_name})