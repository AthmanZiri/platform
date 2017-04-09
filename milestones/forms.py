from django import forms
# from django.contrib.auth.models import User

from .models import Milestone


class MilestoneForm(forms.ModelForm):
	# owner		= forms.ChoiceField()
	description = forms.CharField(max_length=100, required=False, widget=forms.Textarea())
	due_date 	= forms.DateField(widget=forms.SelectDateWidget)
	complete 	= forms.TypedChoiceField(
                   coerce=lambda x: x == 'True',
                   choices=((False, 'False'), (True, 'True')),
                   widget=forms.RadioSelect
                )

	class Meta:
		model  	= Milestone
		fields 	= ('owner', 'title', 'description', 'due_date', 'complete')
