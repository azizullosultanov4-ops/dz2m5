from django.urls import path
from apps.books.views import BookListCreateAPIView

urlpatterns = [
    path('books/', BookListCreateAPIView.as_view()),
]
