from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import GoodsSerializer
from .models import Goods


class SnippetList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        snippets = Goods.objects.all()[:10]
        serializer = GoodsSerializer(snippets, many=True)
        return Response(serializer.data)