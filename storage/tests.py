from unittest import TestCase
from bson.objectid import ObjectId

from storage.resource_pool import * 

class TestId(TestCase):

    def setUp(self):
        self.id = Id(bucketname="foo", objectname="bar")
        self.id1 = Id(bucketname="foo1", objectname="bar1")

    def test__eq__a(self):
        self.assertEquals(self.id, self.id)
    
    def test__eq__b(self):
        self.assertNotEqual(self.id, self.id1)
    
    def test__str__(self):
        self.assertEquals(str(self.id), "foobar")

class TestResourcePool(TestCase):

    def setUp(self):
        self.id1 = Id(bucketname="foo1", objectname="bar1")
        self.id2 = Id(bucketname="foo2", objectname="bar2")
        self.id3 = Id(bucketname="foo3", objectname="bar3")
        
        self.pool1 = ObjectPool(id = self.id1)
        self.pool2 = ObjectPool(id = self.id2)
        r1 = self.pool1.get_resource()
        r2 = self.pool1.get_resource()
        r1.data = "R1"
        r2.data = "R2"
        
        self.pool1.return_resource(r1)
        self.pool1.return_resource(r2)
        r3 = self.pool2.get_resource()
        r4 = self.pool2.get_resource()
        r3.data = "R3"
        r4.data = "R4"
        self.pool2.return_resource(r3)
        self.pool2.return_resource(r4)

        self.pools_manager = ObjectPoolManager.get_instance()
        self.pools_manager.pools[self.id1] = self.pool1
        self.pools_manager.pools[self.id2] = self.pool2 
        
    def test_get_instance(self):
        self.assertIsNotNone(self.pools_manager)
    
    def test_pools_a(self):
        self.assertEquals(len(self.pools_manager.pools), 2)
    
    def test_pools_b(self):
        r = self.pools_manager.get_resource(self.id1)
        self.assertEquals(len(self.pools_manager.pools), 2)
    
    def test_pools_c(self):
        r = self.pools_manager.get_resource(self.id3)
        self.assertEquals(len(self.pools_manager.pools), 3)
    
    def test_get_resource_a(self):
        r = self.pools_manager.get_resource(self.id1)
        self.assertEquals(r.data, "R1")

    def test_resources_a(self):
        r = self.pools_manager.get_resource(self.id1)
        pool1 = self.pools_manager.pools[self.id1]
        self.assertEquals(len(pool1.resources), 1)

    def test_get_resource_b(self):
        r = self.pools_manager.get_resource(self.id2)
        self.assertEquals(r.data, "R3")

    def test_resources_b(self):
        r = self.pools_manager.get_resource(self.id2)
        pool1 = self.pools_manager.pools[self.id2]
        self.assertEquals(len(pool1.resources), 1)