import psycopg2
from psycopg2 import connect
import sys
import base64
class imageDAO:
    def __init__(self, dbname, user, password, host, port):
        self.dbname = dbname
        self.user = user
        self.password = password
        self.host = host
        self.port = port

    def connect(self):
        return connect(
            dbname=self.dbname,
            user=self.user,
            password=self.password,
            host=self.host,
            port=self.port,
        )
        

    def insertImage(self, image):
        try:
            with self.connect() as conn:
                with conn.cursor() as cur:
                    binary = psycopg2.Binary(image)
                    cur.execute("INSERT INTO images(imgdata) VALUES (%s) RETURNING imgid", (binary,) )
                    id = str(cur.fetchone()[0])
        except Exception as e:
            raise e
        return 

    def getImage(self):
        try:
            with self.connect() as conn:
                with conn.cursor() as cur:
                    cur.execute("select * from images")
                    image = cur.fetchone()[1]

        except Exception as e:
            raise e
        return image