from bottle import app
import routes
from bottle_cors_plugin import cors_plugin

app = app()
app.install(cors_plugin('*'))

app.run(host='127.0.0.1', port=8080)