from address import Address
from mailing import Mailing

from_address = Address("123456", "Москва", "Красная пл.", "1", "10")
to_address = Address("654321", "Санкт-Петербург", "Невский пр.", "25", "5")

mailing = Mailing(to_address, from_address, 1500, "RU123456789")

print(f"Отправление {mailing.track} из {mailing.from_address.index}, "
      f"{mailing.from_address.city}, {mailing.from_address.street}, "
      f"{mailing.from_address.house} - {mailing.from_address.apartment} "
      f"в {mailing.to_address.index}, {mailing.to_address.city}, "
      f"{mailing.to_address.street}, {mailing.to_address.house} -"
      f"{mailing.to_address.apartment}. "
      f"Стоимость {mailing.cost} рублей.")
