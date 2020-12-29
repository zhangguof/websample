#-*- coding:utf-8 -*-
import os
cur_path = os.path.dirname(os.path.abspath(__file__))
template_path = os.path.join(cur_path,"templates")
static_path = os.path.join(cur_path,"static")


auth_user = False

db_path = os.path.join(cur_path,"db")


session_path = os.path.join(cur_path,"db","sessions")

def make_paths(paths):
	for path in paths:
		if not os.path.exists(path):
			os.makedirs(path)
			print "make dir:%s"%path

make_paths((static_path,session_path))

session_timeout = 30*24*60*60