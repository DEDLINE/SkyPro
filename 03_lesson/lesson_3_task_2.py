from smartphone import Smartphone

catalog = [
    Smartphone("Samsung", "Galaxy S21", "+79111234567"),
    Smartphone("Apple", "iPhone 13", "+79227654321"),
    Smartphone("Google", "Pixel 6", "+79339876543"),
    Smartphone("OnePlus", "9 Pro", "+79445678901"),
    Smartphone("Xiaomi", "Mi 11", "+79552345678")
]

for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.phone_number}")
