





from django.contrib import admin
from django.urls import path,include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('task/', include('task.urls')),
    path('', RedirectView.as_view(url='task/', permanent=False)),
]