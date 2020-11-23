#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 23:31:51 2020

@author: masayamatu
"""

from ipywidgets import Textarea

def get_input(change):
    global Input
    Input=change["new"]

textarea = Textarea()
textarea.observe(get_input, names='value')
display(textarea)