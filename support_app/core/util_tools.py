
def search_web(keywards : list[str]) -> str :
    """Given a list of keywards, this tool performs web search and
    returns top ten results.

    :param keywords: list of keywards to search
    :return: top ten results
    """
    pass

def send_email(recipient : str, subject : str, body : str) :
    """Sends email using AWS SES.

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

def query_vector_db(entity : str) -> list[str] :
    """Queries and retrievs the similar entities from AWS Kendra.

    :param entity: the entity for which similar examples are queried
    :return: list of similar entities
    """
    pass
