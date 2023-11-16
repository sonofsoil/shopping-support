from langchain.tools import StructuredTool
from support_app.core.order_tracker_expert import derive_days_to_deliver
from support_app.core.order_cancel_expert import decide_cancel_order
from support_app.core.order_identifier_expert import identify_relevant_order
from support_app.core.order_api import fetch_orders, cancel_order
from support_app.core.util_tools import (
    search_web,
    send_email,
    query_product_catalog,
    query_vector_db,
    text_to_sql,
)

class SupportTool() :
    tool : StructuredTool = None
    type : str = None
    typeImg : str = None
    domain : str = None
    domainImg : str = None
    trait : str = None
    traitImg : str = None

    def __init__(self, type : str,
                 typeImg : str,
                 domain: str,
                 domainImg: str,
                 trait : str,
                 traitImg : str,
                 tool : StructuredTool) -> None:
        self.type = type
        self.typeImg = typeImg
        self.domain = domain
        self.domainImg = domainImg
        self.trait = trait
        self.traitImg = traitImg
        self.tool = tool

class SupportTools() :
    tools : list[SupportTool]

    def __init__(self) -> None:
        self.tools = []
        self.tools.append(SupportTool(type='Retriever',
                                      typeImg='/static/support_app/retriever_icon.png',
                                      domain='Amazon',
                                      domainImg='/static/support_app/amazon_icon.png',
                                      trait='API',
                                      traitImg='/static/support_app/api_icon.svg',
                                      tool=StructuredTool.from_function(fetch_orders)))
        self.tools.append(SupportTool(type='Retriever',
                                      typeImg='/static/support_app/retriever_icon.png',
                                      domain='Amazon',
                                      domainImg='/static/support_app/amazon_icon.png',
                                      trait='Expert',
                                      traitImg='/static/support_app/expert_icon.png',
                                      tool=StructuredTool.from_function(identify_relevant_order)))
        self.tools.append(SupportTool(type='Retriever',
                                      typeImg='/static/support_app/retriever_icon.png',
                                      domain='AWS',
                                      domainImg='/static/support_app/aws_icon.svg',
                                      trait='Expert',
                                      traitImg='/static/support_app/expert_icon.png',
                                      tool=StructuredTool.from_function(text_to_sql)))
        self.tools.append(SupportTool(type='Retriever',
                                      typeImg='/static/support_app/retriever_icon.png',
                                      domain='Amazon',
                                      domainImg='/static/support_app/amazon_icon.png',
                                      trait='Expert',
                                      traitImg='/static/support_app/expert_icon.png',
                                      tool=StructuredTool.from_function(derive_days_to_deliver)))
        self.tools.append(SupportTool(type='Retriever',
                                      typeImg='/static/support_app/retriever_icon.png',
                                      domain='Amazon',
                                      domainImg='/static/support_app/amazon_icon.png',
                                      trait='Expert',
                                      traitImg='/static/support_app/expert_icon.png',
                                      tool=StructuredTool.from_function(decide_cancel_order)))
        self.tools.append(SupportTool(type='Action',
                                      typeImg='/static/support_app/action_icon.png',
                                      domain='Amazon',
                                      domainImg='/static/support_app/amazon_icon.png',
                                      trait='API',
                                      traitImg='/static/support_app/api_icon.svg',
                                      tool=StructuredTool.from_function(cancel_order)))
        self.tools.append(SupportTool(type='Retriever',
                                      typeImg='/static/support_app/retriever_icon.png',
                                      domain='External',
                                      domainImg='/static/support_app/external_icon.png',
                                      trait='API',
                                      traitImg='/static/support_app/api_icon.svg',
                                      tool=StructuredTool.from_function(search_web)))
        self.tools.append(SupportTool(type='Action',
                                      typeImg='/static/support_app/action_icon.png',
                                      domain='AWS',
                                      domainImg='/static/support_app/aws_icon.svg',
                                      trait='API',
                                      traitImg='/static/support_app/api_icon.svg',
                                      tool=StructuredTool.from_function(send_email)))
        self.tools.append(SupportTool(type='Retriever',
                                      typeImg='/static/support_app/retriever_icon.png',
                                      domain='Amazon',
                                      domainImg='/static/support_app/amazon_icon.png',
                                      trait='Expert',
                                      traitImg='/static/support_app/expert_icon.png',
                                      tool=StructuredTool.from_function(query_product_catalog)))
        self.tools.append(SupportTool(type='Retriever',
                                      typeImg='/static/support_app/retriever_icon.png',
                                      domain='AWS',
                                      domainImg='/static/support_app/aws_icon.svg',
                                      trait='API',
                                      traitImg='/static/support_app/api_icon.svg',
                                      tool=StructuredTool.from_function(query_vector_db)))

    def get_tools(self) -> list[SupportTool] :
        return [t.tool for t in self.tools]
    
    def get_tool_list(self) -> list[any] :
        tl = []
        for tool in self.tools :
            tl.append({
                'type' : tool.type,
                'typeImg': tool.typeImg,
                'domain': tool.domain,
                'domainImg': tool.domainImg,
                'trait': tool.trait,
                'traitImg': tool.traitImg,
                'name': tool.tool.name,
                'description': tool.tool.description
            })
        return tl
