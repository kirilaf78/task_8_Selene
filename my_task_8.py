import requests
import logging

# Set up logging
logging.basicConfig(filename='logs.log', level=logging.INFO)

# Decorator to check the success of API responses
def check_api_response(func):
    def wrapper(*args, **kwargs):
        response = func(*args, **kwargs)
        if isinstance(response, requests.Response) and response.status_code != 200:
            logging.error(f'API request {func.__name__} failed with status code {response.status_code}')
        elif isinstance(response, dict) and not response:
            logging.error(f'API request {func.__name__} failed with empty response')
        return response
    return wrapper

@check_api_response
def get_db(endpoint):
    headers = {"Connection": "keep-alive", "cache-control": "no-cache", "accept-encoding": "gzip, deflate"}
    response = requests.get(endpoint, headers=headers)
    logging.info(f"Request: {endpoint}")
    logging.info(f"Response: {response.status_code}{response.text}")
    return response


@check_api_response
def add_zone(endpoint):
    headers = {"Content-Type": "application/json", "Connection": "keep-alive",
               "cache-control": "no-cache", "accept-encoding": "gzip, deflate"}
    params = {
        "id": 11111,
        "zone": "intersitial",
        "type": "interstitial_rewarded_video"
    }
    response = requests.post(endpoint, headers=headers, json=params, verify=True)
    logging.info(f"Request: {endpoint}")
    logging.info(f"Response: {response.status_code}{response.text}")
    return response


if __name__ == '__main__':
    get_db("https://my-json-server.typicode.com/IlyaKnysh/fake_db/db")
    add_zone("https://my-json-server.typicode.com/IlyaKnysh/fake_db/ad_zones")
