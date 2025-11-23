from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest, HttpResponse
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator

class AboutView(LoginRequiredMixin, TemplateView):
    template_name = "about.html"

BLOG_POSTS = [
    {
        "slug": "penerjunan-magang",
        "image": "theme/assets/img/blog/1.jpeg",
        "author_name": "Kusuma",
        "author_image": "theme/assets/img/blog/b6.jpg",
        "tag": "By Kusuma",
        "title": "Penerjunan Magang di PT. Dimata Sora Jayate",
        "description": (
            "Lorem Ipsum is simply dummy text of the printing and typesetting industry. "
            "Lorem Ipsum has been the industry's standard."
        ),
        "time": "Agustus 04, 2025",
        "content": (
            "Penerjunan mahasiswa magang Program Studi Ilmu Komputer dilaksanakan "
            "serentak pada 4 Agustus 2025. Enam mahasiswa yang ditempatkan di PT. "
            "Dimata Sora Jayate terbagi ke dalam dua divisi, yaitu <span style='color: black; font-weight: bold;'>Machine Learning (ML)</span> "
            "dan <span style='color: black; font-weight: bold;'>DevOps</span>. Empat mahasiswa tergabung di divisi ML, sementara dua lainnya "
            "di divisi DevOps. Pada hari pertama magang, mentor memberikan "
            "arahan yang terstruktur serta memastikan setiap mahasiswa mendapatkan proyek "
            "yang sejalan dengan konsentrasi masing-masing.\n\n"

            "Perusahaan menyediakan fasilitas belajar yang memadai dan lingkungan yang "
            "mendukung pengembangan kompetensi mahasiswa melalui keterlibatan langsung "
            "dalam proyek industri. Mentor secara berkala memantau perkembangan proyek "
            "yang dikerjakan mahasiswa, sekaligus memberikan arahan apabila terdapat "
            "kendala dalam proses pengerjaan."
        ),
    },
    {
        "slug": "hut-dimata",
        "image": "theme/assets/img/blog/2.jpeg",
        "author_name": "Tim Norton",
        "author_image": "theme/assets/img/blog/b6.jpg",
        "tag": "BY TIM NORTON",
        "title": "The newest web framework that changed the world",
        "description": (
            "Lorem Ipsum is simply dummy text of the printing and typesetting industry. "
            "Lorem Ipsum has been the industry's standard."
        ),
        "time": "March 20, 2023",
        "content": (
            "Di artikel ini kamu bisa cerita tentang framework yang kamu pakai "
            "waktu magang, misalnya Django, FastAPI, Next.js, dsb, dan bagaimana "
            "framework itu membantu menyelesaikan project."
        ),
    },
    {
        "slug": "optical-character-recognition",
        "image": "theme/assets/img/blog/3.jpeg",
        "author_name": "Tim Norton",
        "author_image": "theme/assets/img/blog/b6.jpg",
        "tag": "BY TIM NORTON",
        "title": "5 ways to improve user retention for your startup",
        "description": (
            "Lorem Ipsum is simply dummy text of the printing and typesetting industry. "
            "Lorem Ipsum has been the industry's standard."
        ),
        "time": "March 25, 2023",
        "content": (
            "Ini bisa kamu kaitkan ke fitur-fitur yang kamu buat di project magang "
            "yang berhubungan dengan UX, notifikasi, dashboard, dsb."
        ),
    },
    {
        "slug": "kunjungan-dospem-1",
        "image": "theme/assets/img/blog/4.jpg",
        "author_name": "Tim Norton",
        "author_image": "theme/assets/img/blog/b6.jpg",
        "tag": "BY TIM NORTON",
        "title": "5 ways to improve user retention for your startup",
        "description": (
            "Lorem Ipsum is simply dummy text of the printing and typesetting industry. "
            "Lorem Ipsum has been the industry's standard."
        ),
        "time": "March 30, 2023",
        "content": (
            "Ini bisa kamu kaitkan ke fitur-fitur yang kamu buat di project magang "
            "yang berhubungan dengan UX, notifikasi, dashboard, dsb."
        ),
    },
]

def index(request: HttpRequest) -> HttpResponse:
    blog_posts  = BLOG_POSTS
    paginator   = Paginator(blog_posts, 3)
    page_number = request.GET.get("page")
    page_obj    = paginator.get_page(page_number)
    context     = {
        "page_obj": page_obj,
        "blog_posts": page_obj,
    }
    return render(request, "index.html", context)

def blog_detail(request: HttpRequest, slug: str) -> HttpResponse:
    blog_post = next((post for post in BLOG_POSTS if post["slug"] == slug), None)
    if blog_post is None:
        from django.http import Http404
        raise Http404("Blog post not found")

    return render(request, "blog_detail.html", {"post": blog_post})

