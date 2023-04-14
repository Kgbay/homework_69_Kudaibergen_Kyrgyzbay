import json

from django.http import HttpResponse

json_data = {
    "A": 1234,
    "B": 4567
}


def add_view(request, *args, **kwargs):
    answer = {
        'answer': json_data['A'] + json_data['B']
    }
    if request.body:
        answer['content'] = json.loads(request.body)
    answer_as_json = json.dumps(answer)
    response = HttpResponse(answer_as_json, content_type='application/json')
    return response


def substract_view(request, *args, **kwargs):
    answer = {
        'answer': json_data['A'] - json_data['B']
    }
    if request.body:
        answer['content'] = json.loads(request.body)
    answer_as_json = json.dumps(answer)
    response = HttpResponse(answer_as_json, content_type='application/json')
    return response


def multiply_view(request, *args, **kwargs):
    answer = {
        'answer': json_data['A'] * json_data['B']
    }
    if request.body:
        answer['content'] = json.loads(request.body)
    answer_as_json = json.dumps(answer)
    response = HttpResponse(answer_as_json, content_type='application/json')
    return response


def divide_view(request, *args, **kwargs):
    answer = {
        'answer': json_data['A'] // json_data['B']
    }
    if request.body:
        answer['content'] = json.loads(request.body)
    answer_as_json = json.dumps(answer)
    response = HttpResponse(answer_as_json, content_type='application/json')
    return response
