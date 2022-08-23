import sys
import os
sys.path.append(os.path.abspath("."))

import redis

class RedisCache:

    def __init__(self, name: str, expires=None, **kwargs):
        self.name = name
        self.expires = expires
        self.r = redis.Redis(**kwargs)
        if expires is not None:
            self.r.expire(name, expires)
            

    def add(self, key, value):
        return self.r.hset(self.name, key, value)

    def addIfNotExist(self, key, value):
        return self.r.hsetnx(self.name, key, value)

    def addAll(self, dictionary):
        return self.r.hmset(name=self.name, mapping=dictionary)

    def remove(self, key):
        return self.r.hdel(self.name, key)

    def get(self, key) -> str:
        out = self.r.hget(name=self.name, key=key)
        return out.decode() if out is not None else None

    def getAll(self) -> dict:
        return self.r.hgetall(name=self.name)

    def getAllKeys(self) -> list:
        return self.r.hkeys(self.name)

    def getAllValues(self) -> list:
        return self.r.hvals(self.name)

    def keyExist(self, key) -> bool:
        return self.r.hexists(self.name, key)

    def size(self):
        return self.r.hlen(self.name)

    def clear(self):
        return self.r.delete(self.name)
    
    def close(self) -> None:
        self.r.close()



if __name__ == "__main__":
    # mycache = RedisCache("mycache", host="localhost", port=7002)
    # # mycache.clear()
    # mycache.add("surname", "kullolli")
    # mycache.add("name", "klaus")
    # mycache.addIfNotExist("surname", "shima")
    # print(mycache.get("surname"))
    # print(mycache.get("name"))
    # print(mycache.keyExist("name"))
    # print(mycache.getAll())
    
    visitedCache = RedisCache("visited", host="localhost", port=7002)
    print(visitedCache.getAll())
    print(visitedCache.getAllKeys())
    # statisticsCache  = RedisCache("statistics", host="localhost", port=7002)
 
