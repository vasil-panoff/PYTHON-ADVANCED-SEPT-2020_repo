class Time:
    max_hours = 23
    max_minutes = 59
    max_seconds = 59

    def __init__(self, hours: int, minutes: int, seconds: int):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def set_time(self, hours: int, minutes: int, seconds: int) -> None:
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def get_time(self):
        return f"{self.hours:02d}:{str(self.minutes).zfill(2)}:{self.seconds:02d}"

    def next_second(self) -> str:
        self.seconds = (self.seconds + 1) % 60
        self.minutes = (self.minutes + int(self.seconds == 0)) % 60
        self.hours = (self.hours + int(self.minutes == 0)) % 24
        return self.get_time()


time = Time(23, 59, 59)
print(time.next_second())
time = Time(10, 59, 59)
print(time.next_second())
time = Time(9, 30, 59)
print(time.next_second())
