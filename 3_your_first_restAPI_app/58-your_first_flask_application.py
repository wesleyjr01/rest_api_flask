"""
    Flask applications are built around requests and responses.
    
        A request is what your browser does. Whenever you go to a 
    Website, you are making a request, and there is a computer
    somewhere on the internet that is receiving that request,
    and that computer has something like a Flask application in
    it.
        So that Flask application receives that request from your
    browser, than then decides what to do with it, and then returns
    back a response.
        For example, one request may be to ask for a certain page's
    home page. Another request may be to ask something called hello.html
    for an html file.
        Another request may be to ask for user number three, for example.
    So requests can be really anything. But the server, the flask application,
    has to be created to be able to understand those requests. So that's the
    key here.

    * '/' means the homepage of the site.

    * The port is a sort of area of the computer where your app is going to
    be receiving your requests and returning your responses through.

    * Once you run the app, you will see:
        Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
     127.0.0.1 is a special IP adress, that is reserved for your computer,
     specificallly.
        So when you acess the 127.0.0.1 adress in your browser, you are acessing
    your own computer.
"""
from flask import Flask

app = Flask(__name__)


@app.route("/")  # example 'http://www.google.com/'
def home():  # this name doesnt matter
    return "Hello, world"


# tell a specific port
app.run(port=5000)
