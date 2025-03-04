from django.urls import path
from .views import AnnouncementCreateView, AnnouncementListView

app_name = "announcements"
urlpatterns = [
    path("create/", AnnouncementCreateView.as_view(), name="announcement-create" ),
    path("list/", AnnouncementListView.as_view(), name="announcement-list" ),


]
