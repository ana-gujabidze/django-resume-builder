from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import include, path, re_path

from resume_builder import views

urlpatterns = [
    re_path(r"^add/$", views.ResumeCreateView.as_view(), name="resume_view"),
    re_path(r"^profile_list/$", views.ResumeListView.as_view(), name="profile_list"),
    re_path(r"^edit/(?P<pk>\d+)/$", views.UpdateResumeView.as_view(), name="resume_edit"),
    re_path(r"^remove/(?P<pk>\d+)/$", views.DeleteResumeView.as_view(), name="resume_remove"),
    re_path(r"^pdf/(?P<pk>\d+)/$", views.ResumeDetailView.as_view(), name="resume_detail"),
    path("tinymce/", include("tinymce.urls")),
]
