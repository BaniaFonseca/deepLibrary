from minio import Minio

class Connection:

    @staticmethod
    def get_connection():
        client = Minio('localhost:9000',
            access_key='deep+2020',
            secret_key='deep+2020',
            secure=False)
        
        return client   