#!/usr/bin/env python
#-*- coding:utf-8 -*-
import requests
from selenium import webdriver
def wangzhi():
    dr=webdriver.Chrome()
    wz=dr.get('http://www.moore.ren')
    return wz
