
from helpers.HttpResponse import HttpResponse

from collections import Counter

from datetime import datetime
@app.route('/', methods=['GET'])
def home():
    return '123'


@app.route('/is_double', methods=['POST'])
def is_double():
    request_data = request.get_json() or {}
    text_1 = request_data.get('text', 0).lower()
    text_2 = request_data.get('text2', 0).lower()

    if text_2 in text_1:
        return HttpResponse.make(data=True)
    else:
        return HttpResponse.make(data=False)


@app.route('/even_digit', methods=['POST'])
def even_digit():
    request_data = request.get_json() or {}
    digit = request_data.get('digit', 0)

    sum = 0

    while digit > 10:
        while digit != 0:
            sum += digit % 10
            digit //= 10
        digit = sum
        sum = 0
    if digit % 2 == 0:
        return HttpResponse.make(data={
            'digit': digit,
            'is_Even': True
        })
    else:
        return HttpResponse.make(data={
            'digit': digit,
            'is_Even': False
        })


@app.route('/get_name', methods=['POST'])
def get_name():
    request_data = request.get_json() or {}
    name = request_data.get('name')
    surname = request_data.get('surname')
    second_name = request_data.get('second_name')

    if not (name and surname):
        return HttpResponse.make(error_text="Поле ввода пусто")

    else:
        return HttpResponse.make(data={
            'name': (name[0]).title(),
            'surname': surname[0].title(),
            'second_name': second_name[0].title()

        })


@app.route('/st', methods=['POST'])
def set_time():
    time = int(datetime.now().time().hour)
    if time >= 6 and time < 12:
        return HttpResponse.make(data={
            'time': "Доброе утро!"
        })
    if time >= 12 and time < 18:
        return HttpResponse.make(data={
            'time': "Добрый день!"
        })
    if time >= 18 and time < 24:
        return HttpResponse.make(data={
            'time': "Добрый вечер!"
        })
    if time >= 0 and time < 6:
        return HttpResponse.make(data={
            'time': "Доброй ночи!"
        })


@app.route('/count', methods=['POST'])
def count_symbol():
    request_data = request.get_json() or {}
    word = request_data.get('word')
    count = int(request_data.get('count'))
    list = []

    for i in word:
        if word.count(i) >= count and i not in list:
            list.append(i)

    return HttpResponse.make(data=list)
