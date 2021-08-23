from django import forms
from .models import TaskModel


class NewTaskForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'validate', 'autofocus': 'autofocus'}), required=True)
    description = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'validate'}), required=True)
    priority = forms.ChoiceField(label="Set Priority",
                                 choices=[(3, "High"), (2, "Medium"), (1, "Low")])

    class Meta:
        model = TaskModel
        fields = ('title', 'description', 'priority')
