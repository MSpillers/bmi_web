import os
from flask import Flask, render_template

def create_app():
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY=os.getenv("FLASK_SECRET_KEY") or 'prc9FWjeLYh_KsPGm0vJcg'
    )

    from wsgi.main.views import main
    app.register_blueprint(main)

    return app