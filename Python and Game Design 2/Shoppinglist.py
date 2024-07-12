shopping_list = {
    "Groceries": [
        "Milk",
        "Bread",
        "Eggs",
        "Fruits: Apples",
        "Fruits: Bananas",
        "Fruits: Oranges",
        "Vegetables: Carrots",
        "Vegetables: Broccoli",
        "Vegetables: Spinach"
    ],
    "Household Items": [
        "Toilet Paper",
        "Paper Towels",
        "Cleaning Supplies: Dish Soap",
        "Cleaning Supplies: Laundry Detergent"
    ],
    "Personal Care": [
        "Shampoo",
        "Toothpaste",
        "Soap"
    ]
}

def print_shopping_list(shopping_list):
    for category, items in shopping_list.items():
        print(f"## {category}")
        for item in items:
            print(f"- [ ] {item}")
        print()  # Add a blank line between categories

if __name__ == "__main__":
    print_shopping_list(shopping_list)
