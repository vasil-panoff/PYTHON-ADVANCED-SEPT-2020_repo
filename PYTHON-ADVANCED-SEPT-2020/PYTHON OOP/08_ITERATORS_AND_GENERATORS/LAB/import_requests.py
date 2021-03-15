import requests

response = requests.get(f'https://api.instantwebtools.net/v1/passenger?page=5')
data = response.json()
print(data)

class PassengerReader:
    def __init__(self):
        self.results_per_page = 5
        response = requests.get(f'https://api.instantwebtools.net/v1/passenger?page=0&size={self.results_per_page}')
        data = response.json()
        self.current_page = 0
        self.index = 0
        self.total_pages = data['totalPages']
        self.reults_on_page = data['data']


    def __iter__(self):
            return self

    def __next__(self):
        index = self.index
        if self.index <= self.results_per_page:
            self.index += 1
            return self.results_per_page[index]
        elif self.index > self.results_per_page:
            self.current_page += 1
            response = requests.get(f'https://api.instantwebtools.net/v1/passenger?page={self.current_page}&size={results_per_page}')
            self.results_on_page = response.json()['data']
            self.index = 1
            return self.results_on_page[0]

passenger_reader = PassengerReader()

for passenger in passenger_reader:
    print(passenger)
