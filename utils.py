# -*- coding:utf-8 -*-
import conf
import web
import os
import time

from web.contrib.template import render_jinja

def html(f):
    def warp_func(*args, **kwargs):
        web.header('Content-Type', 'text/html')
        return f(*args, **kwargs)
    return warp_func

def json(f):
    def warp_func(*args, **kwargs):
        web.header('Content-Type', 'application/json')
        return f(*args, **kwargs)
    return warp_func


def text(f):
    def warp_func(*args, **kwargs):
        web.header('Content-Type', 'text/plain')
        return f(*args, **kwargs)
    return warp_func

render = render_jinja(conf.template_path,encoding = "utf-8")

def reload_conf():
    conf_file = os.path.join(conf.cur_path,"conf.json")
    if os.path.exists(conf_file):
        with open(conf_file,"rb") as f:
            import json
            conf_data = json.load(f)
            conf.__dict__.update(conf_data)



