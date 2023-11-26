
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

def query_product_catalog(queryString : str, marketplace : int) -> str :
    """Answers to a user query related to products from Amazon catalog.
    The answer is also presented in natural language for human or AI
    consumption.

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

def order_support_agent(ser_id : str, user_query : str) -> str :
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
