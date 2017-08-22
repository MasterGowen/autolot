from flask import Flask, session, g, render_template
from flask_assets import Environment, Bundle

from datetime import datetime
import os
import glob

from backend.views import main

app = Flask(__name__)
assets = Environment(app)
app.config.from_object('config')

STATIC_DIR = os.path.join(app.root_path, "static")
ts_counter = len(list(glob.iglob(STATIC_DIR + "/**/*.ts", recursive=True)))
js_counter = len(list(glob.iglob(STATIC_DIR + "/**/*.js", recursive=True)))
css_counter = len(list(glob.iglob(STATIC_DIR + "/**/*.scss", recursive=True)))


if ts_counter > 0:
    ts = Bundle(
        "**/*.ts",
        filters='typescript,jsmin',
        output='static/main_ts.js'
    )
    assets.register("main_ts", ts)

if js_counter > 0:
    js = Bundle(
        "**/*.js",
        filters='jsmin',
        output='static/main_js.js'
    )
    assets.register("main_js", js)

if css_counter > 0:
    css = Bundle(
        "**/*.scss",
        filters='scss',
        output='static/main.css'
    )

    assets.register("main_css", css)


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404


@app.context_processor
def current_year():
    return {'current_year': datetime.utcnow().year}


app.register_blueprint(main.mod)


# if app.debug:
#     from flask import send_from_directory
#
#     @app.route('/favicon.ico')
#     def favicon():
#         return send_from_directory(os.path.join(app.root_path, 'static'),
#                                    'favicon.ico', mimetype='image/vnd.microsoft.icon')
#
#     @app.route('/js/<path:path>')
#     def send_js(path):
#         return send_from_directory('/static/js', path)
#
#
#     @app.route('/css/<path:path>')
#     def send_css(path):
#         return send_from_directory('/static/css', path)
#
#
#     @app.route('/img/<path:path>')
#     def send_img(path):
#         return send_from_directory('/static/img', path)
