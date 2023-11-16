from datetime import datetime, timedelta

def fetch_orders(user_id: str = "Shopper") -> dict:
    """ Fetches the existing orders for the user. If no order found
    for the user, returns empty list.
    :param user_id: user identifier
    :return: the order list containing order details, including
      order_id, product_id, delivery date, product_title, product_type,
      product_description, quantity and order status.
    """
    #print(f"userId: {userId} description - {description}")
    now = datetime.now()
    two_days_from_now = now + timedelta(days=2, hours=3)
    ten_days_from_now = now + timedelta(days=10)
    yesterday = now - timedelta(days=1)
    if user_id == 'Shopper' :
        return [{
            'delivery_date' : f'{two_days_from_now.strftime("%B %d, %Y")}',
            'order_status' : 'shipped',
            'order_id' : 'order-1',
            'product_id' : 'product-123',
            'product_title' : 'Engraved Crystal Flower Vase',
            'product_type' : 'home decor interior',
            'quantity' : 1,
            'product_details' : 'A long-time favorite, this classic crystal vase never disappoints.'
        }, {
            'delivery_date' : f'{ten_days_from_now.strftime("%B %d, %Y")}',
            'order_status' : 'pending',
            'order_id' : 'order-2',
            'product_id' : 'product-456',
            'product_title' : 'Affresh Dishwasher Cleaner',
            'product_type' : 'kitchen appliance supply',
            'quantity' : 6,
            'product_details' : 'Affresh® dishwasher cleaner cleans even where you can’t\
              see to help remove odor-causing residues and buildup that can form in machines over time. '
        }, {
            'delivery_date' : f'{yesterday.strftime("%B %d, %Y")}',
            'order_status' : 'delivered',
            'order_id' : 'order-3',
            'product_id' : 'product-789',
            'product_title' : 'The Count of Monte Cristo',
            'product_type' : 'book',
            'quantity' : 1,
            'product_details' : 'Nominated as one of America’s best-loved novels by PBS’s\
              The Great American Read.'
        }]
    return []

def cancel_order(userId: str, orderId: str) -> bool:
    """ Cancels user order and return the cancel status.
    :param userId: user identifier
    :param orderId: order identifier
    :return: True if order canclled successfully, false otherwise
    """
    print(f"userId: {userId} orderId - {orderId}")
    if 'Shopper' == userId:
        return f'order {orderId} was successfully canceled for user {userId}'
    return f'failed to cancel order {orderId} for user {userId}'
