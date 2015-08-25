#!/usr/bin/env python
#coding: utf-8

import os
import json

from flask import Flask, request

app = Flask(__name__)


@app.route('/webhook', methods=['POST'])
def webhook():
    data = json.loads(request.data)
    if data['actor']['username'].lower() == 'thewawar':
        os.system('git pull')
        os.system('jekyll build')
        return 'ok'


if __name__ == '__main__':
    import sys
    app.run(host='0.0.0.0', port=int(sys.argv[1]))
