#encoding=utf-8

import webapp2
from service import postindex
from tools.web_tools import *


class SearchPage(webapp2.RequestHandler):
    def get(self):
        show_html(self.response, 'search.html', {"query": self.request.get('query')})


class SearchAjax(webapp2.RequestHandler):
    def get(self):
        query = self.request.get('query')
        cursor = self.request.get('cursor')
        pagesize = 10
        result = postindex.query(query, cursor, pagesize)
        show_json(self.response, result)