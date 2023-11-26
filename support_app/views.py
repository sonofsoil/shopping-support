from django.shortcuts import render
from support_app.core.order_api import fetch_orders
from support_app.core.tool_registry import SupportTools

def demo(request):
   return render(request, "support_app/demo.html")

def orders(request):
    orders = fetch_orders()
    return render(request, "support_app/orders.html", {"orders": orders})

def tools(request):
    tools = SupportTools().get_tool_list()
    return render(request, "support_app/tools.html", {"tools": tools})

def home(request):
    return render(request, "support_app/home.html")
