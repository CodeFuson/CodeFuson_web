# backend/views.py

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .main import main

@csrf_exempt
def generate_code(request):
    if request.method == "POST":
        try:

            body = json.loads(request.body)
            prompt = body.get("prompt", "")


            generated_code = main(prompt)


            return JsonResponse({"generated_code": generated_code}, status=200)

        except Exception as e:

            return JsonResponse({"error": str(e)}, status=400)


    else:
        return JsonResponse({"message": "Only POST method is allowed."}, status=405)
