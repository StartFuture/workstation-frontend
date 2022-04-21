from flask import Flask, render_template, request, redirect, url_for, flash, jsonify

from user import bp as bp_user
from main import bp as bp_main
from box import bp as bp_box
from blog import bp as bp_blog

app = Flask(__name__)

app.register_blueprint(bp_user)
app.register_blueprint(bp_main)
app.register_blueprint(bp_box)
app.register_blueprint(bp_blog)

if __name__ == '__main__':
    app.run(debug=True)