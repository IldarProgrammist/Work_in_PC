import socket
import getpass

#Функция Информация о компьютере
def Inforamtion_of_machine():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(('mail.ru', 80))
    print('Имя компьютера'+ socket.gethostname())
    print('Имя пользователя:' + getpass.getuser())
    print('Ip-адрес компьютера: '+ s.getsockname()[0])

    s.close()
Inforamtion_of_machine()





