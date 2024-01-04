import json

orders = []
while True:
    id = int(input("Введіть ID замовлення (або 0 для завершення введення): "))
    if id == 0:
        break

    product = input("Введіть назву товару: ")
    quantity = int(input("Введіть кількість: "))

    order = {"order_id": id, "product": product, "quantity": quantity}
    orders.append(order)


with open("orders.json", "w") as json_file:
    json.dump(orders, json_file)

print("Дані успішно експортовано.")

with open("orders.json", "r") as json_file:
    orders = json.load(json_file)


total_quantity = sum(order["quantity"] for order in orders)
average_quantity = total_quantity / len(orders)


