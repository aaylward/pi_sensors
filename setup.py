from distutils.core import setup
setup(
  name = 'pi_sensors',
  packages = ['pi_sensors'],
  install_requires=[
    'boto3',
    'envirophat',
  ],
  version = '0.1',
  description = 'Send Enviro-phat data to kinesis firehose',
  author = 'Andy Aylward',
  author_email = 'aaylward@gmail.com',
  url = 'https://github.com/aaylward/pi_sensors',
  download_url = 'https://github.com/aaylward/pi_sensors/tarball/0.1',
  keywords = ['raspberry pi', 'enviro-phat', 'kinesis', 'firehose'],
  classifiers = [],
  entry_points = {
    'console_scripts': ['sense=pi_sensors.sense:main'],
  },
)
