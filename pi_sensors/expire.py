#!/usr/bin/env python

import os
import requests

DEVICE_ID = os.environ['DEVICE_ID']
API_KEY = os.environ['ENVIRO_KEY']
DEBUG = os.getenv('DEBUG')


def main():
    headers = {'Content-type': 'application/json', 'Accept': 'application/json', 'enviro-key': API_KEY}
    r = requests.post('https://api.tippypi.com/v1/sensors/expire?deviceId=' + DEVICE_ID, headers=headers)
    if DEBUG:
        print "tippyapi status code : {}".format(r.status_code)


if __name__=='__main__':
    main()
