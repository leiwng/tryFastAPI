import requests

people = {'name':'Robert.Bob', 'age':32, 'address':'杭州南路320号', 'salary': 19999}
requests.post('http://127.0.0.1:8000/insert', json=people).json()
requests.get('http://127.0.0.1:8000/')