from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^input$', views.input),
    url(r'^destroy/(?P<id>\d+)$', views.destroy),
    url(r'^delete$', views.delete)

]
