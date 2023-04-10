from flask import Flask, request

app = Flask(__name__)

@app.route('/hello')
def index():
    name = request.args.get('name', default='World')
    return 'Hello ' + str(name)

@app.route('/hello-json')
def index2():
    return {"text": "Hello World from Dictionary"}

@app.route('/hello-html')
def index3():
    return "<h1>Hello World</h1><p>Subtext</p>"

@app.route('/hello-html-error')
def index4():
    return "<h1>Not Found</h1><p>The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again.</p>"

@app.route('/hello/<name>')
def whatevername(name):
   return 'Hello ' + str(name)

@app.route('/hello/<name>/change/<amount>')
def changeFunc(name, amount):
    return 'Hello ' + str(name) + ', your change is ' + str(10 - int(amount))

@app.route('/reflect', methods = ['POST'])
def reflect():
    data = request.data
    return 'Hello ' + str(data)

@app.route('/reflect/plex', methods = ['POST'])
def reflectPlex():
    data = request.json
    newData = {}
    for i in data:
        if (isinstance(data[i], str)):
            newData['plex_' + i] = 'plex_' + data[i]
        else:
            newData['plex_' + i] = data[i]
    return newData

@app.route('/reflect/plex/form', methods = ['POST'])
def reflectPlexForm():
    data = request.form
    newData = {}
    for i in data:
        newData['plex_' + i] = 'plex_' + str(data[i])
    return newData

app.run(host='0.0.0.0', port=81)