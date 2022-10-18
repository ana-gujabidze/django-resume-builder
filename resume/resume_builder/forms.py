from django import forms
from tinymce.widgets import TinyMCE

from resume_builder.models import Resume


class ResumeForm(forms.ModelForm):
    professional_summary = forms.CharField(widget=TinyMCE(attrs={"cols": 30, "rows": 10}), label=False)
    user_img = forms.ImageField(label="Image Field")
    career_obj = forms.CharField(widget=TinyMCE(attrs={"cols": 30, "rows": 10}), label=False)
    education = forms.CharField(widget=TinyMCE(attrs={"cols": 30, "rows": 10}), label=False)
    references = forms.CharField(widget=TinyMCE(attrs={"cols": 30, "rows": 10}), label=False)

    class Meta:
        model = Resume
        fields = "__all__"
        exclude = ("created_at",)
        widgets = {
            "job_1_start_dt": forms.TextInput(attrs={"type": "date"}),
            "job_1_end_dt": forms.TextInput(attrs={"type": "date"}),
            "job_2_start_dt": forms.TextInput(attrs={"type": "date"}),
            "job_2_end_dt": forms.TextInput(attrs={"type": "date"}),
        }
        labels = {
            "job_1_start_dt": "Start Date",
            "job_1_end_dt": "End Date",
            "job_1_description": "Position Details",
            "job_2_start_dt": "Start Date",
            "job_2_end_dt": "End Date",
            "job_2_description": "Position Details",
        }

    def __init__(self, *args, **kwargs):
        super(ResumeForm, self).__init__(*args, **kwargs)
        self.fields["professional_summary"].required = False
        self.fields["career_obj"].required = False
        self.fields["education"].required = False
        self.fields["references"].required = False
        self.fields["professional_summary"].required = False
