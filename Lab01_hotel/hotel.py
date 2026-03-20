class Guest:
    def __init__(self, name, period, money):
        self.name = name
        self.period = period
        self.money = money

class Room:
    def __init__(self, number, price_per_day):
        self.number = number
        self.price = price_per_day
        self.occupied_until = 0
    def is_free(self, current_day):
        return current_day >= self.occupied_until

class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms = []
        self.bookings = []
    def add_room(self, room):
        self.rooms.append(room)
    def free_rooms_count(self, day):
        return sum(1 for r in self.rooms if r.is_free(day))
    def find_free_rooms(self, start, end):
        return [r for r in self.rooms if r.occupied_until <= start]
    def book_room(self, guest, start_day):
        total_cost = 0
        for room in self.rooms:
            total_cost = room.price * guest.period
            if room.is_free(start_day) and guest.money >= total_cost:
                end_day = start_day + guest.period
                room.occupied_until = end_day
                guest.money -= total_cost
                self.bookings.append({
                    'room': room.number, 'guest': guest.name,
                    'start': start_day, 'end': end_day, 'cost': total_cost
                })
                return True
        return False
    def calc_cost(self, room, days):
        return room.price * days
    def get_profit(self, start, end):
        total = 0
        for b in self.bookings:
            if b['start'] >= start and b['end'] <= end:
                total += b['cost']
        return total
    def find_guest(self, name, day):
        for b in self.bookings:
            if b['guest'] == name and b['start'] <= day < b['end']:
                return f"Гість {name} у номері {b['room']}"
        return "Гість не знайдений"
