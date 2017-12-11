import socket

#Функция для определения сетевого ip-адреса на компьютере
def Inforamtion_of_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(('mail.ru', 80))
    print('Ip-адрес данного компьютера: '+ s.getsockname()[0])
    s.close()
Inforamtion_of_ip()





