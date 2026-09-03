from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PostSerializer
from ...models import Post


@api_view()
def PostList(request):
    return Response({"name":"ali"})

@api_view()
def PostDetail(request,id):
    post = Post.objects.get(pk=id)
    print(post.__dict__)
    serializer = PostSerializer(post)
    print(serializer.__dict__)
    return Response(serializer.data)