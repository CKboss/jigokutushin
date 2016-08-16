import tornado.web
import os.path

from tornado.options import define, options
define("port", default=8000, help="run on the given port", type=int)

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("templates/indexjigoku.php")

class The404Handler(tornado.web.RequestHandler):
    def get(self):
        self.render("templates/404.php")

class JigokuHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("templates/jigoku2.php")

class Index2Handler(tornado.web.RequestHandler):
    def post(self):
        self.render("templates/index2.html",picture="a02.jpg")

if __name__ == "__main__":

    tornado.options.parse_command_line()
    app = tornado.web.Application(
        handlers=[
            (r"/", IndexHandler),
            (r"/404.php",The404Handler),
            (r"/jigoku.php", JigokuHandler),
            (r"/add.php",Index2Handler),
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