#!/usr/bin/env python
from flask import Flask
from app_routes import urls_blueprint

app = Flask(__name__)
app.register_blueprint(urls_blueprint)

if __name__ == "__main__":
    app.run(debug=True)