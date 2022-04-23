from flask import Flask, render_template, request, redirect, url_for, flash, jsonify

from user import bp as bp_user
from main import bp as bp_main
from box import bp as bp_box
from blog import bp as bp_blog

app = Flask(__name__)

app.secret_key = 'super secret key'

app.register_blueprint(bp_user)
app.register_blueprint(bp_main)
app.register_blueprint(bp_box)
app.register_blueprint(bp_blog)

@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('errors/erro-400.html'), 404

@app.errorhandler(500)
def page_not_load(e):
    # note that we set the 404 status explicitly
    return render_template('errors/erro-500.html'), 500

if __name__ == '__main__':
    app.run(debug=True)