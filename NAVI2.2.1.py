import time
import os
import datetime
from colorama import init, Fore, Style
import phonenumbers
from phonenumbers import geocoder, carrier, timezone
import requests
import random
from tabulate import tabulate
import sys
from ipwhois import IPWhois

init()
y = Fore.YELLOW
g = Fore.GREEN
m = Fore.MAGENTA
b = Fore.BLUE
r = Fore.RED
c = Fore.CYAN
w = Fore.WHITE
br = Style.BRIGHT
df = Style.NORMAL
dim = Style.DIM
def N():
    print(f'''{dim}{b}
 ███▄    █  ▄▄▄    ██▒   █▓ ██▓
 ██ ▀█   █ ▒████▄  ▓██░   █▒▓██▒
▓██  ▀█ ██▒▒██  ▀█▄ ▓██  █▒░▒██▒
▓██▒  ▐▌██▒░██▄▄▄▄██▒██ █░░░██░
▒██░   ▓██░ ▓█   ▓██▒▒▀█░  ░██░
░ ▒░   ▒ ▒  ▒▒   ▓▒█░░ ▐░  ░▓  
░ ░░   ░ ▒░  ▒   ▒▒ ░░ ░░   ▒ ░
   ░   ░ ░   ░   ▒     ░░   ▒ ░
         ░       ░  ░   ░   ░                      {br}                                                            
{c}{df}-====={b}[{br}{w}NAVI-2.2.1{df}{b}]{c}=====-{br}
{b}[{c}Author{b}]{w} t.me/projectgd23c
{b}[{c}INFO{b}]{w} Перепродажа под запретом, все вопросы к разработчику
''')

def generate_random_ip():
    ip = ".".join(str(random.randint(0, 255)) for _ in range(4))
    return ip

def get_username():
    txt = f'{br}{c}[NAVI] Введите имя пользователя: {df}'
    for i in txt:
        time.sleep(0.1)
        print(i, end='', flush=True)
    username = input()
    with open('Navisdata.txt', 'w') as file:
        file.write(username)
    return username

def get_greeting(name):
    current_time = datetime.datetime.now().time()
    if current_time < datetime.time(12, 0):
        txt = f"{br}{b}[{c}NAVI{b}]{w} Доброе утро, {name}\nВас приветствует ассистент NAVI{df}\n"
    elif current_time < datetime.time(18, 0):
        txt = f"{br}{b}[{c}NAVI{b}]{w} Добрый день, {name}\nВас приветствует ассистент NAVI{df}\n"
    else:
        txt = f"{br}{b}[{c}NAVI{b}]{w} Добрый вечер, {name}\nВас приветствует ассистент NAVI{df}\n"
    
    for i in txt:
        time.sleep(0.01)
        print(i, end='', flush=True)

def Choose():
    an = f'''
{br}{b}[{w}1{b}]{c} ПОИСК ПО IP
{br}{b}[{w}2{b}]{c} ПОИСК ПО НОМЕРУ
{br}{b}[{w}3{b}]{c} ПОИСК ПО НИКУ
{br}{b}[{w}4{b}]{c} ПОИСК ПО ПОЧТЕ
{br}{b}[{w}5{b}]{c} SMS BOMBER
{br}{b}[{r}!{b}]{df}{r} Дисклеймер: Используйте эту утилиту ответственно и с уважением к частной жизни других людей.{br}'''
    
    print(an)

    inp = input(f'{br}{b}[{r}*{b}]{w} Номер функции: ')
    if inp == '1':
        time.sleep(0.1)
        print(f'{br}{b}[{r}?{b}]{w} Пример рандомного IP: ' + generate_random_ip())
        time.sleep(0.1)
        ip = input(f'{br}{b}[{r}+{b}]{w} Введите IP-адрес: ')
        

        ipinfo = find_ip_info(ip)
        time.sleep(0.06)
        print(f'{br}{b}[{r}*{b}]{w} Информация найденная по данному айпи адресу: \n{c}{ipinfo} \n By NAVI 2.2.1')
        time.sleep(2)
        ask = input(f'{br}{b}[{r}?{b}]{w} Вернутся в главное меню? Y/N: ')
        if ask == 'Y':
            time.sleep(1)
            N()
            Choose()
    if inp == '2':
        time.sleep(0.1)
        print(f'{br}{b}[{r}?{b}]{w} Пример рандомного RU номера: ' + generate_random_number())
        time.sleep(0.1)
        numb = input(f'{br}{b}[{r}+{b}]{w} Введите номер телефона: ')
        time.sleep(0.06)
        numbinfo = find_phone_info(numb)
        print(f'{numbinfo} \n By NAVI 2.2.1')
        time.sleep(2)
        ask = input(f'{br}{b}[{r}?{b}]{w} Вернутся в главное меню? Y/N: ')
        if ask == 'Y':
            time.sleep(1)
            N()
            Choose()
    if inp == '3':
        time.sleep(2)
        print(f'{br}{b}[{r}!{b}]{df}{r} https://github.com/sherlock-project/sherlock.{br}')
        time.sleep(3)
        ask = input(f'{br}{b}[{r}?{b}]{w} Вернутся в главное меню? Y/N: ')
        if ask == 'Y':
            time.sleep(1)
            N()
            Choose()
    if inp == '4':
        time.sleep(2)
        print(f'{br}{b}[{r}!{b}]{df}{r} https://github.com/megadose/holehe.{br}')
        time.sleep(3)
        ask = input(f'{br}{b}[{r}?{b}]{w} Вернутся в главное меню? Y/N: ')
        if ask == 'Y':
            time.sleep(1)
            N()
            Choose()
    if inp == '5':
        time.sleep(2)
        print(f'{br}{b}[{r}!{b}]{df}{r} https://mega.nz/file/pnV0EAKY#iSipMDV5DYVpalm4w45TDxDzXovpB3JFa9FgPOwddSY.{br}')
        time.sleep(3)
        ask = input(f'{br}{b}[{r}?{b}]{w} Вернутся в главное меню? Y/N: ')
        if ask == 'Y':
            time.sleep(1)
            N()
            Choose()

def Navi():
    try:
        with open('Navisdata.txt', 'r') as file:
            name = file.read()
    except FileNotFoundError:
        name = get_username()
    N()
    get_greeting(name)
    Choose()
    time.sleep(10)

def find_phone_info(phone_number):
    try:
        parsed_number = phonenumbers.parse(phone_number, None)
        if not phonenumbers.is_valid_number(parsed_number):
            return "Недействительный номер телефона"
        
        region_info = phonenumbers.geocoder.description_for_number(parsed_number, "ru")
        carrier_info = phonenumbers.carrier.name_for_number(parsed_number, "en")

        country = phonenumbers.geocoder.description_for_number(parsed_number, "en")
        region = phonenumbers.geocoder.description_for_number(parsed_number, "ru")
        formatted_number = phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
        is_valid = phonenumbers.is_valid_number(parsed_number)
        is_possible = phonenumbers.is_possible_number(parsed_number)
        timezona = timezone.time_zones_for_number(parsed_number)
        data = [
            [f"{br}{b}[{r}*{b}]{w} ИНФОРМАЦИЯ ПО НОМЕРУ:", formatted_number],
            [f"Страна", country],
            [f"Регион", region],
            [f"Оператор", carrier_info],
            [f"Активен?", is_valid],
            [f"Валид?", is_possible],
            [f"{br}{b}[{r}*{b}]{w} СОЦИАЛЬНЫЕ СЕТИ", ""],
            [f"Telegram", f"https://t.me/{phone_number}"],
            [f"Whatsapp", f"https://wa.me/{phone_number}"],
            [f"Viber", f"https://viber.click/{phone_number}"],
        ]
        
        table = tabulate(data, headers=["Инфа", "Результат"], tablefmt="pretty")
        
        return table
    except phonenumbers.phonenumberutil.NumberFormatException:
        return "Ошибка в формате номера телефона"
    except Exception as e:
        return f"Произошла ошибка: {str(e)}"
def find_ip_info(ip_address):
    try:
        vpn_check_url = f"https://ipinfo.io/{ip_address}/json"
        vpn_check_response = requests.get(vpn_check_url)
        vpn_check_data = vpn_check_response.json()
        is_vpn_or_proxy = vpn_check_data.get("vpn", False)

        ipwhois = IPWhois(ip_address)
        whois_info = ipwhois.lookup_rdap()

        asn_info = whois_info.get("asn_description", "N/A")
        location = whois_info.get("network", {}).get("cidr", "N/A")

        data_list = [
            ["Инфа", "Результат"],
            ["IP адрес", ip_address],
            ["VPN/Прокси", "Да" if is_vpn_or_proxy else "Нет"],
            ["ASN", whois_info.get("asn") or "N/A"],
            ["Организация", asn_info or "N/A"],
            ["Страна", whois_info.get("asn_country_code") or "N/A"],
            ["Whois", whois_info.get("raw") or "N/A"],
            ["Местоположение", location or "N/A"]
        ]

        formatted_table = ""
        for row in data_list:
            formatted_table += f"{row[0]:<15}: {row[1]}\n"

        return formatted_table

    except requests.RequestException as e:
        return f"Произошла ошибка при запросе: {str(e)}"
    except Exception as e:
        return f"Произошла ошибка: {str(e)}"
aperatori = {
    "МТС": ["910", "915", "916", "917", "919", "985", "986"],
    "билайн": ["903", "905", "906", "909", "962", "963", "964", "965", "966", "967", "968", "969", "980", "983", "986"],
    "МегаФон": ["925", "926", "929", "936", "999"],
    "Теле2": ["901", "958", "977", "999"]
}

def generate_random_number():
    operator = random.choice(list(aperatori.keys()))
    prefix = random.choice(aperatori[operator])
    number = ''.join([random.choice('0123456789') for _ in range(7)])
    return f"+7{prefix}{number}"
if __name__ == "__main__":
    Navi()
