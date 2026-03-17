"""print("enter year to check")
n=int(input("year"))
def leapyear(n):
  if n % 4 == 0 and n % 100 != 0 :
    print("year{n}, is a leap year")
  elif n % 400 == 0 :
    print("year{n} , is a leap year")
  else:
    print("year {n}, is not a leap year")

leapyear(n)


"""






# optional range check (uncomment if you want bounds validation)
# year must be between 1900 and 100000 inclusive
# year = int(input('Enter year: '))
# if not (1900 <= year <= 10**5):
#     raise ValueError('year out of bounds')


def is_leap(year):
  if year % 400 == 0:
    return True
  elif year % 100 == 0:
    return False
  elif year % 4 == 0:
    return True
  else:
    return False


year = int(input())
print(is_leap(year))