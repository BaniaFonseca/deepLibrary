from minio import Minio

class Connection:

    @staticmethod
    def get_connection():
        client = Minio('192.168.43.109:9000',
            access_key='deep+2020',
            secret_key='deep+2020',
            secure=False)
        
        return client   