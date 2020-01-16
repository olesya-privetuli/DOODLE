import os
# высший результат всех игр
record_height = 'record'


class Background:
    def __init__(self):
        self.result = 0
        self.dir = os.path.dirname(__file__)
        self.record = 0

    def result_on_game(self):
        return self.result

    def new_jump(self):
        self.result += 1

    def new_result(self):
        return self.result

    def get_result(self):
        with open(os.path.join(self.dir, record_height), 'r+') as f:
            self.record = int(f.read())
        if self.result >= self.record:
            # новый рекорд
            self.record = self.result
            # изменение рекорда
            with open(os.path.join(self.dir, record_height), 'w') as f:
                f.write(str(self.result))
            text = ['Поздравляем!',
                    'У вас новый рекорд: {}'.format(self.result)]
        else:
            text = ['Рекорд: {}'.format(self.record),
                    'Ваш результат: {}'.format(self.result)]
        return text