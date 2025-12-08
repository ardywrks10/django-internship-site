from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

class BlogPost(models.Model):
    slug = models.SlugField(
        max_length = 200,
        unique     = True,
        help_text  = "Slug unik untuk URL, misalnya: penerjunan-magang",)

    title = models.CharField(
        max_length = 200,
        help_text  = "Judul blog yang tampil di card dan halaman detail.",)

    description = models.CharField(
        max_length = 255,
        help_text  = "Deskripsi singkat untuk card di halaman utama.",)

    content = models.TextField(
        help_text  = "Isi lengkap artikel (boleh beberapa paragraf).",)

    image = models.CharField(
        max_length = 255,
        help_text  = "Relative static path, e.g. 'theme/assets/img/blog/1.jpeg'",)

    author_name = models.CharField(
        max_length = 100,
        help_text  = "Nama penulis, misalnya 'Kusuma'.",)

    author_image   = models.CharField(
        max_length = 255,
        blank      = True,
        default    = "theme/assets/img/blog/b6.jpg",
        help_text  = "Relative static path untuk avatar penulis.",)

    tag = models.CharField(
        max_length = 100,
        blank      = True,
        help_text  = "Tag pendek, misalnya 'By Kusuma'.",)
    
    view_count     = models.PositiveIntegerField(
        default    = 0,
        help_text  = "Jumlah berapa kali artikel dilihat"
    )

    published_at  = models.DateField(
        help_text = "Tanggal artikel dipublikasikan.",)

    created_at    = models.DateTimeField(auto_now_add=True)
    updated_at    = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-published_at", "-created_at"]

    def __str__(self) -> str:
        return self.title


class Comment(models.Model):
    user = models.ForeignKey(
        User,
        on_delete = models.CASCADE,
        help_text = "User yang memberikan komentar",)

    post = models.ForeignKey(
        BlogPost,
        related_name = "comments",
        on_delete    = models.CASCADE,
        help_text    = "Post yang dikomentari",)

    content = models.TextField(
        help_text = "Isi komentar",)

    created_at    = models.DateTimeField(
        default   = timezone.now,
        help_text = "Waktu ketika komentar dibuat",)

    class Meta:
        ordering = ["created_at"]

    def __str__(self) -> str:
        return f"Comment by {self.user.username} on {self.post.title}"

    def get_absolute_url(self):
        return reverse("public:blog_detail", args=[self.post.slug])
