from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest, HttpResponse
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

class AboutView(LoginRequiredMixin, TemplateView):
    template_name = "about.html"

BLOG_POSTS = [
    {
        "slug": "design-driven-team",
        "image": "theme/assets/img/blog/1.jpg",
        "author_name": "Tim Norton",
        "author_image": "theme/assets/img/blog/b6.jpg",
        "tag": "BY TIM NORTON",
        "title": "Make your team a Design driven company",
        "description": (
            "Lorem Ipsum is simply dummy text of the printing and typesetting industry. "
            "Lorem Ipsum has been the industry's standard."
        ),
        "content": (
            "Ini nanti bisa kamu isi dengan versi panjang artikelnya. "
            "Bisa beberapa paragraf yang menjelaskan pengalaman magang, "
            "apa yang kamu kerjakan, tantangan, dan lesson learned.\n\n"
            "Kamu bisa mulai dengan: During my internship, I worked on ... "
        ),
    },
    {
        "slug": "new-web-framework",
        "image": "theme/assets/img/blog/2.jpg",
        "author_name": "Tim Norton",
        "author_image": "theme/assets/img/blog/b6.jpg",
        "tag": "BY TIM NORTON",
        "title": "The newest web framework that changed the world",
        "description": (
            "Lorem Ipsum is simply dummy text of the printing and typesetting industry. "
            "Lorem Ipsum has been the industry's standard."
        ),
        "content": (
            "Di artikel ini kamu bisa cerita tentang framework yang kamu pakai "
            "waktu magang, misalnya Django, FastAPI, Next.js, dsb, dan bagaimana "
            "framework itu membantu menyelesaikan project."
        ),
    },
    {
        "slug": "improve-user-retention",
        "image": "theme/assets/img/blog/3.jpg",
        "author_name": "Tim Norton",
        "author_image": "theme/assets/img/blog/b6.jpg",
        "tag": "BY TIM NORTON",
        "title": "5 ways to improve user retention for your startup",
        "description": (
            "Lorem Ipsum is simply dummy text of the printing and typesetting industry. "
            "Lorem Ipsum has been the industry's standard."
        ),
        "content": (
            "Ini bisa kamu kaitkan ke fitur-fitur yang kamu buat di project magang "
            "yang berhubungan dengan UX, notifikasi, dashboard, dsb."
        ),
    },
]

def index(request: HttpRequest) -> HttpResponse:
    context = {
        "blog_posts": BLOG_POSTS,
    }
    return render(request, "index.html", context)

def blog_detail(request: HttpRequest, slug: str) -> HttpResponse:
    blog_post = next((post for post in BLOG_POSTS if post["slug"] == slug), None)
    if blog_post is None:
        from django.http import Http404
        raise Http404("Blog post not found")

    return render(request, "blog_detail.html", {"post": blog_post})

