class IncorrectVinNumber (Exception):
    def __init__(self, message):
        self.message = message

class IncorrectCarNumbers (Exception):
    def __init__(self, message):
        self.message = message

class Car:
    def __init__(self,model,vin_number,CarNumber):
        self.model = model
        self.__is_valid_vin(vin_number)
        self.__vin = vin_number
        self.__is_valid_numbers(CarNumber)
        self.__numbers = CarNumber

    def __is_valid_vin(self,vin_number):
          if isinstance(vin_number,int):
              True
          else:
              raise IncorrectVinNumber("Некорректный тип vin номер")
          if 1000000 <= vin_number <= 9999999:
              True
          else:
              raise IncorrectVinNumber('Неверный диапазон для vin номера')

    def __is_valid_numbers(self,CarNumber):
          if isinstance(CarNumber,str):
              True
          else:
              raise IncorrectCarNumbers ('Некорректный тип данных для номеров')
          if len(CarNumber) <= 6:
              True
          else:
              raise IncorrectCarNumbers ('Неверная длина номера')

try:
  first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{first.model} успешно создан')

try:
  second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{second.model} успешно создан')

try:
  third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{third.model} успешно создан')