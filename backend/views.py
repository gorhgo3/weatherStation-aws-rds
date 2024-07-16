from django.http import JsonResponse
from django.shortcuts import render
from datetime import datetime

def serveTimeObj(req):
  return JsonResponse({"time": datetime.now()})