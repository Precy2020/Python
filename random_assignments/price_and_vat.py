def your_vat():
    while True:
        try:
            price, VAT = eval(input("Enter your price and VAT both seperated by comma: "))
            result = (price * VAT / 100) + price
            print(result)
        except SyntaxError:
            print('Syntax Error ')
        except ZeroDivisionError:
            print('Zero Division Error ')
        except TypeError:
            print('Type Error')
        except ValueError:
            print('Value Error')
        except NameError:
            print('Name Error ')
        except KeyboardInterrupt:
            print('Please reason well!!')
        except EOFError:
            print('Why control D?? ')
        else:
            print('Thank you for using my calculator ')
            break
        finally:
            print('You are great!!! ')


your_vat()
