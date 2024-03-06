from django.http import Http404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from snippets.models import Snippet
from snippets.serializers import SnippetSerializer

class SnippetList(APIView):  
    def get(self, request, format=None):
        snippet_instance = Snippet.objects.all()
        serializer = SnippetSerializer(snippet_instance, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer_instance = SnippetSerializer(data=request.data)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data, status=status.HTTP_201_CREATED)
        return Response(serializer_instance.errors, status=status.HTTP_400_BAD_REQUEST)
    
# @api_view(['GET', 'POST'])
# def snippet_list(request, format=None):
#     if request.method == 'GET':
#         snippet_object = Snippet.objects.all()
#         serializer = SnippetSerializer(snippet_object, many=True)
#         return Response(serializer.data)
        
#     if request.method == 'POST':
#         serializer = SnippetSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
class SnippetDetail(APIView):
    def get_object(self, pk):
        try:
            return Snippet.objects.get(pk=pk)
        except Snippet.DoesNotExist:
            raise Http404
    
    def get(self, request, pk, format=None):
        snippet_instance = self.get_object(pk)
        serializer_instance = SnippetSerializer(snippet_instance)
        return Response(serializer_instance.data)
    
    def put(self, requset, pk, format=None):
        snippet_instance = self.get_object(pk)
        serializer_instance = SnippetSerializer(snippet_instance, data=requset.data)
        if serializer_instance.is_valid():
            serializer_instance.save
            return Response(serializer_instance.data)
        return Response(serializer_instance.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        snippet_instance = self.get_object(pk)
        snippet_instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# @api_view(['GET', 'PUT', 'DELETE'])
# def snippet_detail(request, pk, format=None):
#     try:
#         snippet_instance = Snippet.objects.get(pk=pk)
#     except Snippet.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
        
#     if request.method == 'GET':
#         serializer = SnippetSerializer(snippet_instance)
#         return Response(serializer.data)

#     elif request.method == 'PUT':
#         serializer = SnippetSerializer(snippet_instance, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         snippet_instance.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
    
    