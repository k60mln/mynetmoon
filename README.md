# mynetmoon
Monitoring network hardware (HPE inc. or over) SNMP
Мониторинг сетевого оборудорвания с помощью SNMP

Приложение на Django для мониторинга активного сетевого оборудования (коммутаторов, свичей, маршрутизаторов, при желании можно немного редактировать код и добавить другое оборудование которое поддерживает протокол SNMP. 

Программу писал для учебных целей, защиту и аутентификацию бд отключал (кому нужно поправьте глобальные конфиги джанго), есть форма входа на сайт только для заранее созданных админов через админку (тоже все при желании можно сделать под себя, так как повторюсь проект был учебный).

Что умеет приложение? 

- учет активного сетевого оборудования;
- сортировка оборудования по категориям;
- поиск по имени устройства или по ip-адресу;
- добавление новых устройств и их редактирование;
- автоматическая проверка доступности устройства в сети в реальном времени;
- автоматическое заполнение полей информации устройства, данные берутся напрямую с устройства через протокол snmp;
- получение с устройства текущей конфигурации;
- получение информации по портам (интерфейсам);
- получение логов;
- хранение информации об устройстве, логов и конфигурации в бд;
- резервное копирование (бекап устройств) и журнал событий со всех устройств;


Подходит для сетевых администраторов для мониторинга оборудования и получения быстрого доступа к логам (для траблшутинга), также бекапа устройств (автоматически раз в 24ч.), snmp значения установлены для устройств компании HPE т.к. у меня в компании 90% устройств были от них, при желании мрожно добавить кусок небольшого кода для универсальности, или изменить значения snmp для своих устройств.

Для установки закинуть папку в pycharmproject, установить django и остальные программные пакеты которые потребуются, так же установить БД, в коде прописана postgress, вы можете поменять на свою.



--------------------ENG-------------------- 

Monitoring network equipment using SNMP

A Django application for monitoring active network equipment (switches, switches, routers, if you wish, you can edit the code a little and add other equipment that supports the SNMP protocol.

I wrote the program for educational purposes, turned off the protection and authentication of the database (who needs to correct the global django configs), there is a login form for the site only for pre-created admins through the admin panel (you can also do everything if you wish, for yourself, since I repeat the project was educational).

What can the application do?

- accounting of active network equipment;
- sorting equipment into categories;
- search by device name or ip-address;
- adding new devices and editing them;
- automatic check of device availability in the network in real time;
- automatic filling of device information fields, data is taken directly from the device via the snmp protocol;
- receiving the current configuration from the device;
- obtaining information on ports (interfaces);
- receiving logs;
- storage of information about the device, logs and configuration in the database;
- backup (device backup) and event log from all devices;


Suitable for network administrators to monitor equipment and get quick access to logs (for troubleshooting), also backup devices (automatically once every 24 hours), snmp values are set for HPE devices. in my company, 90% of the devices were from them, if you wish, you can add a piece of small code for universality, or change the snmp values ​​for your devices.

To install, drop the folder into pycharmproject, install django and the rest of the software packages that you need, also install the database, postgress is written in the code, you can change it to your own.
