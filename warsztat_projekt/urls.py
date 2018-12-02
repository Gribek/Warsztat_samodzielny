"""warsztat_projekt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from contact_box.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', show_all_contacts),
    url(r'^new$', NewPerson.as_view()),
    url(r'^modify/(?P<id>\d+)$', EditPerson.as_view()),
    url(r'^delete/(?P<id>\d+)$', DeletePerson.as_view()),
    url(r'^show/(?P<id>\d+)$', show_person),
    url(r'^showGroup/(?P<group_id>\d+)$', show_group),
    url(r'^(?P<id>\d+)/addAddress$', AddAddress.as_view()),
    url(r'^(?P<id>\d+)/addPhone$', AddPhoneNumber.as_view()),
    url(r'^(?P<id>\d+)/addEmail$', AddEmail.as_view()),
    url(r'^deletePhone/(?P<id>\d+)$', DeletePhone.as_view()),
    url(r'^deleteEmail/(?P<id>\d+)$', DeleteEmail.as_view()),
    url(r'^addGroup$', AddGroup.as_view()),
    url(r'^AddGroupMember/(?P<group_id>\d+)$', AddGroupMember.as_view()),
    url(r'^showGroup/group_search/(?P<group_id>\d+)$', GroupSearch.as_view()),

]
