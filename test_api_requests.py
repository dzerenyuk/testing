import requests
import json
import pytest

class TestSample:
    @pytest.fixture()
    def test_setup(self):
        self.url = "https://swapi.co/api/people/"
        self.payload = ""
        self.headers = {
            'Content-Type': "application/json",
            'User-Agent': "PostmanRuntime/7.20.1",
            'Accept': "*/*",
            'Cache-Control': "no-cache",
            'Postman-Token': "6e290516-c612-41a5-8574-147998735d24,f0936e07-07a8-4cc9-b4f7-b88b63800614",
            'Host': "swapi.co",
            'Accept-Encoding': "gzip, deflate",
            'Cookie': "__cfduid=d219445e6c2d500ebd4b26ef499b7f10a1573830513",
            'Connection': "keep-alive",
            'cache-control': "no-cache"
        }
        self.response = requests.request("GET", self.url, data = self.payload, headers = self.headers)
        self.data = self.response.json()
        self.data_heroes = self.data["results"]


    def test_first_test(self, test_setup):
        assert self.data_heroes[0]['name'] == 'Luke Skywalker'
    def test_second_test(self, test_setup):
        assert self.data_heroes[1]['height'] == '167'
    def test_third_test(self, test_setup):
        assert self.data_heroes[0]['films'][4] == 'https://swapi.co/api/films/7/'

