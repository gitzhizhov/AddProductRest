import requests


home_url = 'http://localhost:8080'
api_get = '/api/food'
api_post = '/api/food'
url_api_get = home_url + api_get
url_api_post = home_url + api_post
response = None

session = requests.Session()

def request_get_check_status():
    response = session.get(home_url)
    #print(response.status_code)
    return response.status_code


def request_get_all_product():
    response = session.get(url_api_get)
    #print(f'Код ответа: {response.status_code}')
    #print(f'Последний продукт: {response.json()[-1]}')
    #print(response.json())
    return response.json()



def request_post_add_product(param):
    #post_params = {'name': 'Mango', 'type': 'FRUIT', 'exotic': True}
    post_params = param
    response = session.post(url_api_post, json=post_params)
    #print(f'Код ответа: {response.status_code}')
    #print(f'Заголовок запроса POST: {response.request.headers}')
    #print(f'Тело запроса POST: {response.request.body}')
    return response.status_code


def check_add_product():
    response = session.get(url_api_get)
    #print(f'Код ответа: {response.status_code}')
    #print(f'Последний продукт: {response.json()[-1]}')
    return response.json()[-1]


# print(request_get_check_status())
# print(request_get_all_product())
# print(request_post_add_product())
# print(check_add_product())