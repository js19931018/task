import time
import uuid
def next_id(t=None):
    if t is None:
        t = time.time()
    return '%015d%s000' % (int(t * 1000), uuid.uuid4().hex)
if __name__ == '__main__':
    t1=next_id()
    t2=next_id()
    print t1,t2