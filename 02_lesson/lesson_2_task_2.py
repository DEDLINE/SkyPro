def is_year_leap(year):
    return year % 4 == 0


year = 2024
print(f"Год {year}: {is_year_leap(year)}")

year = 2023
print(f"Год {year}: {is_year_leap(year)}")
