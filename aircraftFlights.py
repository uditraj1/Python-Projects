'''Model for aircraft flights.'''

class Flight:
    '''A flight with a particular passenger aircraft.'''
    
    def __init__(self,number,aircraft):
        if not number[:2].isalpha():
            raise ValueError(f'No airline code with {number}')
        if not number[:2].isupper():
            raise ValueError(f'Invalid airline code {number}')
        if not (number[2:].isdigit() and int(number[2:]) <=9999):
            raise ValueError(f'Invalid route number {number}')
        self._number = number
        self._aircraft = aircraft
        rows, seats = self._aircraft.seating_plan()
        self._seating = [None] + [{letter : None for letter in seats} for _ in rows]
 
    def aircraft_model(self):
        return self._aircraft.model()

    def number(self):
        return self._number
 
    def airline(self):
        return self._number[:2]

    def allocate_seat(self,seat,passenger):
        seat_row_num, letter = self._parse_seat(seat)
        if self._seating[seat_row_num][letter] is not None:
            raise ValueError(f'Seat {seat} already occupied')
        self._seating[seat_row_num][letter] = passenger

    def _parse_seat(self,seat):
        rows, seat_letters = self._aircraft.seating_plan()
        letter = seat[-1]        
        if letter not in seat_letters:
            raise ValueError(f'Invalid seat letter {letter}')
        seat_row = seat[:-1]
        try:
            seat_row_num = int(seat_row)
        except:
            raise ValueError(f'Invalid seat row {seat_row}')
        if seat_row_num not in rows:
            raise ValueError(f'Invalid row number {seat_row_num}')
        return seat_row_num, letter

    def relocate_passenger(self,from_seat,to_seat):
        from_row, from_letter = self._parse_seat(from_seat)
        if self._seating[from_row][from_letter] is None:
            raise ValueError(f'No passenger to relocate in seat {from_seat}')
        to_row, to_letter = self._parse_seat(to_seat)
        if self._seating[to_row][to_letter] is not None:
            raise ValueError(f'Seat {to_seat} is already occupied')
        self._seating[to_row][to_letter] = self._seating[from_row][from_letter]
        self._seating[from_row][from_letter] = None

    def num_available_seats(self):
        return sum(sum(1 for s in row.values() if s is None)
                   for row in self._seating if row is not None)

    def make_boarding_cards(self,card_printer):
        for passenger,seat in sorted(self._passenger_seats()):
            card_printer(passenger,seat,self._number,self._aircraft.model())

    def _passenger_seats(self):
        row_numb,seat_letter = self._aircraft.seating_plan()
        for row in row_numb:
            for letter in seat_letter:
                passenger = self._seating[row][letter]
                if passenger is not None:
                    yield(passenger,f'{row}{letter}')

def make_flights():
    f = Flight('BA758', AirbusA319('G-EUPT'))
    f.allocate_seat('12A','Guido van Rossum')
    f.allocate_seat('15F','Bjarne Stroustrup')
    f.allocate_seat('15E','Andres Hejlsberg')
    f.allocate_seat('1C','John McCarthy')
    f.allocate_seat('1D','Richard Hickey')

    g = Flight('AF72', Boeing777('F-GSPS'))
    g.allocate_seat('55K', 'Larry Wall')
    g.allocate_seat('33G', 'Yukihiro Matsumoto')
    g.allocate_seat('4B', 'Brian Kernighan')
    g.allocate_seat('4A', 'Dennis Ritchie')

    return f, g

class Aircraft:

    def __init__(self,registration):
        self._registration = registration

    def registration(self):
        return self._registration

    def num_seats(self):
        rows, seats_per_row = self.seating_plan()
        return len(rows) * len(seats_per_row)

class AirbusA319(Aircraft):

    def model(self):
        return 'Airbus A319'

    def seating_plan(self):
        return range(1,23), 'ABCDEF'

class Boeing777(Aircraft):

    def model(self):
        return 'Boeing 777'

    def seating_plan(self):
        return range(1,56), 'ABCDEGHJK'                    

def console_card_printer(passenger,seat,number,model):
    output = f'| Name: {passenger} ' \
             f' Flight: {number} ' \
             f' Seat: {seat} ' \
             f' Aircraft: {model} |' 
    banner = '+' + '-' * (len(output)-2) + '+'
    border = '|' + ' ' * (len(output)-2) + '|'
    lines = [banner,border,output,border,banner]
    card = '\n'.join(lines)
    print(card)
    print()
