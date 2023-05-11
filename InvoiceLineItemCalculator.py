#   Thomas Carney
#   CIS261
#   Invoice Line-Item Calculator

def heading():
    print('The Invoice Line Item Calculator\n')

def get_price():
    while True:
        try:
            return float(input('Enter price:  '))
        except ValueError:
            print('Invalid decimal number. Please try again.')
        
def get_qty():
    while True:
        try:
            return int(input('Enter quantity:  '))
        except ValueError:
            print('Invalid integer. Please try again.')

def calc_total():
    return price * qty

def show_info():
    print()
    print(f'PRICE:     {price}')
    print(f'QUANTITY:  {qty}')
    print(f'TOTAL:     {total}')

if __name__ == "__main__":
    heading()
    run = 'y'
    while run.lower() != 'n':
        price = get_price()
        qty = get_qty()
        total = calc_total()
        show_info()
        run = input('Enter another line item? (y,n):  ')
        print()
    print('Bye!')