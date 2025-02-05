from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['POST'])
def generate_code(request):
    if request.method == 'POST':
        prompt = request.data.get('prompt', None)
        if prompt:
            generated_code = f"Generated code based on: {prompt}"
            return Response({"code": generated_code}, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Missing 'prompt' field in the request"}, status=status.HTTP_400_BAD_REQUEST)
    return Response({"error": "Method Not Allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
