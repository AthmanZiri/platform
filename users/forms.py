from django import forms
<<<<<<< HEAD
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

from .models import Profile


class SignUpForm(UserCreationForm):
    email = forms.EmailField(
        max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2',)


class ProfileForm(UserChangeForm):

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        del self.fields['password']

    class Meta:
        model = Profile
        fields = ('bio', 'gender', 'phone_number',
                  'expectations', 'current_occupation')
=======

from users.models import MenteeApplication, MentorApplication


class ApplicationForm(forms.ModelForm):

    def save(self, *args, **kwargs):
        app = super(ApplicationForm, self).save(*args, **kwargs)

        if app.user is None:
            app.save()
            return app

        # update redundant information
        app.user.first_name = app.first_name
        app.user.last_name = app.last_name
        app.user.save()

        return app


class MentorApplicationForm(ApplicationForm):
    role = 'mentor'

    class Meta:
        model = MentorApplication
        fields = ('email',
                  'first_name',
                  'last_name',
                  'bio',
                  'gender',
                  'phone_number',
                  'current_occupation')


class MenteeApplicationForm(ApplicationForm):
    role = 'mentee'

    class Meta:
        model = MenteeApplication
        fields = ('email',
                  'first_name',
                  'last_name',
                  'bio',
                  'gender',
                  'phone_number',
                  'expectations')
>>>>>>> 6530ec01b4f0dd6191f3bf80c32cb89c860de185
