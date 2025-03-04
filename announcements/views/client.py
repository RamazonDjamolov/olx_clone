from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView, ListView
from announcements.models import Announcement


#
#
class AnnouncementCreateView(CreateView):
    model = Announcement
    fields = ['title', 'description', 'price', 'phone', 'city']
    template_name = 'announcement/create.html'
    success_url = reverse_lazy('announcements:announcement-list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class AnnouncementListView(ListView):
    model = Announcement
    template_name = 'announcement/list.html'
    context_object_name = 'announcements'

    def get_queryset(self):
        return Announcement.objects.filter(user=self.request.user) or Announcement.objects.filter(is_active=False)
