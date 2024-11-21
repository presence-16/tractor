def division(num1 , num2):
    try:
        if num2 != 0:
         return num1/num2
    except ZeroDivisionError:
      print('division by 0 is not allowed')
         