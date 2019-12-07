"""import json, requests, sys
if len(sys.argv) < 2:
    print('Usage: quickWeather.py location')
    sys.exit()
#location = ' '.join(sys.argv[1:])
location = 'San Francisco, CA'
url ='http://api.openweathermap.org/data/2.5/forecast/daily?q=%s&cnt=3' % (location)
response = requests.get(url)
response.raise_for_status()
print(response.text)
"""


class Class1:
    def __init__(self):

    def func1(self):
       print("Method func1 of class Class1")
    def func2(self):
        print('Method func2 of class Class1')

class Class2(Class1):
    def func3(self):
        print('Method func3 of Class2')
c = Class2()
print(c.func1())


