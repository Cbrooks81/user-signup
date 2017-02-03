#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import webapp2
import cgi
import re


page_header = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Signup</title>
        <style type="text/css">
            .error {
                color: red;
            }
        </style>
    </head>"""


page_body = """

    <body>
        <h1>
            <a href = "/">Signup</a>
        </h1>
        <form method = "post">
            <table>
                <tr>
                    <td><label for = "username">Username</label></td>
                    <td>
                        <input name="username" type="text" value="" >
                        <span class="error"></span>
                    </td>
                </tr>
                <tr>
                    <td><label for="password">Password</label></td>
                    <td>
                        <input name="password" type="password" required>
                        <span class ="error"></span>
                    </td>
                </tr>
                <tr>
                    <td><label for="verify">Verify Password</label></td>
                    <td>
                        <input name="verify" type="password" required>
                        <span class ="error"></span>
                    </td>
                </tr>
                <tr>
                    <td><label for="email">Email (optional)</label></td>
                    <td>
                        <input name="email" type="email" value="">
                        <span class="error"></span>
                    </td>
                </tr>
            </table>
            <input type="submit">
        </form>"""


def page_body2(user_error1,user_error2,user_error3,user_error4):

    page_body2 = ("""

            <body>
                <h1>
                    <a href = "/">Signup</a>
                </h1>
                <form method = "post">
                    <table>
                        <tr>
                            <td><label for = "username">Username</label></td>
                            <td>
                                <input name="username" type="text" value="" >
                                <span class="error">%(user_error1)s</span>
                            </td>
                        </tr>
                        <tr>
                            <td><label for="password">Password</label></td>
                            <td>
                                <input name="password" type="password" required>
                                <span class ="error">%(user_error2)s</span>
                            </td>
                        </tr>
                        <tr>
                            <td><label for="verify">Verify Password</label></td>
                            <td>
                                <input name="verify" type="password" required>
                                <span class ="error">%(user_error3)s</span>
                            </td>
                        </tr>
                        <tr>
                            <td><label for="email">Email (optional)</label></td>
                            <td>
                                <input name="email" type="email" value="">
                                <span class="error">%(user_error4)s</span>
                            </td>
                        </tr>
                    </table>
                    <input type="submit">
                </form>"""%{"user_error1":user_error1,"user_error2":user_error2,
                            "user_error3":user_error3,"user_error4":user_error4})
    return page_body2


page_footer = """
    </body>
    </html>"""



User_Check = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
def valid_username(username):
    return username and User_Check.match(username)

Password_Check = re.compile(r"^.{3,20}$")
def valid_password(password):
    return password and Password_Check.match(password)

Email_Check = re.compile(r'^[\S]+@[\S]+\.[\S]+$')
def valid_email(email):
    return not email or Email_Check.match(email)


class MainHandler(webapp2.RequestHandler):


    def get(self):

        content = page_header + page_body + page_footer

        self.response.write(content)



    def post(self):

        have_error = False

        username = self.request.get("username")
        password = self.request.get("password")
        verify = self.request.get("verify")
        email = self.request.get("email")



        if not valid_username(username):
            user_error1 = "Not a valid username"
            have_error = True
        else:
            user_error1 = ""

        if not valid_password(password):
            user_error2 = "Not a valid password"
            have_error = True
        else:
            user_error2 = ""

        if password != verify:

            user_error3 = "passwords do not match"
            have_error = True

        else:
            user_error3 = ""

        if not valid_email(email):
            user_error4 = "not a valid email"
            have_error = True

        else:
            user_error4 = ""



        if not have_error:

            self.redirect('/welcome?username=' + username)
        else:

            content2 = page_header + page_body2(user_error1,user_error2,user_error3,user_error4) + page_footer

            self.response.write(content2)


class WelcomeHandler(webapp2.RequestHandler):

    def get(self):



        username = self.request.get("username")
        escaped_username = cgi.escape(username, quote = True)
        new_username = "<strong>" + escaped_username + "</strong>"
        welcome_sentence ="Welcome " + new_username + "!!!"
        content = page_header + welcome_sentence + page_footer

        self.response.write(content)







app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/welcome', WelcomeHandler)

], debug=True)
