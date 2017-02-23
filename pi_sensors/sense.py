#!/usr/bin/env python

import time
import json
import os
import requests
from envirophat import weather, light

SLEEP_INTERVAL_SECONDS = 1
DEVICE_ID = os.environ['DEVICE_ID']
API_KEY = os.environ['ENVIRO_KEY']


def millis():
    return int(round(time.time() * 1000))


def get_enviro_line():
    return {
        'temperature': weather.temperature(),
        'pressure': weather.pressure(),
        'light': light.light(),
        'deviceId': DEVICE_ID,
        'time': millis()
    }


def report_stats():
    headers = {'Content-type': 'application/json', 'Accept': 'application/json', 'enviro-key': API_KEY}
    r = requests.post('https://api.tippypi.com/v1/sensors', json=get_enviro_line(), headers=headers)
    print r.status_code


def main():
    while True:
        try:
            report_stats()
        except Exception as e:
            print 'error reporting stats: ', e
        time.sleep(SLEEP_INTERVAL_SECONDS)


if __name__=='__main__':
    main()
