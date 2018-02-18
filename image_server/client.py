import requests
import os

def post(filepath, endpoint="http://35.231.112.69/image"):
    print requests.post(endpoint, files={'image': filepath}, params={'key': os.environ["API_KEY"]})

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description='Upload to the image server.')
    parser.add_argument('path', type=str, help='Path to image')
    parser.add_argument('--endpoint', type=str, help='Endpoint', default="http://35.231.112.69/image")
    args = parser.parse_args()
    post(args.path, args.endpoint)
