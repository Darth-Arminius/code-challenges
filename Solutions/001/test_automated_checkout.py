import unittest

from automated_checkout import (
  has_deal_requirements,
  combine_order_info,
  calculate_total_cost,
  calculate_total_saved
)

mock_orders = [
  {
    "id": 1,
    "orders": [
      {
        "name": "apple",
        "quantity": 2
      },
      {
        "name": "banana",
        "quantity": 1
      },
      {
        "name": "bread",
        "quantity": 1
      }
    ],
    "receipt": "INDIVIDUAL_ASCENDING"
  },
  {
    "id": 2,
    "orders": [
      {
        "name": "apple",
        "quantity": 7
      },
      {
        "name": "banana",
        "quantity": 3
      },
      {
        "name": "bread",
        "quantity": 2
      },
      {
        "name": "beer",
        "quantity": 1
      },
      {
        "name": "sweets",
        "quantity": 4
      }
    ],
    "receipt": "DEAL_ASCENDING"
  },
  {
    "id": 3,
    "orders": [
      {
        "name": "apple",
        "quantity": 1
      },
      {
        "name": "banana",
        "quantity": 1
      },
    ]
  },
  {
    "id": 4,
    "orders": [
      {
        "name": "invalid",
        "quantity": 1
      },
    ]
  },
]

mock_products = [
  {
    "name": "apple",
    "type": "fruit",
    "price": 0.5
  },
  {
    "name": "banana",
    "type": "fruit",
    "price": 1,
    "deal": {
      "products": ["apple"],
      "quantity": 2,
      "price": 0.75
    }
  },
  {
    "name": "bread",
    "type": "grains",
    "price": 1.5,
    "deal": {
      "types": ["fruit"],
      "quantity": 3,
      "price": 1
    }
  },
  {
    "name": "beer",
    "type": "alcohol",
    "price": 5,
    "deal": {
      "types": ["ready_meal"],
      "quantity": 1,
      "price": 3
    }
  },
  {
    "name": "sweets",
    "type": "confectionary",
    "price": 1.75,
    "deal": {
      "products": ["sweets"],
      "quantity": 2,
      "price": 1
    }
  },
]

mock_combined_orders = [
    {
        "name": "apple",
        "quantity": 2,
        "type": "fruit",
        "price": 0.5,
        "deal_price": None
    },
    {
        "name": "banana",
        "quantity": 1,
        "type": "fruit",
        "price": 1,
        "deal_price": 0.75
    },
    {
        "name": "bread",
        "quantity": 1,
        "type": "grains",
        "price": 1.5,
        "deal_price": 1
    }
]


class TestAutomatedCheckout(unittest.TestCase):
    def test_has_deal_requirements(self):
        """
        Test that it returns whether a deal passes all requirements
        """

        # No deal exists
        actual_has_requirements = has_deal_requirements({}, mock_orders[0]["orders"], mock_products)
        self.assertEqual(actual_has_requirements, False)

        # No matching deal item
        actual_has_requirements = has_deal_requirements(mock_products[3]["deal"], mock_orders[1]["orders"], mock_products)
        self.assertEqual(actual_has_requirements, False)

        # Not enough quantity of matching deal item
        actual_has_requirements = has_deal_requirements(mock_products[1]["deal"], mock_orders[2]["orders"], mock_products)
        self.assertEqual(actual_has_requirements, False)

        # Satisfies requirements Products
        actual_has_requirements = has_deal_requirements(mock_products[1]["deal"], mock_orders[0]["orders"], mock_products)
        self.assertEqual(actual_has_requirements, True)

        # Satisfies requirements Types
        actual_has_requirements = has_deal_requirements(mock_products[2]["deal"], mock_orders[0]["orders"], mock_products)
        self.assertEqual(actual_has_requirements, True)


    def test_combine_order_info(self):
        """
        Test that it combines the data from the orders list and the products list
        """

        # Order contains a product that doesn't exist
        actual_combined_order = combine_order_info(mock_orders[3]["orders"], mock_products)
        self.assertEqual(actual_combined_order, None)

        # Successfully combines order and product data
        actual_combined_order = combine_order_info(mock_orders[0]["orders"], mock_products)
        self.assertEqual(actual_combined_order, mock_combined_orders)


    def test_calculate_total_cost(self):
        """
        Test that it correctly adds the price of each item multiplied by the quantity and taking into account any deal prices
        """

        actual_total_cost = calculate_total_cost(mock_combined_orders)
        self.assertEqual(actual_total_cost, 2.75)


    def test_calculate_total_saved(self):
        """
        Test that it calculates the maximum cost and returns the difference between that and the total cost
        """

        actual_total_saved = calculate_total_saved(mock_combined_orders, 2.75)
        self.assertEqual(actual_total_saved, 0.75)


if __name__ == "__main__":
    unittest.main()