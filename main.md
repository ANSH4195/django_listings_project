# For the templates folder to work, goto:
(main)settings.py -> TEMPLATES -> add:

  "'DIRS': [os.path.join(BASE_DIR, 'templates')],"

<!-- ================================================================= -->

# Connecting postgres:
pip install psycopg2 & psycopg2-binary
(main)settings.py -> add:

  DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'btredb',
        'USER': 'postgres',
        'PASSWORD': '1234',
        'HOST': 'localhost'
    }
  }

<!-- ================================================================= -->

# Making migrations to register tables & stuff in database:
python manage.py migrate

You will see tables in pgadmin browser window under:
databases -> btredb -> schemas -> public -> tables

<!-- ================================================================= -->

# Creating models:
  # We create a class with the SINGULAR VERSION OF THE APP NAME.
  If the app name is Listings -> class Listing().


  # The id is AUTOMATICALLY handled by postgresql


  # Also, when using foreign keys pass the NAME OF CLASS OF FOREIGN KEY.
  Ex: You want realtors as the foreignkey,
  do: models.ForeignKey(Realtor, on_delete=something)

  Don't forget to import it:
  from realtors.models import Realtor


  # Set the main field you want to display in the admin
  def __str__(self):
    return self.title


  # Make migrations:
    python manage.py makemigrations ->
    python manage.py migrate

<!-- ================================================================= -->

# Register the models in the respective admin.py:
  Import the model and add:
  admin.site.register(Listing)

<!-- ================================================================= -->

# Media folder to contain all the images uploaded:
  Goto btre -> settings.py -> goto to the end and add:


  # Media Folder
  MEDIA_ROOT = os.path.join(BASE_FIR, 'media')
  MEDIA_URL = '/media/'


  # To show them correctly:
  Goto btre -> urls.py -> add:

  from djano.conf import settings
  from django.conf.urls.static import static

  urlpatterns = [
      ...
  ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

<!-- ================================================================= -->

# Customising ADMIN panel:
  Create a folder named admin in templates.
  Create a file named base_site.html (V. V. IMP)

  Import {% extends 'admin/base.html' %}

  Rest see in the file itself

<!-- ================================================================= -->

# Customising tables in admin:
  goto listings -> admin.py

  create a class named ListingAdmin:

  class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published', 'price', 'list_date', 'realtor')

  admin.site.register(Listing, ListingAdmin)

  list_display are the fields that you want to show.

  see the rest there only.

<!-- ================================================================= -->

# FOR AUTH LOGIN AND REGISTER:
  Remember to put method="POST" in the form actions

<!-- ================================================================= -->

# MESSAGES/ALERTS APP:
  Add to btre -> settings.py:
    # Messages
    from django.contrib.messages import constants as messages
    MESSAGE_TAGS = {
        messages.ERROR: 'danger',
    }

  Also, check templates -> partials -> _alerts.html

  Put:
  <!-- Alerts -->
  {% include 'partials/_alerts.html' %}

  where in the template you want to use the messages.

<!-- ================================================================= -->

# LOGIN AND REGISTER SHTUFF:
  accounts -> views.py