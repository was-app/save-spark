from django.shortcuts import render, redirect

def home(request):
    if not request.user.is_authenticated:
        return redirect('login')

    if request.method == 'POST':
        if 'recurrent_button' in request.POST:
            return redirect('recurrent_transaction')
        elif 'extra_button' in request.POST:
            return redirect('extra_transaction')

    return render(request, 'home/home.html')
