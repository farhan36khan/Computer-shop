# Global constants
BASIC_COMPONENTS_COST = 200
DISCOUNT_ONE_ITEM = 0.05
DISCOUNT_TWO_OR_MORE_ITEMS = 0.10

# Global arrays to store item information
case_items = [("A1", "Compact", 75.00), ("A2", "Tower", 150.00)]
ram_items = [("B1", "8 GB", 79.99), ("B2", "16 GB", 149.99), ("B3", "32 GB", 299.99)]
hdd_items = [("C1", "1 TB HDD", 49.99), ("C2", "2 TB HDD", 89.99), ("C3", "4 TB HDD", 129.99)]
ssd_items = [("D1", "240 GB SSD", 59.99), ("D2", "480 GB SSD", 119.99)]
second_hdd_items = [("E1", "1 TB HDD", 49.99), ("E2", "2 TB HDD", 89.99), ("E3", "4 TB HDD", 129.99)]
optical_drive_items = [("F1", "DVD/Blu-Ray Player", 50.00), ("F2", "DVD/Blu-Ray Re-writer", 100.00)]
os_items = [("G1", "Standard Version", 100.00), ("G2", "Professional Version", 175.00)]

# Global variables to store the chosen items and the price
chosen_items = {
    "case": None,
    "ram": None,
    "hdd": None,
    "additional_items": [],
    "os": None
}


def display_items(category, items):
    print(f"Available {category} items:")
    for item in items:
        item_code, description, price = item
        print(f"{item_code}: {description} - ${price:.2f}")


def choose_item(category, items):
    display_items(category, items)
    while True:
        item_code = input(f"Select a {category} item (Enter item code): ").strip().upper()
        for item in items:
            if item_code == item[0]:
                return item
        print("Invalid item code. Please try again.")


def order_main_items():
    print("Welcome to the Online Computer Shop!")
    print("Let's start by ordering the main items.")
    chosen_items["case"] = choose_item("case", case_items)
    chosen_items["ram"] = choose_item("RAM", ram_items)
    chosen_items["hdd"] = choose_item("Main Hard Disk Drive", hdd_items)


def order_additional_items():
    additional_items_cost = 0
    while True:
        display_items("Additional items", ssd_items + second_hdd_items + optical_drive_items)
        additional_item_code = input("Select an additional item (Enter item code, or 'done' to finish): ").strip().upper()
        if additional_item_code == 'DONE':
            break
        for item in ssd_items + second_hdd_items + optical_drive_items:
            if additional_item_code == item[0]:
                additional_items_cost += item[2]
                chosen_items["additional_items"].append(item)
                print(f"{item[1]} added to the order.")
                break
        else:
            print("Invalid item code. Please try again.")
    return additional_items_cost


def order_os():
    display_items("Operating System", os_items)
    while True:
        os_item_code = input("Select an Operating System (Enter item code, or 'none' for no OS): ").strip().upper()
        if os_item_code == 'NONE':
            break
        for item in os_items:
            if os_item_code == item[0]:
                chosen_items["os"] = item
                print(f"{item[1]} added to the order.")
                break
        else:
            print("Invalid item code. Please try again.")


def calculate_total_price():
    total_price = BASIC_COMPONENTS_COST
    total_price += chosen_items["case"][2]
    total_price += chosen_items["ram"][2]
    total_price += chosen_items["hdd"][2]
    total_price += sum(item[2] for item in chosen_items["additional_items"])
    if chosen_items["os"]:
        total_price += chosen_items["os"][2]
    return total_price


def apply_discount(total_price):
    additional_item_count = len(chosen_items["additional_items"])
    if additional_item_count == 1:
        discount = DISCOUNT_ONE_ITEM
    elif additional_item_count >= 2:
        discount = DISCOUNT_TWO_OR_MORE_ITEMS
    else:
        discount = 0
    discount_amount = total_price * discount
    return total_price - discount_amount, discount_amount


def main():
    order_main_items()
    additional_items_cost = order_additional_items()
    order_os()
    total_price = calculate_total_price()
    final_price, discount_amount = apply_discount(total_price)

    print("\nOrder summary:")
    print(f"Case: {chosen_items['case'][1]} - ${chosen_items['case'][2]:.2f}")
    print(f"RAM: {chosen_items['ram'][1]} - ${chosen_items['ram'][2]:.2f}")
    print(f"Main Hard Disk Drive: {chosen_items['hdd'][1]} - ${chosen_items['hdd'][2]:.2f}")
    for item in chosen_items["additional_items"]:
        print(f"Additional Item: {item[1]} - ${item[2]:.2f}")
    if chosen_items["os"]:
        print(f"Operating System: {chosen_items['os'][1]} - ${chosen_items['os'][2]:.2f}")
    print(f"Total Price (before discount): ${total_price:.2f}")
    print(f"Discount Applied: ${discount_amount:.2f}")
    print(f"Final Price: ${final_price:.2f}")


if __name__ == "__main__":
    main()
