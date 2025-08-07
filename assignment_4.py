# Task 4: List Comprehensions with Sales Data
# Scenario
# A retail analytics team needs to process quarterly sales data to generate insights and reports.
# The Dataset
sales_data = [
    {'product': 'Laptop', 'q1': 150, 'q2': 180, 'q3': 160, 'q4': 200},
    {'product': 'Mouse', 'q1': 300, 'q2': 280, 'q3': 320, 'q4': 350},
    {'product': 'Keyboard', 'q1': 200, 'q2': 190, 'q3': 210, 'q4': 230},
    {'product': 'Monitor', 'q1': 80, 'q2': 95, 'q3': 85, 'q4': 110},
    {'product': 'Headphones', 'q1': 120, 'q2': 140, 'q3': 130, 'q4': 160}
]
# Your Tasks
# Task 4a: Calculate Annual Totals
# TODO: Use list comprehension to create a new list with annual totals
# Include product name and total_sales
# [{'product': <product name>, 'total_sales': q1 + q2 + q3 + q4}]

annual_sales = annual_sales = [{'product': item['product'],'total_sales': item['q1'] + item['q2']
                                + item['q3'] + item['q4']} for item in sales_data]
 

# Test your result
print("Annual Sales Totals:")
for item in annual_sales:
    print(f"  {item['product']}: {item['total_sales']} units")
# Expected Output:
# Annual Sales Totals:
#   Laptop: 690 units
#   Mouse: 1250 units
#   Keyboard: 830 units
#   Monitor: 370 units
#   Headphones: 550 units

# Task 4b: Find High-Performing Products-----------------------------
# TODO: Use list comprehension to find products with total sales > 600
# Return just the product names-------------------------------
# high_performers = [# YOUR CODE HERE for product in sales_data # YOUR CONDITION HERE]

# # Test your result---------------------------
# print("High-Performing Products (>600 units):")
# for product in high_performers:
#     print(f"  {product}")


# Expected Output:
# High-Performing Products (>600 units):
#   Laptop
#   Mouse
#   Keyboard

# Task 4c: Growth Analysis-------------------------------------------
# TODO: Use list comprehension to calculate Q4 vs Q1 growth percentage
# Formula: ((Q4 - Q1) / Q1) * 100
# Include products that had positive growth---------------------------
# growth_analysis = [# YOUR CODE HERE for product in sales_data # YOUR CONDITION HERE]

# # Test your result-------------------------------------
# print("Products with Positive Growth (Q4 vs Q1):")
# for item in growth_analysis:
#     print(f"  {item['product']}: {item['growth_percentage']:.1f}% growth")
# Expected Output:
# Products with Positive Growth (Q4 vs Q1):
#   Laptop: 33.3% growth
#   Mouse: 16.7% growth
#   Keyboard: 15.0% growth
#   Monitor: 37.5% growth
#   Headphones: 33.3% growth
# Submission Requirements
# What to Submit
# Complete Python file with all your solutions
# Test output showing all functions work correctly