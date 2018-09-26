import redis

from MixQueue.Queue import BaseQueue


class RedisQueue(BaseQueue):

    def __init__(self, host, port=6379, db=0):
        super(RedisQueue, self).__init__()
        self.r = redis.StrictRedis(host=host, port=port, db=db)

    def get_client(self):
        return self.r

    def push_left(self, key, value):
        return self.r.lpushx(key, *value)

    def push_array_left(self, key, *value):
        return self.r.lpush(key, *value)

    def push_right(self, key, value):
        return self.r.rpushx(key, value)

    def push_array_right(self, key, *value):
        return self.r.rpush(key, *value)

    def pop_left(self, key):
        return self.r.lpop(key)

    def pop_right(self, key):
        return self.r.rpop(key)

    @property
    def qsize(self, key):
        return self.r.llen(key)

    def get(self, key, timeout=2):
        self.r.blpop(key, timeout=timeout)

    def put(self, key, value):
        self.r.rpushx(key, value)

    def get_nowait(self, key):
        self.r.lpop(key)

    def put_nowait(self, key, value):
        self.r.rpushx(key, value)
