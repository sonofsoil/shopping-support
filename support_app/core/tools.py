
def fetch_order(userId: str, description : str) -> dict:
    """ Fetches the order for the user.
    :param userId: user identifier
    :param description: product description
    :return: the order details in JSON structure containing orderId, delivery date and order status
    """
    print(f"userId: {userId} description - {description}")
    return {
        'delivery_date' : 'October 29, 2023',
        'order_status' : 'pending',
        'order_id' : 'order-123'
    }

def cancel_order(userId: str, orderId: str) -> bool:
    """ Cancels user order and return the cancel status.
    :param userId: user identifier
    :param orderId: order identifier
    :return: True if order canclled successfully, false otherwise
    """
    print(f"userId: {userId} orderId - {orderId}")
    if 'happyuser' == userId:
        return f'order {orderId} was successfully canceled for user {userId}'
    return f'failed to cancel order {orderId} for user {userId}'

