#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-06-07 23:09:50
# @Author  : 曹伟 (caocaosze@qq.com)
# @Link    : #
# @Version : $Id$

import json

class Student(object):
	def __init__(self,name,age,score):
		self.name=name
		self.age=age
		self.score=score
s=Student('caowei',22,88)
print(s)
# def student2dict(std):
# 	return {
# 		"name":std.name,
# 		"age":std.age,
# 		"score":std.score
# 	}

print(json.dumps(s,default=lambda obj:obj.__dict__))	