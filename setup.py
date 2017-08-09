from setuptools import setup

setup(name='natural_time_periods',
      version='0.1',
      description='Return start/end dates for natural language time periods',
      url='https://github.com/psychemedia/python-natural-time-periods',
      author='Tony Hirst',
      author_email='tony.hirst@gmail.com',
      license='MIT',
      packages=['natural_time_periods'],
      install_requires=[
          'python-dateutil',
      ],
      zip_safe=False)