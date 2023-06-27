from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import AuthenticationFailed
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .serializer import BookSeriliazer
from .models import Books
from .permissions import CanViewBook, CanEditBook
# Create your views here.

class BearerAuthentication(TokenAuthentication):
    keyword = 'Bearer'

class QueryParameterTokenAuthentication(TokenAuthentication):
    def authenticate(self, request):
        # Extract the token from query parameters
        token = request.query_params.get('key')
        
        if token:
            return self.authenticate_credentials(token)
        else:
            raise AuthenticationFailed('Token not provided in query parameters')

class BookList(APIView):
    # authentication_classes = [QueryParameterTokenAuthentication]
    permission_classes = [IsAuthenticated, CanEditBook]
    def get(self, request):
        print(request.GET)
        books = Books.objects.all()
        serialize = BookSeriliazer(books,many=True)
        return Response(serialize.data)
    def post(self, request):
        serializer = BookSeriliazer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
        return Response(serializer.errors, status = 400)

@api_view(['GET'])
@permission_classes([IsAuthenticated, CanViewBook])
def book_details(request,pk):
    book = get_object_or_404(Books, pk=pk)
    serializer = BookSeriliazer(book)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated, CanEditBook])
def add_books(request):
    serializer = BookSeriliazer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=201)
    return Response(serializer.error,status=400)

@api_view(['GET'])
@permission_classes([IsAuthenticated, CanViewBook])
def get_books(request):
    book = Books.objects.all()
    serializer = BookSeriliazer(book,many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated, CanEditBook])
def delete_book(request,pk):
    book = Books.objects.get(id=pk)
    book.delete()
    return Response(status=204)

@api_view(['PUT'])
@permission_classes([IsAuthenticated, CanEditBook])
def update_book(request,pk):
    book = Books.objects.get(id=pk)
    serializer = BookSeriliazer(book, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)


