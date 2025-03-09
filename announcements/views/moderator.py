from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView, ListView
from announcements.models import Announcement, StatusChoices


# @permission_required('announcements.view_announcement')
class ListModerateView(PermissionRequiredMixin, ListView):
    model = Announcement
    context_object_name = 'announcements'
    template_name = 'announcement/moderate/list.html'
    queryset = Announcement.objects.filter(status=StatusChoices.IN_REVIEW)
    permission_required = "announcements.view_announcement"

class AnnouncementsUpdateView(PermissionRequiredMixin,UpdateView):
    model = Announcement
    template_name = 'announcement/moderate/update.html'
    fields = ['status']
    success_url = reverse_lazy('announcements:moderate-list')
    pk_url_kwarg = 'pk'
    permission_required = "announcements.moderate_announcement "



