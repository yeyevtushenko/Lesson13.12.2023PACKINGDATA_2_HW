import json
import pickle
import gzip

class Stadium:
    def __init__(self, name, opening_date, country, city, capacity):
        self.name = name
        self.opening_date = opening_date
        self.country = country
        self.city = city
        self.capacity = capacity

    def __sub__(self, other):
        return abs(self.capacity - other.capacity)

    def __add__(self, other):
        return abs(self.capacity + other.capacity)

    def __mul__(self, other):
        return abs(self.capacity * other.capacity)

    def __truediv__(self, other):
        return abs(self.capacity / other.capacity)

    def to_dict(self):
        return {
            "name": self.name,
            "opening_date": self.opening_date,
            "country": self.country,
            "city": self.city,
            "capacity": self.capacity
        }

    def to_json(self, filename):
        with open(filename, 'w') as json_file:
            json.dump(self.to_dict(), json_file)

    @classmethod
    def from_json(cls, filename):
        with open(filename, 'r') as json_file:
            data = json.load(json_file)
            return cls(**data)

    def to_pickle(self, filename):
        with open(filename, 'wb') as pickle_file:
            pickle.dump(self.to_dict(), pickle_file)

    @classmethod
    def from_pickle(cls, filename):
        with open(filename, 'rb') as pickle_file:
            data = pickle.load(pickle_file)
            return cls(**data)

    def to_gzip_json(self, filename):
        with gzip.open(filename, 'wt') as gzip_file:
            json.dump(self.to_dict(), gzip_file)

    @classmethod
    def from_gzip_json(cls, filename):
        with gzip.open(filename, 'rt') as gzip_file:
            data = json.load(gzip_file)
            return cls(**data)


stadion1 = Stadium("Стадіон 1", "01.01.1995", "Україна", "Київ", 4000)


stadion1.to_json("stadion1.json")
stadion_from_json = Stadium.from_json("stadion1.json")

stadion1.to_pickle("stadion1.pkl")
stadion_from_pickle = Stadium.from_pickle("stadion1.pkl")

stadion1.to_gzip_json("stadion1.json.gz")
stadion_from_gzip_json = Stadium.from_gzip_json("stadion1.json.gz")
