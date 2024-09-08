import json

with open('Assignment_file.json', 'r') as file:
    data = json.load(file)


# Extracting room prices & taxes
room_prices = data['assignment_results'][0]['shown_price']
taxes = json.loads(data['assignment_results'][0]['ext_data']['taxes'])
tax_amount = sum(float(value) for value in taxes.values())

# Using largest number as possible as the starting point of the comparison for the prices
cheapest_price = float('inf')
cheapest_room = None

# Find and return the cheapest (lowest) shown price (Please avoid using the minimum function)
for room, price in room_prices.items():
    price = float(price)
    if price < cheapest_price:
        cheapest_price = price
        cheapest_room = room

output = f"Cheapest shown price: {cheapest_price}\n"




# Print the total price (Net price + taxes) for all rooms along with the room type
num_of_guests = data['assignment_results'][0]['number_of_guests']

output += "Total prices for all rooms: \n"
for room, price in room_prices.items():
    total_price = float(price) + tax_amount
    output += f"Room Type: {room}, Total Price (Net + Taxes): {total_price:.2f} USD\n"

# Find and return the room type, number of guest with the cheapest price
output += "\nCheapest room details:\n"
output += f"Cheapest Price: {cheapest_price} USD\n"
output += f"Room Type: {cheapest_room}\n"
output += f"Number of Guests: {num_of_guests}\n"

with open('task_output.txt', 'w') as f:
    f.write(output)

print("Output DOne")
