import tornado.ioloop
import tornado.web
from pymongo import Connection

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        json = self.get_argument('json', "Hello World");
        self.write(json)

    def post(self):
        conn = Connection()
        db = conn.First
        appCollection = db.app1
        json = self.get_argument('json', 'Hello World~')
        json = json[1,len(json)-1]
        appCollection.insert(json)
#        app1 = appCollection.find()
#        appCollection.insert({'name':'test'})
        self.write(json)
        

if __name__ == "__main__":
    application = tornado.web.Application([(r"/AnalyseServer", MainHandler)])
    application.listen(8080)
    tornado.ioloop.IOLoop.instance().start()
