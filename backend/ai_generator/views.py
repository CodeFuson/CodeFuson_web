from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from . import main


@api_view(['POST'])
def generate_code(request):
    try:
        print("Beérkező adatok:", request.data)  # Debug log
        prompt = request.data.get('prompt')
        if not prompt:
            return Response({'error': 'Prompt is required'}, status=status.HTTP_400_BAD_REQUEST)
        generated_code = main(prompt)
        return Response({'code': generated_code}, status=status.HTTP_200_OK)
    except Exception as e:
        print(f"Server Error: {e}")
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
