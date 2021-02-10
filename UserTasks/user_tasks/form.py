from django import forms

from .models import User, Task


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            "name",
        ]


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = [
            "description",
            "status",
            "user"
        ]
        widgets = {'user': forms.HiddenInput(), "status": forms.HiddenInput()}
