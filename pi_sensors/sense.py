#!/usr/bin/env python

import time
import boto3
import json
from concurrent.futures import ProcessPoolExecutor as Pool
from envirophat import weather, light

DELIVERY_STREAM = 'pi_sensors'
SLEEP_INTERVAL_SECONDS = 1


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
    boto3.client('firehose').put_record(
        DeliveryStreamName=DELIVERY_STREAM,
        Record={ 'Data': get_enviro_line() }
    )


def main():
    with Pool() as executor:
        while True:
            executor.submit(report_stats)
            time.sleep(SLEEP_INTERVAL_SECONDS)


if __name__=='__main__':
    main()
