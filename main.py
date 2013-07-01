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
from google.appengine.api import users

import os
import urllib

import jinja2
import webapp2


JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'])

class MainHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()

        if not user:
            self.redirect(users.create_login_url(self.request.uri))
        else:
            url = users.create_logout_url(self.request.uri)
            template = JINJA_ENVIRONMENT.get_template('index.html')
            template_values = {
            'user': user,
            'url_logout': url};
            self.response.write(template.render(template_values))

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
