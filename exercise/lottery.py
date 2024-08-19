from flask import Flask


# creates an application object
app = Flask(__name__)


# add pages to home page
@app.route('/')
def index():
    return '<h1>This is a home page</h1>'

@app.route('/lottery/<name>')
def index_name(name):
    if name[0].lower() in ['y','z','x','w']:
        return '<h1>Congrats {}! You are the winner!</h1>'.format(name)
    else:
        return '<h1>Sorry {}! You are a loser!</h1>'.format(name)

# if you are running the script 
if __name__ == '__main__':
    app.run()
