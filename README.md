django-emailauth
================

A user model (with admin) using email as login handle for Django 1.5+

Basic usage
-----------

Read the official documentation on customizing authentication first:
https://docs.djangoproject.com/en/dev/topics/auth/customizing

settings.py::

    AUTH_USER_MODEL = 'django_emailauth.EmailUser'


Custom user model
-----------------

models.py::

    from django_emailauth.models import AbstractEmailUser

    class MyUser(AbstractEmailUser):
        """User model with a profile picture."""
        image = models.ImageField(_('profile picture'), upload_to='profiles')

forms.py::

    from django_emailauth.forms import EmailUserCreationForm, EmailUserChangeForm

    class UserCreationForm(EmailUserCreationForm):
        class Meta:
            model = MyUser


    class UserChangeForm(EmailUserChangeForm):
        class Meta:
            model = MyUser

admin.py::

    class UserAdmin(EmailUserAdmin):
        """Admin view with profile picture added in 'Personal info'."""
        fieldsets = (
            (None, {'fields': ('email', 'password',)}),
            (_('Personal info'), {'fields': ('first_name', 'last_name', 'image')}),
            (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                           'groups', 'user_permissions')}),
            (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
        )
        form = UserChangeForm
        add_form = UserCreationForm
