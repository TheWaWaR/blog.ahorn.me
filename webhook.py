#!/usr/bin/env python
# coding: utf-8

import os
import hmac
import hashlib

from flask import Flask, request, current_app

app = Flask(__name__)
app.config['HUB_SECRET'] = os.getenv('HUB_SECRET')


def verify_sign(hub_secret, sign, payload):
    sign_our = hmac.new(hub_secret, payload, hashlib.sha1).hexdigest()
    return sign == 'sha1={}'.format(sign_our)


@app.route('/webhook', methods=['POST'])
def webhook():
    sign = request.headers.get('X-Hub-Signature')
    if not verify_sign(current_app.config['HUB_SECRET'], sign, request.data):
        return 'Invalid Signature', 403

    os.system('git pull')
    os.system('jekyll build')
    return 'ok'


if __name__ == '__main__':
    import sys
    app.run(host='0.0.0.0', port=int(sys.argv[1]))
