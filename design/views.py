from multiprocessing import context
from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views import View
from .models import Post
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from . forms import CommentForm, CreateUserForm
from django.db.models import Q
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

# Create your views here.

class StartingPageView(ListView):
    template_name = "design/index.html"
    model = Post
    context_object_name = "posts"


class PostDetailView(View):
    def is_favourite(self, request, post_id):
        favourite = request.session.get("favourite")
        if favourite is not None:
            is_added_to_favourites = post_id in favourite
        else:
            is_added_to_favourites = False

        return is_added_to_favourites


    def get(self, request, slug):
        post = Post.objects.get(slug=slug)
        context = {
            "post": post,
            "comment_form": CommentForm(),
            "comments": post.comments.all().order_by("-id"),
            "favourites": self.is_favourite(request, post.id),
            "added_to_favourites": self.is_favourite(request, post.id)
        }

        return render(request, "design/post-detail.html", context)
        


    def post(self, request, slug):
        comment_form = CommentForm(request.POST)
        post = Post.objects.get(slug=slug)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            return HttpResponseRedirect(reverse("post-detail-page", args=[slug]))

        context = {
            "post": post,
            "comment_form": comment_form,
            "comments": post.comments.all().order_by("-id"),
            "favourites": self.is_favourite(request, post.id),
            "added_to_favourites": self.is_favourite(request, post.id)
        }

        return render(request, "design/post-detail.html", context)
