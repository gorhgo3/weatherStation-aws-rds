from django.http import JsonResponse
from django.shortcuts import render
from datetime import datetime
import json

def serveTimeObj(req):
  return JsonResponse({"time": datetime.now()})

def serveDevices(req):
  with open('./TempData/devices.json') as json_file:
    json_data = json.load(json_file)
    return JsonResponse({'devices': json_data})