from datetime import datetime, timedelta

class Car:
    def __init__(self, price, creation_time=None, lifespan=None):

        if not isinstance(price, (int, float)):
            raise ValueError("Цена должна быть числом")
        self.price = price

        if creation_time is None:
            self.creation_time = datetime.now()
        else:
            self.creation_time = creation_time

        if lifespan is None:
            self.lifespan = timedelta(days=365)
        else:
            self.lifespan = lifespan


    def calculate_depreciation(self):
        current_time = datetime.now()
        age = current_time - self.creation_time
        depreciation_rate = age.total_seconds() / self.lifespan.total_seconds()
        depreciation_total = self.price * depreciation_rate
        depreciation_total_rounded = round(depreciation_total, 2)
        return depreciation_total_rounded


class Toyota(Car):
    def __init__(self, price, creation_time=None, lifespan=None):
        super().__init__(price, creation_time, lifespan)
        if lifespan is None:
            self.lifespan = timedelta(days=365 * 2)

car1 = Car(2000000)
toyota1 = Toyota(2000000)

current_value_car1 = car1.calculate_depreciation()
current_value_toyota1 = toyota1.calculate_depreciation()

print(f"Сумма амортизационных отчислений автомобиля на {datetime.now().date()} : ", current_value_car1)
print(f"Сумма амортизационных отчислений автомобиля Toyota на {datetime.now().date()}: ", current_value_toyota1)
