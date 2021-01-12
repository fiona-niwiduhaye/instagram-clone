from django.conf.urls import url,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^signup/', views.signup, name='signup'),
    url(r'^account/', include('django.contrib.auth.urls')),
    url(r'^$', views.index, name='index'),
    url(r'^profile/(\d+)', views.profile, name='profile'),
    url(r'^user_profile/(\d+)', views.user_profile, name='user_profile'),
    url(r'post/<id>', views.post_comment, name='comment'),
    url(r'^like/$', views.like_post, name='like_post'),
    url(r'^search/', views.search_profile, name='search'),
    url(r'^unfollow/<to_unfollow>', views.unfollow, name='unfollow'),
    url(r'^follow/<to_follow>', views.follow, name='follow')
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)