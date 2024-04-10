from flask import Flask, render_template

app = Flask(__name__)

# Define a route for the homepage
@app.route('/')
def index():
    return 'Hello Isha!'

# Define another route
@app.route('/about')
def about():
    return 'About page'

if __name__ == '__main__':
    app.run(debug=True)
