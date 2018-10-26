import logging
import pprint

from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import login
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate

# from .forms import UserRegistrationForm
from users.models import UserProfile

logger = logging.getLogger('django.' + __name__)

class UserRegistrationView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'

    # def _partially_filled_form(self, request, form, model_errors=None):
    #     """Display registration form with valid fields pre-filled."""
    #     return render(request, self.template_name, {
    #             'form': form,
    #             'model_errors': model_errors,
    #         })

    # def get(self, request):
    #     """Display blank registration form."""
    #     form = self.form_class(data=None)
    #     return render(request, self.template_name, {'form': form})

    # def post(self, request):
    #     """Process form data and register the user."""

    #     logger.info("Processing registration:\n{:}".format(pprint.pformat(request.__dict__['_post'])))

    #     form = self.form_class(data=request.POST)
    #     if not form.is_valid():
    #         logger.warning("Invalid form: {:}".format(form))
    #         return self._partially_filled_form(request, form)

    #     user = form.save()

    #     # TODO: SHOULD PROBABLY NOT BE READING RAW PASSWORD AND SETTING THEM LIKE THIS.
    #     # But this should work for now to avoid "Invalid password format or unknown
    #     # hashing algorithm."
    #     user.set_password(request.__dict__['_post']['password'])

    #     profile = UserProfile(user=user, display_name=user.username)
    #     try:
    #         user.full_clean()
    #         profile.full_clean()
    #     except ValidationError as e:
    #         return self._partially_filled_form(request, form, model_errors=e.message_dict)

    #     user.save()
    #     profile.save()
    #     login(request, user)
    #     return redirect(to='home')
