from django.urls import path
from .views import AnnouncementCreateView, AnnouncementListView
from .views.moderator import ListModerateView, AnnouncementsUpdateView  # To‘g‘ri nom ishlatilsin

app_name = "announcements"
urlpatterns = [
    path("create/", AnnouncementCreateView.as_view(), name="announcement-create"),
    path("list/", AnnouncementListView.as_view(), name="announcement-list"),
    path("list_moderate/", ListModerateView.as_view(), name="moderate-list"),
    path("moderate/<int:pk>/", AnnouncementsUpdateView.as_view(), name="moderate-update"),

]
