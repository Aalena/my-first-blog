from django.conf.urls import url
from . import views
#This regular expression will match ^ (a beginning) followed by $ (an end) – so only an empty string will match. That's correct, because in Django URL resolvers, 'http://127.0.0.1:8000/' is not a part of the URL. This pattern will tell Django that views.post_list is the right place to go if someone enters your website at the 'http://127.0.0.1:8000/' address.
urlpatterns = [
    url(r'^$',views.post_list,name='post_list'),
    url(r'^post/(?P<pk>\d+)/$',views.post_detail,name='post_detail'),
    #(?P<pk>\d+) – It means that Django will take everything that you place here and transfer it to a view as a variable called pk.
    url(r'^post/new/$',views.post_new,name='post_new'),
    url(r'^post/edit/(?P<pk>\d+)/$',views.post_edit,name='post_edit'),
]