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

def report_stats():
    client = boto3.client('firehose')

    sensor_data = {
        'temperature': weather.temperature(),
        'pressure': weather.pressure(),
        'light': light.light(),
        'time': millis()
    }

    client.put_record(
        DeliveryStreamName=DELIVERY_STREAM,
        Record={ 'Data': json.dumps(sensor_data) }
    )


def main():
    with Pool() as executor:
        while True:
            executor.submit(report_stats)
            time.sleep(SLEEP_INTERVAL_SECONDS)


if __name__=='__main__':
    main()
