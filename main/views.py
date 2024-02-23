from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.utils.http import urlencode
from django.views.generic import ListView, DetailView

from main.models import Menu, Item


class MenuListView(ListView):
    model = Menu


class MenuDetailView(DetailView):
    model = Menu

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)

        item = request.GET.get('item')
        context['item_selected'] = item

        return self.render_to_response(context)


def get_item(request, pk):
    item = get_object_or_404(Item, pk=pk)

    params = {
        'item': item.pk
    }

    return redirect(
        f"{reverse('main:menu-detail', kwargs={'pk': item.menu.pk})}?{urlencode(params)}"
    )
