import phonenumbers
from phonenumbers import format_number, PhoneNumberFormat
from phonenumbers.phonenumberutil import NumberParseException 
import re 

def normalize_phone(phone_number: str) -> str:
   
    cleaned_phone = re.sub(r'[^0-9+]', '', phone_number)
    
    if cleaned_phone.count('+') > 1 or (cleaned_phone.count('+') == 1 and not cleaned_phone.startswith('+')):
         cleaned_phone = cleaned_phone.replace('+', '')

    try:
        parsed_number = phonenumbers.parse(cleaned_phone, "UA") 

        if phonenumbers.is_valid_number(parsed_number):
            return format_number(parsed_number, PhoneNumberFormat.E164)
        
        else:
            return f"Невалидный номер: {phone_number}"

    except NumberParseException as e:
        return f"Ошибка парсинга ({e}): {phone_number}"


raw_numbers = [
    "067\\t123 4567",         
    "(095) 234-5678\\n",      
    "+380 44 123 4567",       
    "380501234567",           
    "     0503451234",        
    "(050)8889900",           
    "38050-111-22-22",        
    "+49 30 12()345678"       
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]

print("Нормализованные международные номера телефонов:")
for num in sanitized_numbers:
    print(num)


print("Нормализованные номера телефонов для SMS-рассылок:")
for num in sanitized_numbers:
    print(num)
