orders = [
    (101, "Anu", "Laptop", 1, 55000),
    (102, "Ravi", "Mouse", 2, 500),
    (103, "Meena", "Keyboard", 1, 1500),
    (104, "John", "Laptop", 1, 55000),
    (105, "Sara", "Monitor", 2, 12000),
    (106, "Kiran", "Mouse", 5, 500),
    (107, "Anu", "Headphones", 2, 2000),
]
processed_orders = [
    (
        order_id,
        customer,
        product,
        quantity,
        price,
        total := quantity * price
    )
    for order_id, customer, product, quantity, price in orders
]
print("\nProcessed Orders:")
for order in processed_orders:
    print(order)

high_value_orders = [
    order for order in processed_orders if order[5] > 5000
]

print("\nHigh Value Orders:")
print(high_value_orders)

total_revenue = sum(order[5] for order in processed_orders)
print("\nTotal Revenue:", total_revenue)

unique_products = {product for _, _, product, _, _ in orders}
print("\nUnique Products:", unique_products)

top_products = sorted(
    {product for _, _, product, _, _ in orders},
    key=lambda p: sum(q for _, _, prod, q, _ in orders if prod == p),
    reverse=True
)
print("\nTop Selling Products:", top_products)
big_customers = {
    customer
    for _, customer, _, _, _ in orders
    if sum(q*p for _, cust, _, q, p in orders if cust == customer) > 7000
}

print("\nHigh Spending Customers:", big_customers)
sorted_orders = sorted(processed_orders, key=lambda x: x[5], reverse=True)

print("\nSorted Orders by Revenue:")
for order in sorted_orders:
    print(order)
discounted_orders = [
    (
        order[0],
        order[1],
        order[2],
        order[3],
        order[4],
        order[5] * 0.9 if order[5] > 20000 else order[5]
    )
    for order in processed_orders
]

print("\nOrders After Discount:")
for order in discounted_orders:
    print(order)

