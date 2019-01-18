Platron Python SDK
===============
## Установка через pip

```
pip install platron
```

## Тесты

Для запуска тестов нужно выполнить

```
pip install -r requirements-dev.txt
```

Для выполнения тестов на текущей версии python

```
pytest
```

Для выполнения тестов на разных версия проекта

```
tox
```

Модуль тестировался на python 2.7, 3.3, 3.4, 3.5, 3.6

В проекте есть интеграционные тесты. Для запуска нужно создать файл с настройками merchant_settings.py, скопировав его
с файла merchant_settings_sample.py в папке \tests\integration\ и внести свои настройки

## Примеры использования

### 1. Создание транзакции

```python
from platron.request.request_builders.init_payment_builder import InitPaymentBuilder
from platron.request.clients.post_client import PostClient
from platron.sdk_exception import SdkException

client = PostClient('merchant_id', 'secret_key')
request = InitPaymentBuilder('10', 'Test description')

try:
    response = client.request(request)
    print(response)
except SdkException as msg:
    print(msg)
```

### 2. Запрос реестра

```python
from platron.request.request_builders.get_registry_builder import GetRegistryBuilder
from platron.request.clients.post_client import PostClient
from platron.sdk_exception import SdkException

client = PostClient('merchant_id', 'secret_key')
request = GetRegistryBuilder('2017-01-01')

try:
    response = client.request(request)
    print(response)
except SdkException as msg:
    print(msg)
```

### 3. Проведение клиринга 

```python
from platron.request.request_builders.do_capture_builder import DoCaptureBuilder
from platron.request.clients.post_client import PostClient
from platron.sdk_exception import SdkException

client = PostClient('merchant_id', 'secret_key')
request = DoCaptureBuilder('3334455')

try:
    response = client.request(request)
    print(response)
except SdkException as msg:
    print(msg)
```

### 4. Обработка запроса от Platron (check)

```python
from platron.callback import Callback
from platron.sdk_exception import SdkException

order_available = 1
params_from_platron = {}

callback = Callback('merchant_return_url_script', 'sdvsfdvsfdvsdv')
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
```

order_available - вместо переменной метод, проверяющий доступность заказа
