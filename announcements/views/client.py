from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView, ListView
from announcements.models import Announcement, StatusChoices


#
#
class AnnouncementCreateView(PermissionRequiredMixin, CreateView):
    model = Announcement
    fields = ['title', 'description', 'price', 'phone', 'city']
    template_name = 'announcement/create.html'
    success_url = reverse_lazy('announcements:announcement-list')
    permission_required = "announcements.add_announcement"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class AnnouncementListView(PermissionRequiredMixin,ListView):
    model = Announcement
    template_name = 'announcement/list.html'
    context_object_name = 'announcements'
    queryset = Announcement.objects.filter(status=StatusChoices.IN_REVIEW)
    permission_required = "announcements.view_announcement"

    def get_queryset(self):
        return Announcement.objects.filter(user=self.request.user) or Announcement.objects.filter(is_active=False)
