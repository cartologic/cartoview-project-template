from django.conf import settings
import cherrypy
from {{project_name}}.wsgi import application

from cherrypy import tools
if __name__ == '__main__':
    # For SSL Support server.ssl_module = 'pyopenssl' server.ssl_certificate =
    # 'ssl/certificate.crt' server.ssl_private_key = 'ssl/private.key'
    # server.ssl_certificate_chain = 'ssl/bundle.crt' Subscribe this server


    config = {
        'tools.staticdir.on': True,
        'tools.staticdir.dir': settings.STATIC_ROOT,
        'tools.expires.on': True,
        'tools.expires.secs': 86400
    }
    cherrypy.tree.mount(None, settings.STATIC_URL, {'/': config})

    config = {
        'tools.staticdir.on': True,
        'tools.staticdir.dir': settings.MEDIA_ROOT,
        'tools.expires.on': True,
        'tools.expires.secs': 86400
    }
    cherrypy.tree.mount(None, settings.MEDIA_URL, {'/': config})

    cherrypy.config.update({
        "server.socket_host": "0.0.0.0",
        "server.socket_port": 8000,
        "server.thread_pool": 30,
        "server.max_request_body_size": 0,
        "server.socket_timeout": 10000000})

    # Mount the application
    cherrypy.tree.graft(application)

    cherrypy.engine.start()
    cherrypy.engine.block()

