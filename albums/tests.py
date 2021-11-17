from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Album

class TestAlbums(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="admin", email="admin@admin.com", password="secretpassword"
        )

        self.album = Album.objects.create(
            title="Sovran",band = 'Draconian' , description="Awesome.", author=self.user, rating = 8, release_year = 2000,
        )

    def test_string_representation(self):
        self.assertEqual(str(self.album), "Sovran")

    def test_album_content(self):
        self.assertEqual(f"{self.album.title}", "Sovran")
        self.assertEqual(f"{self.album.author}", "admin@admin.com")
        self.assertEqual(self.album.description, "Awesome.")

    def test_album_list_view(self):
        response = self.client.get(reverse("album_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Sovran")
        self.assertTemplateUsed(response, "albums/album_list.html")

    def test_album_detail_view(self):
        response = self.client.get(reverse("album_detail", args="1"))
        no_response = self.client.get("/100000/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, "admin")
        self.assertTemplateUsed(response, "albums/album_detail.html")

    def test_album_create_view(self):
        response = self.client.post(
            reverse("album_create"),
            {
                "title": "Moon Flowers",
                "band": "Swallow The Sun",
                "author": self.user.id,
                "description": "Awesome",
                "rating": 5,
                "release_year": 2001,
            }, follow=True
        )
        self.assertRedirects(response, reverse("album_detail", args="2"))
        self.assertContains(response, "Moon Flowers")

    def test_album_update_view_redirect(self):
        response = self.client.post(
            reverse("album_update", args="1"),
            {"title": "Updated name","description":"Sad.","author":self.user.id, "band": "Swallow The Moon","rating": 10,"release_year": 2011}
        )

        self.assertRedirects(response, reverse("album_detail", args="1"))

    def test_album_delete_view(self):
        response = self.client.get(reverse("album_delete", args="1"))
        self.assertEqual(response.status_code, 200)