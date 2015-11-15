from django.views.generic import DeleteView
from .models import Entry


class EntryDetail(DeleteView):
    model=Entry