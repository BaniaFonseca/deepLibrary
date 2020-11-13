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
    def __init__(self, data=None, id=None):
        self.data = data
        self.id = id

    def reset(self):
        """ Put resource back into default setting. """
        self.__data = None

    @property
    def data(self):
        return self.__data
    
    @data.setter
    def data(self, value):
        self.__data = value
    
    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self, id):
        self.__id = id
    
    def __eq__(self, other):
        if not isinstance(other, Resource):
            return NotImplemented
        return self.id == other.id

class ObjectPool(object):
    
    """ Resource manager.
    Handles checking out and returning resources from clients.
    It's a singleton class.
    """

    __instance = None
    __resources = {}

    def __init__(self):
        if ObjectPool.__instance != None:
            raise NotImplemented("This is a singleton class.")

    @staticmethod
    def getInstance():
        if ObjectPool.__instance == None:
            ObjectPool.__instance = ObjectPool()

        return ObjectPool.__instance

    def getResource(self, id):
        if self.__resources.__contains__(id):
            print ("Using existing resource.")
            return self.__resources.pop(id)
        else:
            print ("Creating new resource.")
            id = None
            # data = self.request
            return Resource(id)

    def returnResource(self, resource):
        resource.reset()
        self.__resources.append(resource)

def main():
    pool = ObjectPool.getInstance()

    # These will be created
    one = pool.getResource(1)
    two = pool.getResource(1)

if __name__ == "__main__":
    id1 = Id(bucketname='foo', objectname='bar')
    id2 = Id(bucketname='foo', objectname='bar')
    r1 = Resource(data=None, id=id1)
    r2 = Resource(data=None, id=id2)
    print(r1 == r2)