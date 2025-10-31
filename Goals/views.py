from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from Persistence.services.goal_service import GoalService
from .forms import GoalForm

def add_goals(request):
    if not request.user.is_authenticated:
        return redirect('login')

    if request.method == 'POST':
        form = GoalForm(request.POST)
        if form.is_valid():
            goal = form.cleaned_data
            tmp = GoalService()
            tmp.create_goal(client=request.user, name=goal['name'], target_amount=goal['target_amount'], target_date=goal['target_date'], description=goal['description'])
            return redirect('home:dashboard')
        else:
            return HttpResponse(form.errors)
    else:
        form = GoalForm()
        
    return render(request, 'goals/add_goals.html', {'form': form})

# def goals_view(request):
#     goal_service = GoalService()
#     user = request.user

#     if request.method == 'POST':
#         form = GoalForm(request.POST)
#         action = request.POST.get('action')

#         if action == 'create' and form.is_valid():
#             goal_data = form.cleaned_data
#             goal_service.create_goal(
#                 client=user,
#                 name=goal_data['name'],
#                 target_amount=goal_data['target_amount'],
#                 target_date=goal_data['target_date'],
#                 description=goal_data.get('description', '')
#             )
#             return redirect('goals:goals_view')

#         elif action == 'delete':
#             goal_id = request.POST.get('goal_id')
#             goal_to_delete = goal_service.repo.get(id=goal_id, client=user)
#             if goal_to_delete:
#                 goal_service.delete_goal(goal_to_delete)
#             return redirect('goals:goals_view')

#     goals = goal_service.get_goals_by_user(user)
#     form = GoalForm()
#     context = {
#         'goals': goals,
#         'form': form
#     }
#     return render(request, 'goals/goals.html', context)

