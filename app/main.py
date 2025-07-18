class Car:
    def __init__(self,
                 comfort_class: int, clean_mark: int, brand: str) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self, distance_from_city_center: float, clean_power: float,
                 average_rating: float, count_of_ratings: int) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, car_list: list) -> float:
        total = 0
        for i in car_list:
            total += self.wash_single_car(i)
        return total

    def calculate_washing_price(self, car: Car) -> float:
        price = (car.comfort_class * (self.clean_power - car.clean_mark)
                 * self.average_rating / self.distance_from_city_center)
        return round(price, 1)

    def wash_single_car(self, car: Car) -> float:
        income = 0
        if car.clean_mark < self.clean_power:
            car.clean_mark = self.clean_power - car.clean_mark + car.clean_mark
            income += self.calculate_washing_price(car)
        return income

    def rate_service(self, rate: float) -> None:
        calc = 0
        calc = self.count_of_ratings * self.average_rating + rate
        self.count_of_ratings += 1
        calc /= self.count_of_ratings
        self.average_rating = round(calc, 1)


station1 = CarWashStation(3, 9, 4.2, 11)
car_1 = Car(2, 1, "Ford")

print(station1.serve_cars([car_1]))
