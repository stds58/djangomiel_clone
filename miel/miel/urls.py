"""
URL configuration for miel project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.conf import settings
# from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

# from users.views import TestApiView
# from users.views import CreateAdminUserView
from users.views import CreateAdminUserViewset
from showcase.views import CardTestApiView, UserShowcaseRedirectView, CandidateCardViewset

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'cards', CandidateCardViewset, basename='cards')
router.register(r'admin_create', CreateAdminUserViewset, basename='admin_create')

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('auth/', include('djoser.urls.jwt')),
    path('auth/', include('djoser.urls')),
    # path('admin_create/', CreateAdminUserView.as_view(), name='admin_create'),
    # path('test/', TestApiView.as_view(), name='test_api'),
    path('test_cards/', CardTestApiView.as_view(), name='card_test_api'),
    path('showcase/', UserShowcaseRedirectView.as_view(), name='showcase_user_redirect')
]
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
