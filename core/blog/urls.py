from django.urls import path
from . import views
from django.views.generic import TemplateView
from django.views.generic.base import RedirectView

app_name = "blog"

urlpatterns = [
    path("cbv-index",views.Indexview.as_view(), name="cbv-index"),
    path("post/",views.PostListView.as_view(), name="post_list"),
    path("post/<int:pk>/", views.PostDetailView.as_view(), name = "post-detail"),
    path("post/create/", views.PostCreateView.as_view(), name= "post-create"),
    path("go-to-maktabkhooneh/<int:pk>/",views.RedirectTomaktab.as_view(),name="go-to-maktabkhooneh"),
]