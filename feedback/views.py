from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from feedback.models import Feedback


@login_required(login_url='login')
def feedback(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        Feedback_text = request.POST.get("Feedback_text")
        print(Feedback_text)
        query = Feedback(name=name, email=email, Feedback_text=Feedback_text)
        query.save()
        return redirect("/feedback")
    # query = Feedback.objects.all()[-3]
    return render(request, "feedback.html")
# ,context={'feedback_query':query}