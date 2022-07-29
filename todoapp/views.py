from django.shortcuts import redirect, render
from django.views import View
from .form import ItemForm
from .models import TodoItem
from django.views.generic import TemplateView
from django.utils.timezone import now
# Create your views here.


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        items = TodoItem.objects.filter(cancelled=False)
        context['items'] = items
        return context

    def post(self, request, *args, **kwargs):
        item = self.request.POST.get('item_title')
        new_item = TodoItem(user=self.request.user, title=item)
        new_item.save()
        return redirect('/')


class ManageView(View):
    def get(self, request, **kwargs):
        pk = self.kwargs['pk']
        action = request.GET.get('action')
        c_obj = TodoItem.objects.get(id=pk)

        if action == 'cmp':
            if c_obj.completed == True:
                c_obj.completed = False
            else:
                c_obj.completed = True
                c_obj.date_completed = now()
            c_obj.save()
        elif action == 'rmv':
            c_obj.cancelled = True
            c_obj.date_cancelled = now()
            c_obj.save()
        else:
            pass
        return redirect('todo:index')
