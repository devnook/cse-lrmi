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
import jinja2
import os

import json

#import xmltodict

import webapp2
from webapp2_extras import routes

import logging

import urllib2

jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'])



class MainHandler(webapp2.RequestHandler):
  def get(self):

    template = jinja_environment.get_template('engine.html')
    lrmi_properties = [
      'Typical age range',
      'Learning resource type',
      'Educational use',
      'Use rights url',
      'About',
      'Grade'
    ]



    self.response.out.write(template.render(lrmi_properties=lrmi_properties))


class AboutHandler(webapp2.RequestHandler):
  def get(self):

    template = jinja_environment.get_template('about.html')
    self.response.out.write(template.render())


class HowtoHandler(webapp2.RequestHandler):
  def get(self):

    template = jinja_environment.get_template('howto.html')
    self.response.out.write(template.render())


class SubdomainHomeHandler(webapp2.RequestHandler):
  def get(self):

    template = jinja_environment.get_template('howto.html')
    self.response.out.write(template.render())


class DatasetsMainHandler(webapp2.RequestHandler):
  def get(self):

    template = jinja_environment.get_template('datasets-engine.html')
    self.response.out.write(template.render())


app = webapp2.WSGIApplication([
    routes.DomainRoute('edu.schema-labs.appspot.com', [
        webapp2.Route('/', handler=MainHandler, name='lrmi-cse-home'),
        webapp2.Route('/about', handler=AboutHandler, name='lrmi-cse-about'),
        webapp2.Route('/howto', handler=HowtoHandler, name='lrmi-cse-howto'),
    ]),
    routes.DomainRoute('datasets.schema-labs.appspot.com', [
        webapp2.Route('/', handler=DatasetsMainHandler, name='datasets-cse-home'),
    ]),
    routes.DomainRoute('localhost', [
        webapp2.Route('/', handler=DatasetsMainHandler, name='datasets-cse-home'),
        webapp2.Route('/about', handler=AboutHandler, name='lrmi-cse-about'),
        webapp2.Route('/howto', handler=HowtoHandler, name='lrmi-cse-howto'),
    ])
], debug=True)
