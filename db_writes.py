"""
Handles the database writes for app
"""
import os
import psycopg2


SQL_USER = os.environ["SQL_USER"]
SQL_PWD = os.environ["SQL_PASSWORD"]
SQL_DB = os.environ["SQL_DB"]
DB_USER = os.environ["USER"]
DB_HOST = os.environ["DB_HOST"]
DATABASE_URI = os.environ["DATABASE_URL"]

CON = psycopg2.connect(database=SQL_DB, user=SQL_USER, password=SQL_PWD, host=DB_HOST)

def price_write(price_data):
    """write data to the database"""
    with CON:
        cur = CON.cursor()
        price_list = price_data['priceHistory']
        price_list_str = ''
        for entry in price_list:
            price_list_str += entry['price_date'] + ' - ' + str(entry['price']) + ' '
        item = price_data['title']
        imageurl = price_data['imgurl']
        poster = price_data['user']
        pfp = price_data['profpic']
        time = price_data['time']
        likes = 99
<<<<<<< HEAD
        graphurl ='./graphs/graph_Test ID.png'
=======
        graphurl ='temp'
>>>>>>> master
        asin = price_data['ASIN']
        cur.execute("INSERT INTO posts (itemname, imageurl, pricehist, username, pfp, time, likes, graphurl, asin) " + \
            "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);", (item, imageurl, price_list_str, poster, pfp, time, likes, graphurl, asin))

def get_posts(username):
    """get posts from a specific user from the database"""
    with CON:
        cur = CON.cursor()
        cur.execute(f"SELECT * FROM posts WHERE username = '{username}'")
        rows = cur.fetchall()
        item_data = {
            'itemname': rows[0][1],
            'imgurl': rows[0][2],
            'pricehistory': rows[0][3],
            'user': rows[0][4],
            'pfp': rows[0][5],
            'time': rows[0][6],
            'likes': rows[0][7],
            'graphurl': rows[0][8],
            'asin': rows[0][9]
            }
        return item_data
        
def get_item_data(itemdata):
    """get data on an item from the database"""
    with CON:
        cur = CON.cursor()
        cur.execute(f"SELECT * FROM posts WHERE itemname = '{itemdata}'")
        rows = cur.fetchall()
        print(rows)
        item_data = {
            'itemname': rows[0][1],
            'imgurl': rows[0][2],
            'pricehistory': rows[0][3],
            'user': rows[0][4],
            'pfp': rows[0][5],
            'time': rows[0][6],
            'likes': rows[0][7],
            'graphurl': rows[0][8],
            'asin': rows[0][9]
            }
        return item_data

