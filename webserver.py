#-*- coding:utf-8*-
import os
import sys
cur_path = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0,cur_path)

import utils
import web
import conf
utils.reload_conf()

from  conf import template_path ,session_path

web.config.debug = True

from utils import html,render
import json


urls = (
    r'/', "index",
    r'/hello',"hello",
    )

public_url = (r"/auth",r"/oauth_google_cb",r"/oauth_github_cb",r"/choose_auth")

app = web.application(urls, locals())
application = app.wsgifunc()
web.config.session_parameters['timeout'] = conf.session_timeout
session = web.session.Session(app, web.session.DiskStore(session_path))

def pre_process(handler):
    # env =  web.ctx.env
    url = web.ctx.path
    if url in public_url:
        return handler()
    if not conf.auth_user:
        return handler()

    user = session.get("user","")
    print "user:",user
    # if user in user_white_list:
    #     return  handler()
    return web.found("/choose_auth")

app.add_processor(pre_process)


class index:
    def GET(self):
        return "It'works !"

class hello:
    def GET(self):
        data = web.input()
        info = {"name":"None"}
        if data.get("name"):
            info['name'] = data['name']

        return render.hello(info=info)
    

if __name__ == "__main__":
    app.run()
