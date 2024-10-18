tuple_items=()
total_items=int(input("Enter the total number of items: "))
for i in range(total_items):
    user_input = int(input("Enter a number: "))
    tuple_items = tuple_items + (user_input,)
print(f"Items are added to the tuple are{tuple_items}")

list_items = []
total_items=int(input("Enter the total number of list items: "))
for i in range(total_items):
    user_input = int(input("Enter a number: "))

    list_items.append(user_input)
print(f"Items added to the list are{tuple(list_items)}")