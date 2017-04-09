from django.shortcuts import render
# from django.shortcuts import get_object_or_404, render

from django.http import HttpResponseRedirect, HttpResponse

from django.contrib import messages
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.models import User

from .models import Milestone
from .forms import MilestoneForm


def milestone_list(request):
	milestone  = Milestone.objects.all().order_by('-start_date')
	return render(request, 'milestone_list.html', {'milestone': milestone})


@login_required(login_url='/accounts/login/')
def milestone_create(request):
	if request.method == 'POST':
		form = MilestoneForm(request.POST)
		if form.is_valid():
			title		= form.cleaned_data['title']
			description = form.cleaned_data['description']
			due_date 	= form.cleaned_data['due_date']
			complete 	= form.cleaned_data['complete']

			form.save()
			messages.success(request, "Successfully Created", fail_silently=False)
			return HttpResponseRedirect("/milestones")

	else:
		form = MilestoneForm()
		return render(request, "milestone_create.html", {'form': form})
