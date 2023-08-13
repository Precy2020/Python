# def exception():
#     try:
#         num1, num2 = eval(input('Enter two numbers seperated by comma: '))
#         result = num1 / num2
#         print(result)
#     except SyntaxError:
#         print('Enter a number seperated numbers ')
#         exception()
#     except ZeroDivisionError:
#         print('Not able to divide by zero ')
#         exception()
#     except TypeError:
#         print('Not recognised ')
#         exception()
#     else:
#         print('Thank you for using my calculator ')
#     finally:
#         print('Terrorise')


# exception()

while True:
    try:
        num1, num2 = eval(input('Enter two numbers seperated by comma: '))
        result = num1 / num2
        print(result)
    except SyntaxError:
        print('Enter a number seperated numbers ')
    except ZeroDivisionError:
        print('Not able to divide by zero ')
    except TypeError:
        print('Not recognised ')
    except ValueError:
        print('Not recognised')
    except NameError:
        print('Not recognised ')
    else:
        print('Thank you for using my calculator ')
        break
    finally:
        print('You are great!!! ')

