from django.urls import path
from . import views

urlpatterns = [
    path("", views.StartingPageView.as_view(), name="starting-page"),
    path("post/<slug:slug>", views.PostDetailView.as_view(), name="post-detail-page"),
    path('register/', views.registerPage, name="register"),
	path('login/', views.loginPage, name="login"),  
	path('logout/', views.logoutUser, name="logout"),
    path("favourites", views.FavouritesView.as_view(), name="favourites")
]