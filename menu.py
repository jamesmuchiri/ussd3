import json

from flask import make_response

import datetime
#from ..database import redis

class Menu(object):
    def __init__(self,user_response, phone_number=None):
        self.user_response = user_response
        self.phone_number = phone_number
        

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

    def home(self):
        """serves the home menu"""

        kenya_time = datetime.datetime.utcnow() + datetime.timedelta(hours=3)
        if 5<= kenya_time <12 :
            Good_Morning="Good Morning"
            menu_text =("CON {}"
                        "\nHow may i help you"
                        "\n  -Limit "
                        "\n  -Balance"
                        "\n  -Loan"
                        "\n  -Amount"
            ).format(Good_Morning)
        elif  12 <= kenya_time < 17 :
            Good_Afternoon="Good Afternoon"
            menu_text =("CON {}"
                        "\nHow may i help you"
                        "\n  -Limit "
                        "\n  -Balance"
                        "\n  -Loan"
                         "\n  -Amount"
                    ).format(Good_Afternoon)
        else:
            Good_Evening="Good Evening"
            menu_text =("CON {}"
                        "\nHow may i help you"
                        "\n  -Limit "
                        "\n  -Balance"
                        "\n  -Loan"
                        "\n  -Amount"
                    ).format(Good_Evening)

        # print the response on to the page so that our gateway can read it
        return self.ussd_proceed(menu_text)
