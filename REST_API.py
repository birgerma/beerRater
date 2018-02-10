from flask import Flask, abort, request
import json
import sys
#from pythonTclManager import *

app = Flask(__name__)
#tclManager = TclSessionManager()


@app.route('/',defaults={'version': "latest"},methods=['GET'])
@app.route('/<version>',methods=['GET'])
def index(version):
    return("Hello, World! (version=" + str(version) + ")")

@app.route('/<version>/stores',methods=['GET'])
@app.route('/stores',defaults={'version': "latest"},methods=['GET'])
def createNewTclSession(version):
    return("Avalible stores (version=" + str(version) + ")")

@app.route('/<version>/beers',methods=['GET'])
@app.route('/beers',defaults={'version': "latest"},methods=['GET'])
def executeProc(version):
#    data = json.loads(request.data)
    # sessionId = data['id']
    # procName = data['proc']
    # args = data['args']
    # tcl = tclManager.getSession(sessionId)
    return("Avalible beers (version=" + version + ")")

def startServer(port=5000, debug=False):
    app.run(debug=debug,port=int(port))

if __name__ == '__main__':
    args = sys.argv
    if (len(args)>1):
        port = args[1]
    else:
        port = 5000
    app.run(debug=True,port=int(port),host='0.0.0.0')
