'''Demonstrate raiding a refrigerator.'''

from contextlib import closing

class RefrigeratorRaider:
    
    def open(self):
        print('Open fridge door.')

    def take(self,food):
        print(f'Finding {food}...')
        if food == 'deep fried pizza':
            raise RuntimeError('Health warning!')
        print(f'Taking {food}')

    def close(self):
        print('Close fridge door.')

def raid(food):
    with closing(RefrigeratorRaider()) as r:
        r.open()
        r.take(food)
        # r.close()

if __name__ == '__main__':
    raid('candy')
