import json
from enum import Enum

class Receipt(Enum):
    INDIVIDUAL_ASCENDING = 1
    INDIVIDUAL_DESCENDING = 2
    DEAL_ASCENDING = 3
    DEAL_DESCENDING = 4
    ALPHABETICAL_ASCENDING = 5
    ALPHABETICAL_DESCENDING = 6
    TYPE_ASCENDING = 7
    TYPE_DESCENDING = 8


    def sort(self, product):
        """
        Keys for sorting depending on the receipt type
        """
        match self.value:
            case 1 | 2:
                return product["price"]
            case 3 | 4:
                return product.get("deal_price") or product["price"]
            case 5 | 6:
                return product["name"]
            case 7 | 8:
                return product["type"]
            case _:
                return None


    def reverse(self):
        """
        Just returns whether the sorting should be reversed or not
        """
        match self.value:
            case 1 | 3 | 5 | 7:
                return False
            case 2 | 4 | 6 | 8:
                return True
            case _:
                return False


def get_products():
    """
    Opens the products.json file, reads the content, closes the file
    Returns the content
    """
    products_file = open("Solutions/001/products.json")
    products_data = json.load(products_file)
    products_file.close()

    return products_data


def get_orders():
    """
    Opens the orders.json file, reads the content, closes the file
    Returns the content
    """
    orders_file = open("Solutions/001/orders.json")
    orders_data = json.load(orders_file)
    orders_file.close()

    return orders_data


def has_deal_requirements(deal, orders, products):
    """
    Checks whether the deal is based on certain products or certain types of products
    Then checks if any items in the basket match the deal and adds its quantity to a running total
    If the quantity is enough to satisfy the deal then return True
    Otherwise the deal requirements haven't been met and returns False
    """
    items = deal.get("products") or deal.get("types") or None

    if items is None:
        return False

    total_quantity = 0
    for item in items:
        for order in orders:
          order_product = next((product for product in products if product.get("name") == order.get("name")), None)
          if order_product is None:
              continue

          deal_matching_order = order if order_product.get("name") == item or order_product.get("type") == item else None
          if deal_matching_order:
              total_quantity += deal_matching_order["quantity"]
              if total_quantity >= deal["quantity"]:
                  return True

    return False


def combine_order_info(product_orders, products):
    """
    Checks if the product in the basket exists in the product list
    Checks if the product has a deal and whether that deal's requirements have been met
    Then combines data from the orders list and data from the products list into one array of dictionaries
    """
    combined_orders = []
    for product_order in product_orders:
        product_order_name = product_order["name"]
        product = next((product for product in products if product["name"] == product_order_name), None)
        if product is None:
            return None

        deal = product.get("deal") or None
        deal_price = None
        if deal:
            if has_deal_requirements(product["deal"], product_orders, products):
                deal_price = deal["price"]

        combined_orders.append({
          "name": product_order_name,
          "quantity": product_order["quantity"],
          "type": product["type"],
          "price": product["price"],
          "deal_price": deal_price
        })

    return combined_orders


def calculate_total_cost(orders):
    """
    Simply adds the deal price or normal price multiplied by the quantity bought to a running total
    Returns said total
    """
    total_cost = 0

    for order in orders:
        price = order.get("deal_price") or order.get("price")
        total_cost += price * order["quantity"]

    return total_cost


def calculate_total_saved(orders, total_cost):
    """
    Similar to calculating total cost except ignores deal prices and adds the full price instead
    Then compares the difference between the maximum full cost and the total cost which included deals and returns the difference
    """
    maximum_cost = 0

    for order in orders:
        price = order.get("price")
        maximum_cost += price * order["quantity"]

    return maximum_cost - total_cost


def automated_checkout():
    """
    Starts by reading in the products and orders lists
    Loops through every order and prints out its ID
    Sets the receipt type using the Receipt enum class and the data from the order
    Checks if the receipt type is valid and skips to the next order if it is not
    Combines the order and product data
    If it returns None it means one of the products in the order is invalid and skips to the next order
    Sorts the basket according to the receipt type and prints the details of each product
    Gets the total cost and prints it
    Gets the total saved and prints it
    """
    products = get_products()
    orders = get_orders()

    for order in orders:
        order_id = order["id"]
        print("~~~~~~~~~~~~~")
        print(f"Order ID: {order_id}")

        receipt = order["receipt"]
        try:
            receipt_type = Receipt[receipt]
        except:
            print(f"Invalid receipt type in order")
            print("~~~~~~~~~~~~~")
            print("\n")
            continue

        product_orders = order["orders"]
        combined_orders = combine_order_info(product_orders, products)
        if combined_orders is None:
            print(f"Invalid products in order")
            print("~~~~~~~~~~~~~")
            print("\n")
            continue

        combined_orders.sort(key=receipt_type.sort, reverse=receipt_type.reverse())
        for combined_order in combined_orders:
            name = combined_order["name"]
            quantity = combined_order["quantity"]
            price = combined_order.get("deal_price") or combined_order.get("price")
            formatted_price = '{0:.2f}'.format(price)
            print(f"{quantity}x {name} £{formatted_price}")

        total_cost = calculate_total_cost(combined_orders)
        formatted_total_cost = '{0:.2f}'.format(total_cost)
        print(f"Total Cost: £{formatted_total_cost}")

        total_saved = calculate_total_saved(combined_orders, total_cost)
        formatted_total_saved = '{0:.2f}'.format(total_saved)
        print(f"Total Saved: £{formatted_total_saved}")
        print("~~~~~~~~~~~~~")
        print("\n")


automated_checkout()
