from django.shortcuts import render, get_object_or_404, redirect, resolve_url
from django.http import HttpRequest, HttpResponse
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.conf import settings 

from .models import BlogPost, Comment
from .forms import CommentForm

class AboutView(LoginRequiredMixin, TemplateView):
    template_name = "about.html"

def index(request: HttpRequest) -> HttpResponse:
    blog_posts_qs = BlogPost.objects.all()
    paginator     = Paginator(blog_posts_qs, 3)
    page_number   = request.GET.get("page")
    page_obj      = paginator.get_page(page_number)

    context = {
        "page_obj": page_obj,
        "blog_posts": page_obj,
    }
    return render(request, "index.html", context)

def blog_detail(request: HttpRequest, slug: str) -> HttpResponse:
    post = get_object_or_404(BlogPost, slug=slug)
    if request.method == "GET":
        post.view_count += 1
        post.save(update_fields=["view_count"])

    comments    = post.comments.all()
    pending_key = f"pending_comment_{post.slug}"

    if request.method == "GET" and request.user.is_authenticated:
        pending_content = request.session.pop(pending_key, None)
        if pending_content:
            Comment.objects.create(
                user=request.user,
                post=post,
                content=pending_content,
            )
            return redirect(request.path)

    if request.method == "POST":
        comment_form = CommentForm(request.POST)

        if not request.user.is_authenticated:
            if comment_form.is_valid():
                request.session[pending_key] = comment_form.cleaned_data["content"]

            login_url = resolve_url(settings.LOGIN_URL)
            return redirect(f"{login_url}?next={request.path}")

        if comment_form.is_valid():
            comment      = comment_form.save(commit=False)
            comment.user = request.user
            comment.post = post
            comment.save()
            return redirect(request.path)
    else:
        comment_form = CommentForm()

    context = {
        "post": post,
        "comment_form": comment_form,
        "comments": comments,
    }
    return render(request, "blog_detail.html", context)

