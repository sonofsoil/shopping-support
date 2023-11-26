from langchain.tools import StructuredTool
from support_app.core.order_tracker_expert import derive_days_to_deliver
from support_app.core.order_cancel_expert import decide_cancel_order
from support_app.core.order_identifier_expert import identify_relevant_order
from support_app.core.order_api import fetch_orders, cancel_order
from support_app.core.util_tools import (
    search_web,
    send_email,
    query_product_catalog,
    query_similar_entities,
    text_to_sql,
    order_support_agent,
)

class SupportTool() :
    tool : StructuredTool = None
    type : str = None
    typeImg : str = None
    domain : str = None
    domainImg : str = None
    trait : str = None
    traitImg : str = None
    owner : str = None
    llm : str = None
    tools_used : list[StructuredTool] = None

    def __init__(self, type : str,
                 typeImg : str,
                 domain: str,
                 owner: str,
                 domainImg: str,
                 trait : str,
                 traitImg : str,
                 tool : StructuredTool,
                 llm : str = None,
                 tools_used : list[StructuredTool] = []) -> None:
        self.type = type
        self.typeImg = typeImg
        self.domain = domain
        self.owner = owner
        self.domainImg = domainImg
        self.trait = trait
        self.traitImg = traitImg
        self.tool = tool
        self.tools_used = tools_used
        self.llm = llm

class SupportTools() :
    tools : list[SupportTool]

    def __init__(self) -> None:
        self.tools = []
        fetch_orders_tool = StructuredTool.from_function(fetch_orders)
        self.tools.append(SupportTool(type='Answer',
                                      typeImg='/static/support_app/answer_icon.png',
                                      domain='Amazon',
                                      domainImg='/static/support_app/amazon_icon.png',
                                      owner='Ordering',
                                      trait='API',
                                      traitImg='/static/support_app/api_icon.png',
                                      tool=fetch_orders_tool))
        identify_relevant_order_tool = StructuredTool.from_function(identify_relevant_order)
        self.tools.append(SupportTool(type='Answer',
                                      typeImg='/static/support_app/answer_icon.png',
                                      domain='Amazon',
                                      domainImg='/static/support_app/amazon_icon.png',
                                      owner='AI Builder',
                                      trait='NLI',
                                      llm='Claude-2',
                                      traitImg='/static/support_app/nli_icon.png',
                                      tool=identify_relevant_order_tool))
        text_to_sql_tool = StructuredTool.from_function(text_to_sql)
        self.tools.append(SupportTool(type='Answer',
                                      typeImg='/static/support_app/answer_icon.png',
                                      domain='AWS',
                                      domainImg='/static/support_app/aws_icon.svg',
                                      owner='ExpertQ',
                                      trait='NLI',
                                      llm='Unpublished',
                                      traitImg='/static/support_app/nli_icon.png',
                                      tool=text_to_sql_tool))
        derive_days_to_deliver_tool = StructuredTool.from_function(derive_days_to_deliver)
        self.tools.append(SupportTool(type='Answer',
                                      typeImg='/static/support_app/answer_icon.png',
                                      domain='Amazon',
                                      domainImg='/static/support_app/amazon_icon.png',
                                      owner='AI Builder',
                                      trait='NLI',
                                      llm='GPT-3.5 Turbo',
                                      traitImg='/static/support_app/nli_icon.png',
                                      tool=derive_days_to_deliver_tool))
        decide_cancel_order_tool = StructuredTool.from_function(decide_cancel_order)
        self.tools.append(SupportTool(type='Answer',
                                      typeImg='/static/support_app/answer_icon.png',
                                      domain='Amazon',
                                      domainImg='/static/support_app/amazon_icon.png',
                                      owner='AI Builder',
                                      trait='NLI',
                                      llm='Llama-2 7B',
                                      traitImg='/static/support_app/nli_icon.png',
                                      tool=decide_cancel_order_tool))
        cancel_order_tool = StructuredTool.from_function(cancel_order)
        self.tools.append(SupportTool(type='Action',
                                      typeImg='/static/support_app/action_icon.png',
                                      domain='Amazon',
                                      domainImg='/static/support_app/amazon_icon.png',
                                      owner='Ordering',
                                      trait='API',
                                      traitImg='/static/support_app/api_icon.png',
                                      tool=cancel_order_tool))
        search_web_tool = StructuredTool.from_function(search_web)
        self.tools.append(SupportTool(type='Answer',
                                      typeImg='/static/support_app/answer_icon.png',
                                      domain='External',
                                      domainImg='/static/support_app/external_icon.png',
                                      owner='AI Builder',
                                      trait='API',
                                      traitImg='/static/support_app/api_icon.png',
                                      tool=search_web_tool))
        send_email_tool = StructuredTool.from_function(send_email)
        self.tools.append(SupportTool(type='Action',
                                      typeImg='/static/support_app/action_icon.png',
                                      domain='AWS',
                                      domainImg='/static/support_app/aws_icon.svg',
                                      owner='SimpleEmailService',
                                      trait='API',
                                      traitImg='/static/support_app/api_icon.png',
                                      tool=send_email_tool))
        query_product_catalog_tool = StructuredTool.from_function(query_product_catalog)
        self.tools.append(SupportTool(type='Answer',
                                      typeImg='/static/support_app/answer_icon.png',
                                      domain='Amazon',
                                      domainImg='/static/support_app/amazon_icon.png',
                                      owner='Catalog Platform',
                                      trait='NLI',
                                      llm='Flan-T5 XXL',
                                      traitImg='/static/support_app/nli_icon.png',
                                      tool=query_product_catalog_tool))
        query_similar_entities_tool = StructuredTool.from_function(query_similar_entities)
        self.tools.append(SupportTool(type='Answer',
                                      typeImg='/static/support_app/answer_icon.png',
                                      domain='Amazon',
                                      domainImg='/static/support_app/amazon_icon.png',
                                      owner='AI Builder',
                                      trait='API',
                                      traitImg='/static/support_app/api_icon.png',
                                      tool=query_similar_entities_tool))
        order_support_agent_tool = StructuredTool.from_function(order_support_agent)
        self.tools.append(SupportTool(type='Composite',
                                      typeImg='/static/support_app/composite_icon.png',
                                      domain='Amazon',
                                      domainImg='/static/support_app/amazon_icon.png',
                                      owner='Ordering',
                                      trait='NLI',
                                      traitImg='/static/support_app/nli_icon.png',
                                      llm='GPT-4',
                                      tool=order_support_agent_tool,
                                      tools_used=[fetch_orders_tool,
                                                  identify_relevant_order_tool,
                                                  derive_days_to_deliver_tool,
                                                  decide_cancel_order_tool,
                                                  cancel_order_tool]))
                                      

    def get_tools(self) -> list[SupportTool] :
        return [t.tool for t in self.tools]
    
    def get_tool_list(self) -> list[any] :
        tl = []
        for tool in self.tools :
            startD = tool.tool.description.find(' - ') + 3
            endD = tool.tool.description.find(':param')
            tl.append({
                'type' : tool.type,
                'typeImg': tool.typeImg,
                'domain': tool.domain,
                'domainImg': tool.domainImg,
                'trait': tool.trait,
                'traitImg': tool.traitImg,
                'name': tool.tool.name,
                'description': tool.tool.description[startD:endD].strip(),
                'owner': tool.owner,
                'llm': tool.llm,
                'tools': [t.name for t in tool.tools_used],
            })
        return tl
