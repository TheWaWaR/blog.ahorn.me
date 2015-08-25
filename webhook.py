#!/usr/bin/env python
#coding: utf-8

from flask import Flask

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    print request.args
    print request.form
    print request.data
    return 'ok'

if __name__ == '__main__':
    import sys
    app.run(host='0.0.0.0', port=int(sys.argv[1]))
