# This is a sample Python script.

import os
import requests

url = os.environ.get('HOST', 'http://localhost:5555/upload')


def send_requests():
    images_dir = "../files"

    for image in os.listdir(images_dir):
        path = os.path.join(images_dir, image)
        file = {'media': open(path, 'rb')}
        headers = {'Content-type': 'image/png'}
        response = requests.post(url, files=file, headers=headers)

        print(response.status_code)


if __name__ == '__main__':
    print("___STARTING UPLOAD TEST___")
    send_requests()
    print("___DONE___")
