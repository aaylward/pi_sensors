#!/usr/bin/env python

import time
import json
import os

import requests
import boto3
from envirophat import weather, light

SLEEP_INTERVAL_SECONDS = 1
DEVICE_ID = os.environ['DEVICE_ID']
API_KEY = os.environ['ENVIRO_KEY']
DELIVERY_STREAM = 'pi_sensors'
CLIENT = boto3.client('firehose')


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


def report_to_tippyapi(stats):
    headers = {'Content-type': 'application/json', 'Accept': 'application/json', 'enviro-key': API_KEY}
    r = requests.post('https://api.tippypi.com/v1/sensors', json=stats, headers=headers)


def report_to_firehose(stats):
    CLIENT.put_record(
            DeliveryStreamName=DELIVERY_STREAM,
            Record={ 'Data': json.dumps(stats) + '\n' }
    )


def report_stats():
    stats = get_enviro_line()
    report_to_tippyapi(stats)
    report_to_firehose(stats)


def main():
    while True:
        try:
            report_stats()
        except Exception as e:
            print 'error reporting stats: ', e
        time.sleep(SLEEP_INTERVAL_SECONDS)


if __name__=='__main__':
    main()
