from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from .views import \
    CurrentUserAPIView, \
    KristianaLisitraAPIView, \
    KristianaAPIView, \
    KristianaByKodyAPIView, \
    TossaafiAPIView, \
    TossaafiLisitraAPIView, \
    KitapoAPIView, \
    KitapoLisitraAPIView, \
    KitapoByKristianaAPIView, \
    KitapoLastAPIView, \
    AdidyAPIView, \
    AdidyLisitraAPIView, \
    AdidyByKristianaAPIView, \
    AdidyLastAPIView, \
    LaminasaAPIView, \
    LaminasaLisitraAPIView, \
    LaminasaAfterDayAPIView, \
    MpikambanaAPIView, \
    MpikambanaLisitraAPIView, \
    MpikambanaByKristianaAPIView, \
    KitapoLastByRosiaAPIView, \
    AdidyLastByRosiaAPIView, \
    KitapoHamarininaAPIView, \
    KitapoByDatyAnioAPIView, \
    AdidyHamarininaAPIView, \
    AdidyByDatyAnioAPIView, \
    SondageAPIView, \
    SondageLisitraAPIView

urlpatterns = [
    url(r'^currentUser/$', CurrentUserAPIView.as_view(), name='current_user'),
    url(r'^kristiana/$', KristianaLisitraAPIView.as_view(), name='Kristiana_list'),
    url(r'^kristiana/(?P<pk>\d+)$', KristianaAPIView.as_view(), name='kristiana'),
    url(r'^kristianaByKody/(?P<pk>.+)$', KristianaByKodyAPIView.as_view(), name='kristiana_by_kody'),
    url(r'^tossaafi/$', TossaafiLisitraAPIView.as_view(), name='tossaafi_list'),
    url(r'^tossaafi/(?P<pk>\d+)$', TossaafiAPIView.as_view(), name='tossaafi'),
    url(r'^mpikambana/$', MpikambanaLisitraAPIView.as_view(), name='mpiakambana_list'),
    url(r'^mpikambana/(?P<pk>\d+)$', MpikambanaAPIView.as_view(), name='kristiana'),
    url(r'^mpikambanaByKristiana/(?P<kristiana>.+)/$', MpikambanaByKristianaAPIView.as_view(),
        name='mpikambana_by_kristiana'),
    url(r'^kitapo/$', KitapoLisitraAPIView.as_view(), name='kitapo_list'),
    url(r'^kitapo/(?P<pk>\d+)$', KitapoAPIView.as_view(), name='kitapo'),
    url(r'^kitapoByKristiana/(?P<kristiana>.+)/$', KitapoByKristianaAPIView.as_view(), name='kitapo_by_kristiana'),
    url(r'^kitapoLast/(?P<kristiana>.+)/(?P<rosia>.+)/$', KitapoLastAPIView.as_view(), name='kitapo_last'),
    url(r'^kitapoLastByRosia/$', KitapoLastByRosiaAPIView.as_view(), name='kitapo_last_rosia'),
    url(r'^kitapoHamarinina/$', KitapoHamarininaAPIView.as_view(), name='kitapo_hamarinina'),
    url(r'^kitapoByDatyAnio/$', KitapoByDatyAnioAPIView.as_view(), name='kitapo_by_datyAnio'),
    url(r'^adidy/$', AdidyLisitraAPIView.as_view(), name='adidy_list'),
    url(r'^adidy/(?P<pk>\d+)$', AdidyAPIView.as_view(), name='adidy'),
    url(r'^adidyByKristiana/(?P<kristiana>.+)/$', AdidyByKristianaAPIView.as_view(), name='adidy_by_kristiana'),
    url(r'^adidyLast/(?P<kristiana>.+)/(?P<rosia>.+)/$', AdidyLastAPIView.as_view(), name='adidy_last'),
    url(r'^adidyLastByRosia/$', AdidyLastByRosiaAPIView.as_view(), name='adidy_last_rosia'),
    url(r'^adidyHamarinina/$', AdidyHamarininaAPIView.as_view(), name='adidy_hamarinina'),
    url(r'^adidyByDatyAnio/$', AdidyByDatyAnioAPIView.as_view(), name='adidy_by_datyAnio'),
    url(r'^laminasa/$', LaminasaLisitraAPIView.as_view(), name='laminasa_list'),
    url(r'^laminasa/(?P<pk>\d+)$', LaminasaAPIView.as_view(), name='laminasa'),
    url(r'^laminasaAfterDay/$', LaminasaAfterDayAPIView.as_view(), name='laminasa_after_day'),
    url(r'^sondage/$', SondageLisitraAPIView.as_view(), name='sondage_list'),
    url(r'^sondage/(?P<pk>\d+)$', SondageAPIView.as_view(), name='sondage'),
]
