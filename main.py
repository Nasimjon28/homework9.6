import random
import time
from threading import Thread


class Knight(Thread):
    def __init__(self, name, skill, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name
        self.skill = skill

    def run(self):
        day = 0
        count_warriors = 100
        print(f'{self.name}, на нас напали!', flush=True)  # flush - небуферизованный вывод
        # while count_warriors:
        while count_warriors != 0:
            day += 1
            count_warriors -= self.skill
            print(f'{self.name}, сражается {day} день(дня)..., осталось {count_warriors} воинов', flush=True)
            time.sleep(1)

        print(f'{self.name} одержал победу спустя {day} дней!', flush=True)


knight1 = Knight("Sir Lancelot", 10)  # Низкий уровень умения
knight2 = Knight("Sir Galahad", 20)  # Высокий уровень умения
knight1.start()
knight2.start()
knight1.join()
knight2.join()
print(f'Все битвы закончились!', flush=True)
