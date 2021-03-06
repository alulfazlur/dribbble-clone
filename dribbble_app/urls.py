from django.urls import path
from . import views
from .views import SearchResultsView
from django.conf import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'dribbble_app'
urlpatterns = [
    path('', views.index, name='index'),
    path('form-publish/', views.formPublish, name='form-publish'),
    path('profile/', views.profile, name='profile'),
    path('user/', views.user, name='user'),
    # path('picture-detail<int:userdesign_id>/', views.PictureDetail, name='picture-detail'),
    # path('picture-detail/', views.PictureDetail, name='picture-detail'),
    path('search/', SearchResultsView.as_view(), name='search_results'),
    path('<int:id>/', views.detail, name='detail'),
    path('like/<int:id>/', views.designLike),
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)