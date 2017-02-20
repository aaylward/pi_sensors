#!/usr/bin/env python

import time
import boto3
import json
from envirophat import weather, light

DELIVERY_STREAM = 'pi_sensors'
SLEEP_INTERVAL_SECONDS = 1

CLIENT = boto3.client('firehose');


def millis():
    return int(round(time.time() * 1000))


def get_enviro_line():
    sensor_data = {
        'temperature': weather.temperature(),
        'pressure': weather.pressure(),
        'light': light.light(),
        'time': millis()
    }

    return json.dumps(sensor_data) + '\n'


def report_stats():
    CLIENT.put_record(
        DeliveryStreamName=DELIVERY_STREAM,
        Record={ 'Data': get_enviro_line() }
    )


def main():
    while True:
        report_stats()
        time.sleep(SLEEP_INTERVAL_SECONDS)


if __name__=='__main__':
    main()
