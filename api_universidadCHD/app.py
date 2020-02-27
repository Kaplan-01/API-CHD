import web  # pip install web.py


urls = (
    '/alumnos/?', 'application.controllers.alumnos.Alumnos',
    '/search/?', 'application.controllers.search.Search',
    '/delete/?', 'application.controllers.delete.Delete',
    '/update/?', 'application.controllers.update.Update',
    '/put/?', 'application.controllers.put.Put',
)


app = web.application(urls, globals())


if __name__ == "__main__":
    web.config.debug = False
    app.run()
