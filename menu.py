import json

from flask import make_response

import datetime
#from ..database import redis

class Menu(object):
    def execute(self):
        raise NotImplementedError

    def ussd_proceed(self, menu_text):
        #redis.set(self.session_id, json.dumps(self.session))
        menu_text = "CON {}".format(menu_text)
        response = make_response(menu_text, 200)
        response.headers['Content-Type'] = "text/plain"
        return response

    def ussd_end(self, menu_text):
        #redis.delete(self.session_id)
        menu_text = "END {}".format(menu_text)
        response = make_response(menu_text, 200)
        response.headers['Content-Type'] = "text/plain"
        return response

    
   
