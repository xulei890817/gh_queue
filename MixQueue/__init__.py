from MixQueue.Queue.redis_queue import RedisQueue


def gen_queue(queue_type="redis", *args, **kwargs):
    if queue_type == "redis":
        return RedisQueue(*args, **kwargs)
