import os
record_height = 'record'  # высший результат всех игр


class Background:
    def __init__(self):
        self.result = 0
        self.dir = os.path.dirname(__file__)
        self.record = 0

    def get_result(self):
        with open(os.path.join(self.dir, record_height), 'r+') as f:
            self.record = int(f.read())
        if self.result >= self.record:  # новый рекорд
            self.record = self.result
            with open(os.path.join(self.dir, record_height), 'w') as f:  # изменение рекорда
                f.write(str(self.result))
            text = ['Поздравляем!',
                    'У вас новый рекорд: {}'.format(self.result)]
        else:
            text = ['Рекорд: {}'.format(self.record),
                    'Ваш результат: {}'.format(self.result)]
        return text
