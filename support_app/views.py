from django.shortcuts import render
from django.shortcuts import redirect
from support_app.models import OrderQuery
from support_app.forms import OrderQueryForm
from support_app.core.user_interaction import UserInteraction


def home(request):

    form = OrderQueryForm(request.POST or None)
    query_in = OrderQuery.objects.last()

    if request.method == "POST":
        if form.is_valid():
            query_in = form.save(commit=False)
            query_in.save()
            return redirect("home")
    else:
        user_id = None
        user_query = None
        if query_in:
            user_id = query_in.user_id
            user_query = query_in.user_query
        user_interaction = UserInteraction(user=user_id,
                                           uquery=user_query)
        user_interaction.get_answer()
        return render(request, "support_app/home.html",
            {"form": form, "interaction": user_interaction})

def about(request):
    return render(request, "support_app/about.html")

def contact(request):
    return render(request, "support_app/contact.html")
