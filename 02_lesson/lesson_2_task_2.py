def is_year_leap(year):
    return year % 4 == 0


year = 2024
result = is_year_leap(year)
print(f"Год {year}: {result}")

year = 2023
result = is_year_leap(year)
print(f"Год {year}: {result}")
