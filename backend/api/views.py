from django.http import JsonResponse
import json


def home_view(request, *args, **kwargs):
    body = request.body
    data = {}
    try:
        data = json.loads(body)
    except Exception as ex:
        print('error: ', ex)
    return JsonResponse({"message": data})
