import dl.settings.development as st
from pymongo import MongoClient

class Connection:

    @staticmethod
    def get_connection():
        url = "mongodb://{}:{}@{}:{}/{}".format(st.DATABASE_NAME, st.DATABASE_PASSWORD, st.DATABASE_HOST, st.DATABASE_PORT, st.DATABASE_USER)
        connection = MongoClient(url) 
        return connection[st.DATABASE_NAME]         
