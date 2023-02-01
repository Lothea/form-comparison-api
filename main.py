from bottle import route, response, post, request, app, request
from math import log10, floor
import routes
from bottle_cors_plugin import cors_plugin

app = app()
app.install(cors_plugin('*'))

app.run(host='127.0.0.1', port=8080)