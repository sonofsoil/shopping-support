from langchain.tools import StructuredTool
from support_app.core.order_tracker_expert import derive_days_to_deliver
from support_app.core.order_cancel_expert import decide_cancel_order
from support_app.core.order_identifier_expert import identify_relevant_order
from support_app.core.order_api import fetch_orders, cancel_order
from support_app.core.util_tools import (
    search_web,
    send_email,
    product_support_agent,
    query_similar_entities,
    text_to_sql,
    order_support_agent,
    search_products,
    fetch_product_details,
    buyer_support_agent,
    buy_one_click,
    query_support_sops,
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
    rtt : str = None
    impls : list[str] = None

    def __init__(self, type : str,
                 typeImg : str,
                 domain: str,
                 owner: str,
                 domainImg: str,
                 trait : str,
                 traitImg : str,
                 rtt : str,
                 tool : StructuredTool,
                 llm : str = None,
                 tools_used : list[StructuredTool] = [],
                 impls : list[str] = []) -> None:
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
        self.rtt = rtt
        self.impls = impls

class SupportTools() :
    tools : list[SupportTool]

    def __init__(self) -> None:
        self.tools = []
        fetch_orders_tool = StructuredTool.from_function(fetch_orders)
        identify_relevant_order_tool = StructuredTool.from_function(identify_relevant_order)
        text_to_sql_tool = StructuredTool.from_function(text_to_sql)
        derive_days_to_deliver_tool = StructuredTool.from_function(derive_days_to_deliver)
        decide_cancel_order_tool = StructuredTool.from_function(decide_cancel_order)
        cancel_order_tool = StructuredTool.from_function(cancel_order)
        search_web_tool = StructuredTool.from_function(search_web)
        send_email_tool = StructuredTool.from_function(send_email)
        product_support_agent_tool = StructuredTool.from_function( product_support_agent)
        order_support_agent_tool = StructuredTool.from_function(order_support_agent)
        query_support_sops_tool = StructuredTool.from_function(query_support_sops)
        query_similar_entities_tool = StructuredTool.from_function(query_similar_entities)
        search_products_tool = StructuredTool.from_function(search_products)
        fetch_product_details_tool = StructuredTool.from_function(fetch_product_details)
        buyer_support_agent_tool = StructuredTool.from_function(buyer_support_agent)
        buy_one_click_tool = StructuredTool.from_function(buy_one_click)
        
        self.tools.append(SupportTool(type='Answer Tool',
                                      typeImg='/static/support_app/answer_icon.png',
                                      domain='Amazon Retail',
                                      domainImg='/static/support_app/amazon_icon.png',
                                      owner='Ordering',
                                      trait='Application Programming Interface(API)',
                                      traitImg='/static/support_app/api_icon.png',
                                      rtt='p99 100 ms',
                                      tool=fetch_orders_tool,
                                      impls=['Python SDK']))
        self.tools.append(SupportTool(type='Answer Tool',
                                      typeImg='/static/support_app/answer_icon.png',
                                      domain='Amazon Retail',
                                      domainImg='/static/support_app/amazon_icon.png',
                                      owner='AI Builder',
                                      trait='Natural Language Interface(NLI)',
                                      llm='Flan-T5 XXL',
                                      rtt='1 - 3 sec',
                                      traitImg='/static/support_app/nli_icon.png',
                                      tool=identify_relevant_order_tool,
                                      impls=['LangChain']))
        self.tools.append(SupportTool(type='Answer Tool',
                                      typeImg='/static/support_app/answer_icon.png',
                                      domain='Amazon Web Service',
                                      domainImg='/static/support_app/aws_icon.png',
                                      owner='Redshift Spectrum',
                                      trait='Natural Language Interface(NLI)',
                                      llm='Unpublished',
                                      rtt='1 - 5 sec',
                                      traitImg='/static/support_app/nli_icon.png',
                                      tool=text_to_sql_tool,
                                      impls=['Amazon Q']))
        self.tools.append(SupportTool(type='Answer Tool',
                                      typeImg='/static/support_app/answer_icon.png',
                                      domain='Amazon Retail',
                                      domainImg='/static/support_app/amazon_icon.png',
                                      owner='AI Builder',
                                      trait='Natural Language Interface(NLI)',
                                      llm='GPT-3.5 Turbo',
                                      rtt='1 - 2 sec',
                                      traitImg='/static/support_app/nli_icon.png',
                                      tool=derive_days_to_deliver_tool,
                                      impls=['LangChain', 'Bedrock']))
        self.tools.append(SupportTool(type='Answer Tool',
                                      typeImg='/static/support_app/answer_icon.png',
                                      domain='Amazon Retail',
                                      domainImg='/static/support_app/amazon_icon.png',
                                      owner='AI Builder',
                                      trait='Natural Language Interface(NLI)',
                                      llm='Llama-2 7B',
                                      rtt='< 1 sec',
                                      traitImg='/static/support_app/nli_icon.png',
                                      tool=decide_cancel_order_tool,
                                      impls=['LangChain']))
        self.tools.append(SupportTool(type='Action Tool',
                                      typeImg='/static/support_app/action_icon.png',
                                      domain='Amazon Retail',
                                      domainImg='/static/support_app/amazon_icon.png',
                                      owner='Ordering',
                                      rtt='p99 80 ms',
                                      trait='Application Programming Interface(API)',
                                      traitImg='/static/support_app/api_icon.png',
                                      tool=cancel_order_tool,
                                      impls=['Python SDK']))
        self.tools.append(SupportTool(type='Answer Tool',
                                      typeImg='/static/support_app/answer_icon.png',
                                      domain='Amazon Retail',
                                      domainImg='/static/support_app/amazon_icon.png',
                                      owner='Customer Support',
                                      trait='Natural Language Interface(NLI)',
                                      llm='Proprietary',
                                      rtt='1 - 3 sec',
                                      traitImg='/static/support_app/nli_icon.png',
                                      tool=query_support_sops_tool,
                                      tools_used=[query_similar_entities_tool],
                                      impls=['Amazon Q']))
        self.tools.append(SupportTool(type='Answer Tool',
                                      typeImg='/static/support_app/answer_icon.png',
                                      domain='External',
                                      domainImg='/static/support_app/external_icon.png',
                                      owner='AI Builder',
                                      trait='Application Programming Interface(API)',
                                      traitImg='/static/support_app/api_icon.png',
                                      rtt='p99 150 ms',
                                      tool=search_web_tool,
                                      impls=['Lambda Function']))
        self.tools.append(SupportTool(type='Action Tool',
                                      typeImg='/static/support_app/action_icon.png',
                                      domain='Amazon Web Service',
                                      domainImg='/static/support_app/aws_icon.png',
                                      owner='SimpleEmailService',
                                      trait='Application Programming Interface(API)',
                                      traitImg='/static/support_app/api_icon.png',
                                      rtt='p99 50 ms',
                                      tool=send_email_tool,
                                      impls=['Lambda Function', 'Python SDK']))
        self.tools.append(SupportTool(type='Agent Tool',
                                      typeImg='/static/support_app/composite_icon.png',
                                      domain='Amazon Retail',
                                      domainImg='/static/support_app/amazon_icon.png',
                                      owner='Search Experience',
                                      trait='Natural Language Interface(NLI)',
                                      llm='Proprietary',
                                      rtt='5 - 15 sec',
                                      traitImg='/static/support_app/nli_icon.png',
                                      tool= product_support_agent_tool,
                                      tools_used=[search_products_tool,
                                                  fetch_product_details_tool,
                                                  query_similar_entities_tool],
                                      impls=['Bedrock', 'Amazon Q']))
        self.tools.append(SupportTool(type='Answer Tool',
                                      typeImg='/static/support_app/answer_icon.png',
                                      domain='Amazon Retail',
                                      domainImg='/static/support_app/amazon_icon.png',
                                      owner='AI Builder',
                                      trait='Application Programming Interface(API)',
                                      traitImg='/static/support_app/api_icon.png',
                                      rtt='p99 450 ms',
                                      tool=query_similar_entities_tool,
                                      impls=['Lambda Function']))
        self.tools.append(SupportTool(type='Agent Tool',
                                      typeImg='/static/support_app/composite_icon.png',
                                      domain='Amazon Retail',
                                      domainImg='/static/support_app/amazon_icon.png',
                                      owner='Ordering',
                                      trait='Natural Language Interface(NLI)',
                                      traitImg='/static/support_app/nli_icon.png',
                                      llm='GPT-4',
                                      rtt='5 - 30 sec',
                                      tool=order_support_agent_tool,
                                      tools_used=[fetch_orders_tool,
                                                  identify_relevant_order_tool,
                                                  derive_days_to_deliver_tool,
                                                  decide_cancel_order_tool,
                                                  cancel_order_tool],
                                      impls=['LangChain', 'Amazon Q']))
        self.tools.append(SupportTool(type='Answer Tool',
                                      typeImg='/static/support_app/answer_icon.png',
                                      domain='Amazon Retail',
                                      domainImg='/static/support_app/amazon_icon.png',
                                      owner='Product Search',
                                      trait='Application Programming Interface(API)',
                                      traitImg='/static/support_app/api_icon.png',
                                      rtt='p99 200 ms',
                                      tool=search_products_tool,
                                      impls=['Lambda Function', 'Python SDK']))
        self.tools.append(SupportTool(type='Answer Tool',
                                      typeImg='/static/support_app/answer_icon.png',
                                      domain='Amazon Retail',
                                      domainImg='/static/support_app/amazon_icon.png',
                                      owner='Product Catalog',
                                      trait='Application Programming Interface(API)',
                                      traitImg='/static/support_app/api_icon.png',
                                      rtt='p99 250 ms',
                                      tool=fetch_product_details_tool,
                                      impls=['Python SDK']))
        self.tools.append(SupportTool(type='Action Tool',
                                      typeImg='/static/support_app/action_icon.png',
                                      domain='Amazon Retail',
                                      domainImg='/static/support_app/amazon_icon.png',
                                      owner='Ordering',
                                      trait='Application Programming Interface(API)',
                                      traitImg='/static/support_app/api_icon.png',
                                      rtt='p99 1.5 sec',
                                      tool=buy_one_click_tool,
                                      impls=['Lambda Function', 'Python SDK']))
        self.tools.append(SupportTool(type='Agent Tool',
                                      typeImg='/static/support_app/composite_icon.png',
                                      domain='Amazon Retail',
                                      domainImg='/static/support_app/amazon_icon.png',
                                      owner='Customer Support',
                                      trait='Natural Language Interface(NLI)',
                                      traitImg='/static/support_app/nli_icon.png',
                                      llm='Claude-2',
                                      rtt='5 - 35 sec',
                                      tool=buyer_support_agent_tool,
                                      tools_used=[query_support_sops_tool,
                                                  query_similar_entities_tool,
                                                  order_support_agent_tool,
                                                  product_support_agent_tool,
                                                  buy_one_click_tool],
                                      impls=['LangChain', 'Bedrock']))
                                      

    def get_tools(self) -> list[SupportTool] :
        return [t.tool for t in self.tools]
    
    def get_tool_list(self) -> list[any] :
        tl = []
        for tool in self.tools :
            startD = tool.tool.description.find(' - ') + 3
            endD = tool.tool.description.find(':param')
            impl_list = []
            for impl in tool.impls:
                if impl == 'Bedrock':
                    impl_list.append({
                        'impl': impl,
                        'implImg': '/static/support_app/bedrock.png',
                    })
                elif impl == 'Amazon Q':
                    impl_list.append({
                        'impl': impl,
                        'implImg': '/static/support_app/amazon_q.png',
                    })
                elif impl == 'LangChain':
                    impl_list.append({
                        'impl': impl,
                        'implImg': '/static/support_app/langchain.png',
                    })
                elif impl == 'Lambda Function':
                    impl_list.append({
                        'impl': impl,
                        'implImg': '/static/support_app/lambda.svg',
                    })
                elif impl == 'Python SDK':
                    impl_list.append({
                        'impl': impl,
                        'implImg': '/static/support_app/python.svg',
                    })

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
                'rtt': tool.rtt,
                'impls': impl_list,
            })
        return tl
