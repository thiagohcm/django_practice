from django.shortcuts import render

from .models import Telefone


def telefone_list(request):
    telefone_list_return = Telefone.objects.order_by('cliente_id')
    context = {'telefone_list_return': telefone_list_return}
    return render(request, 'lista.html', context)

