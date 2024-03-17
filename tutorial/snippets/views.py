from django.contrib.auth.models import User
from rest_framework import generics, permissions, renderers, viewsets
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from rest_framework.reverse import reverse
from snippets.models import Snippet
from snippets.permissions import IsOwnerOrReadOnly
from snippets.serializers import SnippetSerializer, UserSerializer

# class SnippetList(generics.ListCreateAPIView):
#     permission_classes=[permissions.IsAuthenticatedOrReadOnly]
    
#     queryset = Snippet.objects.all()
#     serializer_class = SnippetSerializer
    
#     def perform_create(self, serializer):
#         serializer.save(owner=self.request.user)

# class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    
#     queryset = Snippet.objects.all()
#     serializer_class = SnippetSerializer
    
# class SnippetHighlight(generics.GenericAPIView):
#     queryset = Snippet.objects.all()
#     renderer_classes = [renderers.StaticHTMLRenderer]
    
#     def get(self, request, *args, **kwargs):
#         snippet_instance = self.get_object()
#         return Response(snippet_instance.highlighted)


class SnippetViewSet(viewsets.ModelViewSet):
    #  This ViewSet automatically provides `list`, `create`, `retrieve`,
    # `update` and `destroy` actions.
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    
    @action(detail=True, rendered_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, requset, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    
    
    
    
    
    
    
# class UserList(generics.ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
    
# class UserDetail(generics.RetrieveAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    #this viewset automatically provides 'list' and 'retrieve' actions.
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'snippets': reverse('snippet-list', request=request, format=format)
    })  
    
     