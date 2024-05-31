import string
import getpass

def check_min_characters(password):
  result = len(password)>=8
  if not result:
    print("Enter 8 or more characters!")
  return result


def check_possible_symbols(password):
  result = all(character in string.printable and character not in string.whitespace
     for character in password)
  if not result:
    print("Use [a-z] alhpabet!")
  return result


def check_uppercase_symbol(password):
  result = any(character in string.ascii_uppercase for character in password)
  if not result:
    print("Use at least 1 uppercase letter!")
  return result


def check_digit(password):
  result = any(character in string.digits for character in password)
  if not result:
    print("Use at least 1 digit!")
  return result


def check_special_symbol(password):
  result = any(character in "!@#$%^&*()_+-=" for character in password)
  if not result:
    print("Use at least 1 special symbol!")
  return result


def check_password(password):
  min_chars = check_min_characters(password)
  possible_chars = check_possible_symbols(password)
  uppercase_symb = check_uppercase_symbol(password)
  digit = check_digit(password)
  special_symb = check_special_symbol(password)
  return bool (min_chars and possible_chars and uppercase_symb and digit and special_symb)


while True:
  password= getpass.getpass(prompt='Enter a password:')
  if check_password(password):
    print("A nice one, we won't tell it to anyone...")
    break
  else:
    print("Please, check the problems above")
    