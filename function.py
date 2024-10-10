class Practice:
    def __init__(self, name):
        self.name = name

    def hello(self):
        print(f'Hello {self.name}!')

    # bmiを算出する関数
    def bmi(height, weight):
        return weight / (height / 100) ** 2

    # 体感温度を算出する関数
    def felt_air_temperature(temperature, humidity):
        return temperature - 1 / 2.3 * (temperature - 10) * (0.8 - humidity / 100)
