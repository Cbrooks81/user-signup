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
        <form action = "/welcome" method = "post">
            <table>
                <tr>
                    <td><label for = "username">Username</label></td>
                    <td>
                        <input name="username" type="text" value="" required>
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



page_footer = """
    </body>
    </html>"""

class MainHandler(webapp2.RequestHandler):



    def get(self):

        content = page_header + page_body + page_footer

        self.response.write(content)

class userNameError(webapp2.RequestHandler):

    def post(self):


        username = self.request.get("username")

        


class WelcomeHandler(webapp2.RequestHandler):

    def post(self):

        username = self.request.get("username")
        escaped_username = cgi.escape(username, quote = True )
        new_username = "<strong>" + escaped_username + "</strong>"
        welcome_sentence = "Welcome " + new_username + "!!"
        content = page_header + welcome_sentence + page_footer

        self.response.write(content)





app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/welcome', WelcomeHandler)

], debug=True)
