from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Album


class AlbumHomeView(TemplateView):
    template_name = 'albums/home.html'
    model = Album


class AlbumListView(ListView):
    template_name = 'albums/album_list.html'
    model = Album


class AlbumDetailView(DetailView):
    template_name = 'albums/album_detail.html'
    model = Album
    context_object_name = 'album_detail'


class AlbumCreateView(CreateView):
    template_name = 'albums/album_create.html'
    model = Album
    fields = ['author', 'title', 'band' ,'release_year', 'description', 'rating']


class AlbumUpdateView(UpdateView):
    template_name = 'albums/album_update.html'
    model = Album
    fields = ['title', 'band' ,'release_year', 'description', 'rating']


class AlbumDeleteView(DeleteView):
    template_name = 'albums/album_delete.html'
    model = Album
    success_url = reverse_lazy('album_list')