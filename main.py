from flask import Flask, request, jsonify, make_response, render_template, send_from_directory
from flask_cors import CORS
''
app = Flask(__name__, static_url_path='',
            static_folder='static',
            template_folder='templates')
CORS(app)

@app.route('/')
def main():
    """Entry point; the view for the main page"""
    return render_template('login.html')

@app.route('/dashboard')
def main_dashboard():
    """Entry point; the view for the main page"""
    return render_template('dashboard.html')


@app.route('/user_master')
def main_user():
    """Entry point; the view for the main page"""
    return render_template('user_master.html')

if __name__ == "__main__":
    app.run(host="localhost", port=8000, debug=True)













































