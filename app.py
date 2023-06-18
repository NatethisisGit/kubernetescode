from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Please subscribe, like, and comment on this video, TY!!! And if you dont that will not be cool '
