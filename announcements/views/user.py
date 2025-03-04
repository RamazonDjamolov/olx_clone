from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView
from announcements.models import Announcement


class AnnouncementCreateView(CreateView):
    model = Announcement
    redirect_url = '/announcements/'
    fields = '__all__'
    success_url = '/announcements/'
    template_name = 'announcement/create.html'

