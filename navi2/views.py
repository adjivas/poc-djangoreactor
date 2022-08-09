from django.shortcuts import render
from reactor.component import Component


class XCounter(Component):
    _template_name = 'x-counter.html'

    amount: int = 0

    def recv_inc(self):
        self.amount += 1

    def recv_dec(self):
        self.amount -= 1

    def recv_set_to(self, amount: int):
        self.amount = amount


def counter(request):
    return render(request, 'counter.html', context={"title": "index"})
