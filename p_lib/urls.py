from django.urls import path, include
from p_lib.views import BooksList, BookDetail, ContactsView, BookEdit, AuthorsList, AuthorDetail


app_name = "p_lib"

urlpatterns = [
    path('', BooksList.as_view(), name="index"),
    path('book/<int:pk>', BookDetail.as_view(), name="book-detail"),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('create_book/', BookEdit.as_view(), name='book-edit'),
    path('authors/', AuthorsList.as_view(), name='authors-list'),
    path('authors/<int:pk>', AuthorDetail.as_view(), name='author-detail'),
]