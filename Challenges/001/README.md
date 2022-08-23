# CODE CHALLENGE #1 01/08/2022 - AUTOMATED CHECKOUT SERVICE

For this challenge, you need to build an Automated Checkout Service for a grocery store:

- You need to write a program that allows customers to purchase their shopping at the correct price, including all deals & discounts, and get an ordered receipt based on their requirements.
- You can use any language and framework you want but make sure it can read in a JSON file.
- You will be provided with a list of products (`products.txt`) & types of receipt (`receipts.txt`) (you will need to create your own dataset for these) and your program will be tested against a JSON dataset of customer orders (`orders.json`).
- Your program must charge each customer the correct total and output a receipt in the correct order they requested.

_An example: A customer buys 2 apples, 1 banana and a loaf of bread. They want their receipt ordered by individual cost ascending. Apples cost £0.50 each, bananas cost £1 each but if you buy 2 apples then bananas cost £0.75 each, bread costs £1.50 but if you buy 3 of any fruit then it costs £1.00. This means the total would be £2.75 for this example customer. Their receipt would be ordered as: 2 x apples £0.50, 1 x banana £0.75, 1 x loaf of bread £1.00. Bonus points if you also output how much the customer saved from all the deals at the bottom of the receipt, in this case this customer saved £0.75 from the deals._

You will be marked on whether the program meets the criteria, the quality, readability, and performance of the code, and any testing you include.

Good luck
