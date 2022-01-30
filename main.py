# Bekomme die nur so global *kein Peil*
money_names = []
money_worths = []
product_names = []
product_prices = []
numbers_list = ['1.', '2.', '3.', '4.', '5.', '6.', '7.', '8.', '9.', '10.']
money_input = 0

# Alle geldbezogenen Themen
class Money:

    def __init__(self, name, worth):
        self.name = name
        self.worth = worth
        # Die Werte in listen übertragen zur leichteren Ausgabe
        money_names.append(name)
        money_worths.append(worth)

    #Geldrückgabefunktion
    def money_return(money_input, price_item):
        print('Rückgeld:')
        money_overpayed = money_input - price_item

        for x,y in zip(money_names, money_worths):

            coin_amount = money_overpayed // y
            print(str(coin_amount) + ' ' + str(x))
            money_overpayed = money_overpayed % y

#Alle produktbezogenen Themen
class Product:
    def __init__(self, product_name, price):
        self.product_name = product_name
        self.price = price
        #Übertragen in Listen zr leichteren Ausgabe
        product_names.append(product_name)
        product_prices.append(price)

    #Umrechnung des Preises von float in int
    def price_is(self):
        return int(self.price * 100)


    #Ausgabefunktion Produktnamen mit Preis
    def product_call():

        product_listing = "\n".join("{} \t{} \t\t\t{}".format(x, y, z) for x, y, z in zip(numbers_list ,product_names, product_prices))
        print(product_listing)



# Definition der Geldstücke für ein und Auswurf

note1 = Money('1 Cent', 1)
note2 = Money('2 Cent', 2)
note3 = Money('5 Cent', 5)
note4 = Money('10 Cent', 10)
note5 = Money('20 Cent', 20)
note6 = Money('50 Cent', 50)
note7 = Money('1 Euro', 100)
note8 = Money('2 Euro', 200)

# Definition der Produkte in der Maschiene

item1 = Product('Cola', 1.99)
item2 = Product('Pepsi', 2.99)
item3 = Product('Mars', 4.59)
item4 = Product('Limo', 2.39)
item5 = Product('Sandwich', 5.29)
item6 = Product('Emty', 0.00)
item7 = Product('Emty', 0.00)
item8 = Product('Emty', 0.00)

kill = False

def coin_input(item_price):
    money_input = 0
    while item_price > money_input:
        print('Eingeworfenes Geld ist: '+ str(float(money_input) / 100) + '€')
        print('Preis ist: ' + str(float(item_price) / 100) +'€')
        print('Bitte Münzen einwerfen')
        coin_listing = "\n".join("{} \t\t\t{}".format(x, y) for x, y in zip(numbers_list, money_names))
        print(coin_listing)
        number_input = int(input('Bitte Münze auswählen:'))

        try:
            if number_input == 8:
                money_input = money_input + note1.worth
            elif number_input == 7:
                money_input = money_input + note2.worth
            elif number_input == 6:
                money_input = money_input + note3.worth
            elif number_input == 5:
                money_input = money_input + note4.worth
            elif number_input == 4:
                money_input = money_input + note5.worth
            elif number_input == 3:
                money_input = money_input + note6.worth
            elif number_input == 2:
                money_input = money_input + note7.worth
            elif number_input == 1:
                money_input = money_input + note8.worth
            else:
                print('Ungültige Eingabe!')
        except:
            print('Ungültige Eingabe!')
    return int(money_input)

money_names.reverse()
money_worths.reverse()





# Verkaufsdialog und Schleife
while not kill:
    print('Guten Tag, was möchten Sie kaufen?')
    answer = input('1. Produktliste \n2. Verlassen\n')
    try:
        answer = int(answer)
        if answer == 1:
            Product.product_call()

            product_select = input('Was möchten Sie haben?')
            try:
                product_select = int(product_select)
                if product_select == 1:
                    print('Die ' + str(item1.product_name) + ' kostet ' + str(item1.price))
                    Money.money_return(coin_input(Product.price_is(item1)), Product.price_is(item1))
                elif product_select == 2:
                    print('Die ' + str(item2.product_name) + ' kostet ' + str(item2.price))
                    Money.money_return(coin_input(Product.price_is(item2)), Product.price_is(item2))
                elif product_select == 3:
                    print('Die ' + str(item3.product_name) + ' kostet ' + str(item3.price))
                    Money.money_return(coin_input(Product.price_is(item3)), Product.price_is(item3))
                elif product_select == 4:
                    print('Die ' + str(item4.product_name) + ' kostet ' + str(item4.price))
                    Money.money_return(coin_input(Product.price_is(item4)), Product.price_is(item4))
                elif product_select == 5:
                    print('Die ' + str(item5.product_name) + ' kostet ' + str(item5.price))
                    Money.money_return(coin_input(Product.price_is(item5)), Product.price_is(item5))
                elif product_select == 6:
                    print('Die ' + str(item6.product_name) + ' kostet ' + str(item6.price))
                    Money.money_return(coin_input(Product.price_is(item6)), Product.price_is(item6))
                elif product_select == 7:
                    print('Die ' + str(item7.product_name) + ' kostet ' + str(item7.price))
                    Money.money_return(coin_input(Product.price_is(item7)), Product.price_is(item7))
                elif product_select == 8:
                    print('Die ' + str(item8.product_name) + ' kostet ' + str(item8.price))
                    Money.money_return(coin_input(Product.price_is(item8)), Product.price_is(item8))
                else:
                    print('Bitte mit gültiger Zahl antworten!')
            except:
                print('Falsche eingabe!')

        elif answer == 2:
            kill = True
        else:
            print('Ungültige Eingabe!')
    except:
        print('Bitte antworten Sie mit einer Zahl!')

print('Vielen Dank für Ihren besuch!')
