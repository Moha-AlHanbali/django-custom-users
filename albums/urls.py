from django.urls import path
from .views import AlbumHomeView, AlbumListView, AlbumDetailView, AlbumCreateView, AlbumUpdateView, AlbumDeleteView


urlpatterns = [
    path('', AlbumHomeView.as_view(), name = 'home'),
    path('albums/', AlbumListView.as_view(), name = 'album_list'),
    path('albums/<int:pk>/', AlbumDetailView.as_view(), name = 'album_detail'),
    path('albums/create/', AlbumCreateView.as_view(), name = 'album_create'),
    path('albums/<int:pk>/update/', AlbumUpdateView.as_view(), name = 'album_update'),
    path('albums/<int:pk>/delete/', AlbumDeleteView.as_view(), name = 'album_delete'),
]