from flask import Flask
web = Flask(__name__)

@web.route("/")
def index():
    return "панель управления"

web.run()