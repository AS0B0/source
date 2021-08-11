a = [1,2,3]
try:
    print(a[2])
    4 / 0
except IndexError as e:
    print(e)
except ZeroDivisionError as e:
    print(e)

# except (IndexError, ZeroDivisionError) as e:
#   print(e) 같이도 쓸수있음
