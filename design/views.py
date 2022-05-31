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