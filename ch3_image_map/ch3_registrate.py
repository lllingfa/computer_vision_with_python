# -*- coding: utf-8 -*-
"""
Created on Sat Aug 20 18:53:20 2016

@author: user
"""

import imregistration
# load the location of control points
xmlFileName = '../pcv_data/data/jkfaces.xml'
points = imregistration.read_points_from_xml(xmlFileName)
# register
imregistration.rigid_alignment(points,'../pcv_data/data/jkfaces/')
#immatrix = array([mask*array(Image.open(imlist[i]).convert('L')).flatten()
#for i in range(150)],'f')