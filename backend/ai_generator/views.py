from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import status

@api_view(['POST', 'GET'])
@parser_classes([JSONParser])
def generate_code(request):
    if request.method == 'POST':
        if not request.data:
            return Response(
                {"error": "Request body is empty or not valid JSON"},
                status=status.HTTP_400_BAD_REQUEST
            )
        prompt = request.data.get('prompt')
    elif request.method == 'GET':
        prompt = request.query_params.get('prompt')

    if prompt:
        generated_code = f"Generated code based on: {prompt}"
        return Response({"code": generated_code}, status=status.HTTP_200_OK)
    else:
        return Response(
            {"error": "Missing 'prompt' field in the request"},
            status=status.HTTP_400_BAD_REQUEST
        )