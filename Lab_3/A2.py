import string
password = input('Введите пароль: ')
is_norm = True
if len (password) != 8:
    print ('Длина пароля не равна 8')
    is_norm = False
if password.upper() == password:
    print ('В пароле отсутствуют строчные буквы')
    is_norm = False
if password.lower() == password:
    print ('В пароле отсутствуют заглавные буквы')
    is_norm = False
if not any(symbol.isdigit() for symbol in password):
    print ('В пароле отсутствуют цифры')
    is_norm = False
if not any(symbol in '*-#' for symbol in password):
    print ('В пароле отсутствуют специальные символы')
    is_norm = False

allowed = string.ascii_uppercase + string.ascii_lowercase + string.digits + '*-#'
if not all(symbol in allowed for symbol in password):
    print ('В пароле используются непредусмотренные символы')
    is_norm = False

if is_norm == True:
    print ('Надежный пароль')