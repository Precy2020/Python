def your_vat():
    try:
        price, VAT = eval(input("Enter your price and VAT both seperated by comma: "))
        result = (price * VAT / 100) + price
        print(result)
    except SyntaxError:
        print('Enter a comma number seperated numbers ')
        your_vat()
    except ZeroDivisionError:
        print('Not able to divide by zero ')
        your_vat()
    except TypeError:
        print('Not recognised ')
        your_vat()
    except ValueError:
        print('Not recognised')
        your_vat()
    except NameError:
        print('Not recognised ')
        your_vat()
    else:
        print('Thank you for using my calculator ')
    finally:
        print('You are great!!! ')


your_vat()
