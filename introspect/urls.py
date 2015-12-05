from django.conf.urls import patterns, url

from .views import IntrospectionView

urlpatterns = patterns('',
                       url(
                           r'^$',
                           IntrospectionView.as_view()
                       ),
                       )


