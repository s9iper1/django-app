import json

from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from products.models import Product
from django.forms.models import model_to_dict
import json
from rest_framework.response import Response
from rest_framework.decorators import api_view
from products.serializers import ProductSerializer


# @api_view(["GET"])
# def api_home(request, *args, **kwargs):
#     instance = Product.objects.all().order_by("?").first()
#     data = {}
#     if instance:
#         data = ProductSerializer(instance).data
#         return Response(data)
#     #     json_data_string = json.dumps(data)
#     # return HttpResponse(json_data_string, headers={"content_type": "application/json"})

@api_view(["POST"])
def api_home(request, *args, **kwargs):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        print(serializer.data)
        data = serializer.data
    return Response(data)
    #     json_data_string = json.dumps(data)
    # return HttpResponse(json_data_string, headers={"content_type": "application/json"})
