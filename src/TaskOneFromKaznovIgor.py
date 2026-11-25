def validate_password(password: str):

    errors = [];

    password = password.replace(" ", "")
    if len(password) < 8:
        errors.append("Длина пароля не менее 8 символов")
    if not any(c.isupper() for c in password):
        errors.append("Нужна хотя бы одна заглавная буква")
    if not any(c.islower() for c in password):
        errors.append("Нужна хотя бы одна строчная буква")
    if not any(c.isdigit() for c in password):
        errors.append("Нужна хотя бы одна цифра")
    if not any(c in "!@#$%^&*" for c in password):
        errors.append("Нужен хотя бы один спецсимвол")

    if errors:
        raise ValueError(errors)

    return True

# validate_password('hellasdasdasd') # Exception
print(validate_password('heD2&llasdasdasd')) # true
#####################################################################################

logs = [
    "192.168.1.1 - - [01/Jan/2024] 'GET /index.html HTTP/1.1' 200",
    "10.0.0.5 - - [01/Jan/2024] 'POST /login.php HTTP/1.1' 404",
    "192.168.1.1 - - [01/Jan/2024] 'GET /admin/panel HTTP/1.1' 403",
    "10.0.0.5 - - [01/Jan/2024] 'GET /index.html HTTP/1.1' 200",
    "192.168.1.1 - - [01/Jan/2024] 'POST /login.php HTTP/1.1' 200",
]

def find_suspicious_activity(logs: list):
    scanners = []
    suspicious = []

    for log in logs:
        listLog = log.split()

        if listLog[-1] == '404':
            scanners.append(listLog[0])

        if listLog[-1] == '403':
            suspicious.append(listLog[0])

        uniqueScanners = list(dict.fromkeys(scanners))
        uniqueSuspicious = list(dict.fromkeys(suspicious))

    return {"scanners" : uniqueScanners, "suspicious": uniqueSuspicious}

print(find_suspicious_activity(logs)) #{'scanners': ['10.0.0.5'], 'suspicious': ['192.168.1.1']}

#####################################################################################
ALLOWED_PORTS = {21, 22, 80, 443, 3389}
SUSPICIOUS_PORTS = {23, 135}

def scan_ports(port: int):
    textReturn = None

    if port in SUSPICIOUS_PORTS:
        textReturn = f'Port {port} is OPEN and considered VULNERABLE!'

    if port in ALLOWED_PORTS:
        textReturn = f'Port {port} is OPEN.'

    if textReturn is None:
        textReturn = f'Port {port} is closed.'

    return textReturn


print(scan_ports(21)) # Port 21 is OPEN.
#############################################################################################


def create_user(username: str, password: str):
    user = {
        "username" : username,
        "password_hash" : hash(password),
        "failed_login_attempts" : 0,
        "is_locked" : False
     }

    return user


def authenticate_user(user: list, input_password: str):
    if user['is_locked']:
        returnText = 'Account locked'
    else:
        if user['password_hash'] == hash(input_password):
            user['failed_login_attempts'] = 0
            returnText = 'Login successful'

        if not user['password_hash'] == hash(input_password):
            user['failed_login_attempts'] += 1
            returnText = 'password invalid'

        if user['failed_login_attempts'] >= 3:
            user['is_locked'] = True

    return returnText;

user = create_user('Sam', 'qwerty')
print(authenticate_user(user, 'qwerty2'))
print(authenticate_user(user, 'qwerty2'))
print(authenticate_user(user, 'qwerty2')) #password invalid
print(authenticate_user(user, 'qwerty2')) #Account locked
