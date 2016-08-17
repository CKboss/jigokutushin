import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import os.path
from datetime import datetime

from tornado.options import define, options
define("port", default=8000, help="run on the given port", type=int)

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("templates/indexjigoku.php")

class The404Handler(tornado.web.RequestHandler):
    def get(self):
        self.render("templates/404.php")

class FlameHandler(tornado.web.RequestHandler):
    def get(self):
        now = datetime.now()
        if now.hour == 0 and now.minute <= 10:
            self.render("templates/fireindex.html", picture='flame.gif')
        else :
            self.render("templates/404.php")

class JigokuHandler(tornado.web.RequestHandler):
    def get(self):
        now = datetime.now()
        if now.hour==0 and now.minute<=10 :
            self.render("templates/jigoku2.php")
        else :
            self.render("templates/404.php")


class Index2Handler(tornado.web.RequestHandler):
    def post(self):
        now = datetime.now()
        if now.hour == 0 and now.minute <= 10:
            self.render("templates/index2.html",picture="a02.jpg")
        else:
            self.render("templates/404.php")

if __name__ == "__main__":


    tornado.options.parse_command_line()
    app = tornado.web.Application(
        handlers=[
            (r"/", IndexHandler),
            (r"/404.php",The404Handler),
            (r"/jigoku.php", JigokuHandler),
            (r"/add.php",Index2Handler),
            (r"/flame.php",FlameHandler),
            (r"/.*",The404Handler),
        ],

        settings=dict(
            debug=False,
            gzip=True,
        ),

        static_path=os.path.join(os.path.dirname(__file__), "statics"),
    )

    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()