# Task 3: Filter Function with Customer Data
# Scenario
# An e-commerce company wants to identify premium customers for a special promotion based on their purchase history and account status.
# The Dataset
customers = [
    {'name': 'Alice Johnson', 'total_spent': 1250, 'orders': 8, 'vip_member': True},
    {'name': 'Bob Smith', 'total_spent': 750, 'orders': 12, 'vip_member': False},
    {'name': 'Carol Davis', 'total_spent': 2100, 'orders': 15, 'vip_member': True},
    {'name': 'David Wilson', 'total_spent': 450, 'orders': 3, 'vip_member': False},
    {'name': 'Emma Brown', 'total_spent': 980, 'orders': 7, 'vip_member': False},
    {'name': 'Frank Miller', 'total_spent': 1800, 'orders': 20, 'vip_member': True}
]
# Your Task
# Premium Customer Identification
# TODO: Use filter() to find customers who qualify for premium promotion
# Criteria: (total_spent >= 1000 AND orders >= 5) OR vip_member == True
premium_customers = list(filter(lambda customers: customers['total_spent'] >= 1000 and customers['orders'] >= 5 
                                or customers['vip_member'] == 'True', customers))

# Test your result
print("Premium Customers for Special Promotion:")
for customer in premium_customers:
    print(f"  {customer['name']} - Spent: ${customer['total_spent']}, Orders: {customer['orders']}")
# Expected Output:
# Premium Customers for Special Promotion:
#   Alice Johnson - Spent: $1250, Orders: 8
#   Carol Davis - Spent: $2100, Orders: 15
#   Frank Miller - Spent: $1800, Orders: 20