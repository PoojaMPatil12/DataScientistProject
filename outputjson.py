import requests

request = requests.get('http://127.0.0.1:8000/')
print(request.json())        # Output: Application is up and running!

info = requests.get('http://127.0.0.1:8000/Information')
print(info.json())         # Output: Information needs to added here
                    