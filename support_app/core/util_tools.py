
from typing import Any


def search_web(keywards : list[str]) -> str :
    """Given a list of keywards, this tool performs web search and
    returns top ten results.

    :param keywords: list of keywards to search
    :return: top ten results
    """
    pass

def send_email(recipient : str, subject : str, body : str) -> None :
    """Sends email using AWS Simple Email Service(SES).

    :param recipient: email recipient
    :param subject: email subject
    :param body: email body
    :return: none
    """
    pass

def  product_support_agent(queryString : str, marketplace : int) -> str :
    """Assists the buyer with query related to products from Amazon Product
    Catalog. The agent helps the buyer to choose the best product from their
    intent and information buyer needs to know before they purchase. The queries
    can be informational like description, size etc., jurisdictional like
    compliance/restriction, performance like riviews & ratings, price and few
    other like seasonal, maintenance, accessories so on and so forth. The answer
    is also presented in natural language for human or AI consumption.

    :param queryString: user query string
    :param marketplace: optional marketplace id
    :return: answer to the product query  
    """
    pass

def query_similar_entities(domain: str, entity : str) -> list[str] :
    """Queries and retrievs the similar entities from semantic vector
    database in WWAS.

    :param domain: the domain from which the similar entities queried
    :param entity: the entity for which similar examples are queried
    :return: list of similar entities
    """
    pass

def text_to_sql(nl_query : str) -> str :
    """Returns a SQL query translated from a natural language query.
    The return query is a valid SQL query to be subsequently executed
    by the caller.

    :param nl_query: query to a database in natural language
    :return: valid SQL query for execution
    """
    pass

def order_support_agent(user_id : str, user_query : str) -> str :
    """Agent supporting order related queries from Amazon buyers.
    The agent can answer the status of buyer's order, days to
    deliver, past and upcming delivery details etc. The agent can
    also take action on orders like cancenling past orders, generate
    returns and refunds etc.

    :param user_id: user id of the buyer
    :param user_query: the order related query from the user
    :return: answer to the query
    """
    pass

def search_products(user_id : str, search_keywords : list[str]) -> list[Any] :
    """Given the list of product search keywords, finds and returns the list
    of relevant products from Amazon Product Catalog.

    :param user_id: user id of the buyer
    :param search_keywords: list of product search keywords
    :return: list of relevant products
    """
    pass

def fetch_product_details(product_id: str) -> dict[Any] :
    """Given the product ID, fetches the detailed information
    from the Amazon Product Catalog. The information can be
    merchendising information, jurisdictional information,
    compliance information, pricing information, seller information,
    inventory information and shipping details. 

    :param product_id: product id
    :return: map of relevant product information
    """
    pass

def buyer_support_agent(user_id: str, user_query : str) -> str :
    """Agent assisting buyer with product search, product query,
    product purchase, order query and order management related
    tasks. The agent not only provides answers to products and
    orders, it can perform actions like purchasing a product and
    canceling an order on behalf of buyer.  

    :param user_id: user ID of the buyer
    :param user_query: the query from the buyer
    :return: the answer to the buyer's query
    """
    pass

def buy_one_click(user_id: str, product_id : str) -> None :
    """Performs the one-click-buy on behalf of the buyer.
    It uses default buy options of the buyer and purchases
    only one quantity.

    :param user_id: user ID of the buyer
    :param product_id: product ID to buy
    """
    pass

def query_support_sops(user_query : str) -> str :
    """Answers any query related to customer support SOPs. This tool
    uses RAG pattern and retrieves from a vector database with all
    Customer SOPs before invoking LLM. 
    """
    pass
