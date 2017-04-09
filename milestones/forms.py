from django import forms
from .models import Milestone


class MilestoneForm(forms.ModelForm):
	description = forms.CharField(max_length=100, required=False, widget=forms.Textarea())
	due_date 	= forms.DateField(widget=forms.SelectDateWidget)
	complete 	= forms.TypedChoiceField(
                   coerce=lambda x: x == 'True',
                   choices=((False, 'False'), (True, 'True')),
                   widget=forms.RadioSelect
                )

	class Meta:
		model  	= Milestone
		fields 	= ('title', 'description', 'due_date', 'complete')
