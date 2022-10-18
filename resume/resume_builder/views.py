from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, TemplateView, UpdateView

from .forms import ResumeForm
from .models import Resume


class HomepageView(TemplateView):
    template_name = "homepage.html"


class ResumeCreateView(CreateView):
    model = Resume
    form_class = ResumeForm

    def form_valid(self, form):
        user = form.save()
        return redirect("profile_list")


class ResumeListView(ListView):
    paginate_by = 10
    required_field_name = "resume_list.html"
    model = Resume

    def get_queryset(self):
        return Resume.objects.order_by("-created_at")


class UpdateResumeView(UpdateView):
    redirect_field_name = "basic_app/resume_list.html"
    form_class = ResumeForm
    model = Resume


class DeleteResumeView(DeleteView):
    model = Resume
    success_url = reverse_lazy("profile_list")


class ResumeDetailView(DetailView):
    model = Resume

    def get_context_data(self, **kwargs):
        context = super(ResumeDetailView, self).get_context_data(**kwargs)
        return context
