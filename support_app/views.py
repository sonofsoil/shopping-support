from django.shortcuts import render
from django.shortcuts import redirect
from support_app.core.order_api import fetch_orders
from support_app.models import OrderQuery, OrderDetails
from support_app.forms import OrderQueryForm, OrderDetailsForm
from support_app.core.user_interaction import UserInteraction
from support_app.core.order_query_tools import SupportTools


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
                                           uquery=user_query,
                                           eanswer=query_in.expert_answer)
        if not query_in.expert_answer:
            query_in.expert_answer = user_interaction.get_answer()
            query_in.save()

        return render(request, "support_app/home.html",
            {"form": form, "interaction": user_interaction})

def orders(request):

    form = OrderDetailsForm(request.POST or None)
    query_in = OrderDetails.objects.last()

    if request.method == "POST":
        if form.is_valid():
            query_in = form.save(commit=False)
            query_in.save()
            return redirect("orders")
    else:
        user_id = None
        if query_in:
            user_id = query_in.user_id
        orders = fetch_orders(user_id=user_id)
        return render(request, "support_app/orders.html",
            {"form": form, "orders": orders})

def tools(request):
    tools = SupportTools().get_tool_list()
    return render(request, "support_app/tools.html",
            {"tools": tools})

def about(request):
    return render(request, "support_app/about.html")

def contact(request):
    return render(request, "support_app/contact.html")
