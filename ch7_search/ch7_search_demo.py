# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 18:59:43 2016

@author: user
"""
from numpy import *
import cherrypy, os, urllib, pickle
import imagesearch
class SearchDemo(object):
   def __init__(self):
# load list of images
      with open('webimlist.txt') as f:
            self.imlist = f.readlines()
      self.nbr_images = len(self.imlist)
      self.ndx = range(self.nbr_images)
# load vocabulary
      with open('vocabulary.pkl', 'rb') as f:
          self.voc = pickle.load(f)
# set max number of results to show
      self.maxres = 15
# header and footer html
      self.header = """
         <!doctype html>
         <head>
         <title>Image search example</title>
         </head>
         <body>
         """
      self.footer = """
         </body>
         </html>
         """
   def index(self,query=None):
     self.src = imagesearch.Searcher('web.db',self.voc)
   
     html = self.header
     html += """
       <br />
       Click an image to search. <a href='?query='>Random selection</a> of images.
       <br /><br />
        """
     if query:
# query the database and get top images
      res = self.src.query(query)[:self.maxres]
      for dist,ndx in res:
       imname = self.src.get_filename(ndx)
       html += "<a href='?query="+imname+"'>"
       html += "<img src='"+imname+"' width='100' />"
       html += "</a>"
     else:
# show random selection if no query
       random.shuffle(self.ndx)
       for i in self.ndx[:self.maxres]:
         imname = self.imlist[i]
         html += "<a href='?query="+imname+"'>"
         html += "<img src='"+imname+"' width='100' />"
         html += "</a>"

     html += self.footer
     return html
     
   index.exposed = True
cherrypy.quickstart(SearchDemo(), '/',
             config=os.path.join(os.path.dirname(__file__), 'service.conf'))