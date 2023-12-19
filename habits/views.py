from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse


from .models import Habit


def index(request):
    habit_list = Habit.objects.order_by('-pub_date')[:10]
    context = {'habit_list': habit_list, }
    return render(request, 'habits/index.html', context)


def get_latest_habit(request):
    latest_habit = Habit.objects.last()
    return render(request, 'habit_template.html', {'habit': latest_habit})


def detail(request, habit_id):
    habit = get_object_or_404(Habit, pk=habit_id)
    return render(request, 'habits/detail.html', {'habit': habit})


def complete(request, habit_id):
    habit = get_object_or_404(Habit, pk=habit_id)
    try:
        request.POST['complete']
    except KeyError:
        return render(request, 'habits/detail.html', {
            'habit': habit,
            'error_message': "You didn't select a habit."
        })
    else:
        habit.task_completed += 1
        habit.save()
        return HttpResponseRedirect(reverse('habits:index'))
