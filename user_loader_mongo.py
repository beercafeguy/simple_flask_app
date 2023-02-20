import mongo_utils

user1 = {
    "user_name":"vinay",
    "full_name": "Vinay Kothari",
    "id": 2,
    "occupation": "Thekedar"
}

user2 = {
    "user_name":"hem",
    "full_name": "Hem Chandra",
    "id": 1,
    "occupation": "Developer"
}

users = [user1,user2]
mongo_utils.insert_users(users, "dim_users")
