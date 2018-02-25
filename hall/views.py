# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from .models import *

# Create your views here.
def reserve(request):
    theatre = Theatre.objects.get(name=request.POST.get('theatre'))
    auditorium = theatre.auditoriums.get(name=request.POST.get('auditorium'))
    seat = auditorium.seats.select_for_update().get(row=request.POST.get('row'), position=request.POST.get('position'))
    if not seat.booked:
        seat.booked = True
        seat.save()
        msg = 'seat booked'
    else:
        msg = 'sorry the seat is already booked'
    return render(request, 'reserve.html', {'msg': msg})
