import requests
import json
import pytest

<<<<<<< HEAD

class TestRequest:
    @pytest.fixture()
    def test_setup(self):
        self.url = "https://swapi.co/api/people/"
        payload = ""
        headers = {
=======
class TestSample:
    @pytest.fixture()
    def test_setup(self):
        self.url = "https://swapi.co/api/people/"
        self.payload = ""
        self.headers = {
>>>>>>> origin/master
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
<<<<<<< HEAD
        response = requests.request("GET", self.url, data = payload, headers = headers)
        self.data = response.json()
=======
        self.response = requests.request("GET", self.url, data = self.payload, headers = self.headers)
        self.data = self.response.json()
>>>>>>> origin/master
        self.data_heroes = self.data["results"]


    def test_first_test(self, test_setup):
<<<<<<< HEAD
        assert self.data_heroes[0]["name"] == 'Luke Skywalker'

    def test_second_test(self, test_setup):
        assert self.data_heroes[1]["mass"] == "75"













=======
        assert self.data_heroes[0]['name'] == 'Luke Skywalker'
    def test_second_test(self, test_setup):
        assert self.data_heroes[1]['height'] == '167'
    def test_third_test(self, test_setup):
        assert self.data_heroes[0]['films'][4] == 'https://swapi.co/api/films/7/'
>>>>>>> origin/master

