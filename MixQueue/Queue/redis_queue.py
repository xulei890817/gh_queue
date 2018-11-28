import redis

from MixQueue.Queue import BaseQueue
from MixQueue.Queue.d_error import GetValueTimeOutError, NoValueError


class RedisQueue(BaseQueue):

    def __init__(self, host, port=6379, db=0):
        super(RedisQueue, self).__init__()
        self.r = redis.StrictRedis(host=host, port=port, db=db)

    def get_client(self):
        return self.r

    def push_left(self, key, value):
        return self.r.lpush(key, value)

    def push_array_left(self, key, *value):
        for _value in value:
            return self.r.lpush(key, _value)

    def push_right(self, key, value):
        return self.r.rpush(key, value)

    def push_array_right(self, key, *value):
        for _value in value:
            return self.r.rpush(key, _value)

    def pop_left(self, key):
        return self.r.lpop(key)

    def pop_right(self, key):
        return self.r.rpop(key)

    @property
    def qsize(self, key):
        return self.r.llen(key)

    def get(self, key, timeout=2):
        try:
            result = self.r.blpop(key, timeout=timeout)
            return result
        except Exception as e:
            raise GetValueTimeOutError

    def put(self, key, value):
        self.r.rpush(key, value)

    def get_nowait(self, key):
        result = self.r.lpop(key)
        if result is None:
            raise NoValueError
        return result

    def get_batch_nowait(self, key, size):
        result = self.r.lrange(key, 0, size)
        if result is None:
            raise NoValueError
        return result

    def put_nowait(self, key, value):
        self.r.rpush(key, value)
