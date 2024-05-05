import requests
import json


home_url = 'http://localhost:8080'
api_get = '/api/food'
api_post = '/api/food'
api_reset = '/api/data/reset'
url_api_get = home_url + api_get
url_api_post = home_url + api_post
url_api_reset = home_url + api_reset
response = ''


def get_request_check_status():
    response = requests.get(home_url)
    return response.status_code


def get_response():
    return requests.get(home_url)


def response_options():
    response = requests.options(home_url)
    print(response.headers['Allow']) # GET,HEAD,OPTIONS

#response_options()

# получаем все продукты
def get_request_all_product(cookies):
    response = requests.get(url_api_get, cookies=cookies)
    print(response.json())
    return response.json()

def get_last_product():
    list_product = get_request_all_product()
    # получаем список из словарей
    #print(list_product) # [{"name":"Апельсин","type":"FRUIT","exotic":true},{"name":"Капуста","type":"VEGETABLE","exotic":false},{"name":"Помидор","type":"VEGETABLE","exotic":false},{"name":"Яблоко","type":"FRUIT","exotic":false}]
    # выводим последний элемент списка
    print(list_product[-1])
    return list_product[-1]

#get_list_product()


def post_request_add_product(name_prod, type_prod, is_exotic):
    # exotic = None
    # if 'true' == is_exotic.lower: exotic = True
    # if 'false' == is_exotic.lower: exotic = False
    post_params = {'name': name_prod, 'type': type_prod, 'exotic': is_exotic}
    #json_params = {"name":"Mango","type":"FRUIT","exotic": True}
    response = requests.post(url_api_post, json=post_params )
    #cookies = response.cookies.values()[0]
    #cookies = response.cookies
    sess = requests.Session
    print(f'Куки: {response.cookies.values()[0]}')
    #print(response.request)
    #print(f'Заголовок: {response.headers}')
    print(f'Код ответа: {response.status_code}')
    #print(response.request.headers)
    #print(response.request.body)
    print(response.text)
    #return cookies
    return response


def check_add_product(name_prod, type_prod, is_exotic): # name_prod, type_prod, is_exotic
    response = get_request_all_product()
    last_prod = response[-1]
    #print(get_last_product)   # {'name': 'Яблоко', 'type': 'FRUIT', 'exotic': False}
    #print(last_prod['name'])    # Яблоко
    #print(last_prod['type'])    # FRUIT
    #print(last_prod['exotic'])  # False
    if last_prod['name'] == name_prod and last_prod['type'] == type_prod and str(last_prod['exotic']) == is_exotic:
        return True
    return False


session = requests.Session()
response = session.get(url_api_get)
#print(response.text)
print(f'Код ответа: {response.status_code}')
print(f'Последний продукт: {response.json()[-1]}')

post_params = {'name': 'Mango', 'type': 'FRUIT', 'exotic': True}
response = session.post(url_api_post, json=post_params)
print(f'Код ответа: {response.status_code}')
print(f'Заголовок запроса POST: {response.request.headers}')
print(f'Тело запроса POST: {response.request.body}')

response = session.get(url_api_get)
print(f'Код ответа: {response.status_code}')
print(f'Последний продукт: {response.json()[-1]}')

response = session.post(url_api_post)
print(f'Код ответа: {response.status_code}')
