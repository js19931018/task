import threading
import json
import functools

ctx=threading.local()
class APIError(Exception):
    def __init__(self):
        Exception.__init__(self)
        self.message='API error'
def api(func):

    def _wrapper(*args, **kw):
        try:
            r = json.dumps(func(*args, **kw))
        except APIError, e:

            r = json.dumps(dict( message=e.message))
        except Exception, e:
            r = json.dumps(dict(error='internalerror', data=e.__class__.__name__, message=e.message))
        ctx.response.content_type = 'application/json'
        return r
    return _wrapper
