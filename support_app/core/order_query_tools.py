from langchain.tools import StructuredTool
from support_app.core.order_tracker_expert import derive_days_to_deliver
from support_app.core.order_cancel_expert import decide_cancel_order
from support_app.core.order_identifier_expert import identify_relevant_order
from support_app.core.order_api import fetch_orders, cancel_order

class SupportTool() :
    tool : StructuredTool = None
    type : str = 'Any'

    def __init__(self, type : str, tool : StructuredTool) -> None:
        self.type = type
        self.tool = tool

class SupportTools() :
    tools : list[SupportTool]

    def __init__(self) -> None:
        self.tools = []
        self.tools.append(SupportTool(type='API', tool=StructuredTool.from_function(fetch_orders)))
        self.tools.append(SupportTool(type='Expert', tool=StructuredTool.from_function(identify_relevant_order)))
        self.tools.append(SupportTool(type='Expert', tool=StructuredTool.from_function(derive_days_to_deliver)))
        self.tools.append(SupportTool(type='Expert', tool=StructuredTool.from_function(decide_cancel_order)))
        self.tools.append(SupportTool(type='API', tool=StructuredTool.from_function(cancel_order)))

    def get_tools(self) -> list[SupportTool] :
        return [t.tool for t in self.tools]
    
    def get_tool_list(self) -> list[any] :
        tl = []
        for tool in self.tools :
            tl.append({
                'type' : tool.type,
                'name': tool.tool.name,
                'description': tool.tool.description
            })
        return tl
