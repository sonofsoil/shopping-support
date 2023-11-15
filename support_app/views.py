from django.shortcuts import render
from django.shortcuts import redirect
from support_app.core.order_api import fetch_orders
from support_app.models import OrderQuery, OrderDetails
from support_app.forms import OrderQueryForm, OrderDetailsForm
from support_app.core.user_interaction import UserInteraction
from support_app.core.tool_registry import SupportTools

"""
def home(request):

    form = OrderQueryForm(request.POST or None)    
    if request.method == "POST":
        if form.is_valid():
            query_in = form.save(commit=False)
            user_interaction = UserInteraction(user=query_in.user_id,
                                           uquery=query_in.user_query)
            #query_in.expert_answer = user_interaction.get_answer()
            query_in.save()
            #return redirect("home")
            return render(request, "support_app/home.html",
                {"form": form, "interaction": user_interaction})
    else:
        user_id = None
        user_query = None
        expert_answer = None
        query_in = OrderQuery.objects.last()
        if query_in:
            user_id = query_in.user_id
            user_query = query_in.user_query
            expert_answer=query_in.expert_answer
        user_interaction = UserInteraction(user=user_id,
                                           uquery=user_query,
                                           eanswer=expert_answer)
        return render(request, "support_app/home.html",
            {"form": form, "interaction": user_interaction})
"""

def home(request):
    form = OrderQueryForm(request.GET or None)    
    user_interaction = UserInteraction(user=None,
                                       uquery=None)
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
