from datetime import datetime

class Greeter:
  def __init__(self, name, store) -> None:
    self.name = name
    self.store = store
  
  def _day(self):
    return datetime.now().strftime('%A')
  
  def _part_of_day(self):
    hour = datetime.now().hour
    if (hour < 12):
      return 'Morning'
    elif (hour < 17):
      return 'Afternoon'
    else:
      return 'Evening'
  
  def greet(self):
    print(f'Hi, I am {self.name}, and welcome to {self.store}')
    print(f'How\'s your {self._day()} {self._part_of_day()} going?')
    print('Hope you are doing well!')


greeter = Greeter('Yen', 'Crab Soup')
greeter.greet()