Platron Python SDK
===============
## Установка через pip

<pre><code>$ pip install platron_sdk</pre></code>

## Тесты

Для запуска тестов нужно выполнить

<pre><code>$ pip install -r requirements-dev.txt</pre></code>

Для выполнения тестов на текущей версии python

<pre><code>$ pytest</pre></code>

Для выполнения тестов на разных версия проекта

<pre><code>$ tox</pre></code>

Модуль тестировался на python 2.7, 3.3, 3.4, 3.5, 3.6

## Примеры использования

### 1. Создание транзакции

<pre><code>
from platron.request.request_builders.init_payment_builder import InitPaymentBuilder
from platron.request.clients.post_client import PostClient
from platron.sdk_exception import SdkException

client = PostClient('82', 'jkndvjknsdjkvnsjdf')
request = InitPaymentBuilder('10', 'Test description')

try:
    response = client.request(request)
    print(response)
except SdkException as msg:
    print(msg)
</pre></code>

### 2. Запрос реестра

<pre><code>
from platron.request.request_builders.get_registry_builder import GetRegistryBuilder
from platron.request.clients.post_client import PostClient
from platron.sdk_exception import SdkException

client = PostClient('82', 'jkndvjknsdjkvnsjdf')
request = GetRegistryBuilder('2017-01-01')

try:
    response = client.request(request)
    print(response)
except SdkException as msg:
    print(msg)
</pre></code>

### 3. Проведение клиринга 

<pre><code>
from platron.request.request_builders.do_capture_builder import DoCaptureBuilder
from platron.request.clients.post_client import PostClient
from platron.sdk_exception import SdkException

client = PostClient('82', 'jkndvjknsdjkvnsjdf')
request = DoCaptureBuilder('3334455')

try:
    response = client.request(request)
    print(response)
except SdkException as msg:
    print(msg)
</pre></code>

### 4. Обработка запроса от Platron (check)

<pre><code>
from platron.callback import Callback
from platron.sdk_exception import SdkException

order_available = 1
params_from_platron = {}

callback = Callback('sdvsfdvsfdvsdv')
if callback.validate_sig(params_from_platron) :
    if order_available:
        callback.response_ok(params_from_platron)
    else :
        if callback.can_reject(params_from_platron) :
            callback.response_reject(params_from_platron, 'Заказ недоступен для оплаты')
        else :
            ''' Сделать запрос через систему выплат или через заявку на возврат '''
            pass
else:
    callback.response_error(params_from_platron, 'Неправильная подпись')
</pre></code>

order_available - вместо переменной метод, проверяющий доступность заказа