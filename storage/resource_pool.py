class Id(object):

    def __init__(self, bucketname=None, objectname=None):
        self.bucketname = bucketname
        self.objectname = objectname
    
    @property
    def bucketname(self):
        return self.__bucketname
    
    @bucketname.setter
    def bucketname(self, value):
        self.__bucketname = value

    @property
    def objectname(self):
        return self.__objectname
    
    @objectname.setter
    def objectname(self, value):
        self.__objectname = value
    
    def __str__(self):
        return self.bucketname+self.objectname

    def __hash__(self):
        return hash(str(self))

    def __eq__(self, other):
        if not isinstance(other, Id):
            return NotImplemented
        return self.bucketname == other.bucketname \
            and self.objectname == other.objectname

class Resource(object):

    """ Some resource, that clients need to use.
    
    The resources usualy have a very complex and expensive
    construction process, which is definitely not a case
    of this Resource class in my example.
    """
    def __init__(self, data=None, is_new=True):
        self.data = data
        self.is_new = is_new
    
    @property
    def data(self):
        return self.__data
    
    @data.setter
    def data(self, value):
        self.__data = value

    @property
    def is_new(self):
        return self.__is_new

    @is_new.setter
    def is_new(self, value):
        self.__is_new = value

class ObjectPool(object):
    """ 
        Pool of objects of the same type ...
    """
    def __init__(self, id=None):
        self.id = id
        self.resources = []

    @property
    def resources(self):
        return self.__resources
    
    @resources.setter
    def resources(self, value):
        self.__resources = value

    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self, value):
        self.__id = value

    def get_resource(self):
        if len(self.resources) > 0:
            return self.resources.pop(0)
        else:
            data = self.request(id)
            return Resource(data=data)

    def return_resource(self, resource):
        resource.is_new = False
        self.resources.append(resource)

    def __eq__(self, other):
        if not isinstance(other, ObjectPool):
            return NotImplemented
        return self.id == other.id

    def request(self, id):
        return str(id)

class ObjectPoolManager(object):
    
    """ Object Pools manager.
        It's a singleton class.
    """

    __instance = None
    __pools = {}

    def __init__(self):
        if ObjectPoolManager.__instance != None:
            raise NotImplemented("This is a singleton class.")

    @staticmethod
    def get_instance():
        if ObjectPoolManager.__instance == None:
            ObjectPoolManager.__instance = ObjectPoolManager()
        return ObjectPoolManager.__instance

    @property
    def pools(self):
        return self.__pools
    
    @pools.setter
    def pools(self, value):
        self.__pools = value

    def get_resource(self, id):
        if self.__pools.__contains__(id):
            pool = self.__pools[id]
            return pool.get_resource()
        else:
            self.__pools[id] = ObjectPool(id=id)
            pool = self.__pools[id]
            return pool.get_resource()
            
    def return_resource(self, id, resource):
        pool = self.__pools[id]
        pool.return_resource(resource)