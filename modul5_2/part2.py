try:
    x
    1 / 0
except (IndexError, ArithmeticError):
    print('we have division by 0')
    raise
except NameError:
    print('no variable')
else:
    print('division success in else')