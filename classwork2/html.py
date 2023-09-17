l1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
f = open('helloworld.html', 'w')

message = """ <html>
          <body>
          <head><title>PRECIOUS</title></head>
          <p>Your Details:</p>
          <form>
          Name: <br> <input type="text" name= "name">
          <br>
          Age: <br> <input type="text" name= "age">
          <br>
          sport: <br> <input type="text" name= "sport">
          </form>
          </body>
          </html>"""
f.write(message)
f.close()

