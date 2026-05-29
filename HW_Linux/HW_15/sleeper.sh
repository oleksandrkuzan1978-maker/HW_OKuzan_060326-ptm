#!/bin/bash

# Файл для записи информации о процессоре
CPU_INFO="/opt/060326-ptm/kuzan/cpu_info.txt"

# Файл для записи информации об операционной системе
OS_INFO="/opt/060326-ptm/kuzan/os_info.txt"

# Папка для записи и хранения 50 файлов
DIR="/tmp/KUZAN_HW_15_FILES"

mkdir -p $DIR


# Вывод текущего времени 10 раз и количества процессов одним числом
echo "ВЫвод текущего времени:"

for i in {1..10}
    do
    echo "Текущее время: $(date +%H:%M:%S) Количество процессов: $(ps -ef | wc -l)"

    sleep 0.3
    done

# Вывод количества процессов на экран
#echo -n "Количество процессов: "
#ps -ef | wc -l

# Запись информации о процессоре в мой файл
cat /proc/cpuinfo > "$CPU_INFO"


# Запись строки названия операционной системы в файл
grep "^NAME=" /etc/os-release > "$OS_INFO"

# Запись в файл только наименования ОС
grep "^NAME=" /etc/os-release | awk -F= '{print $2}' | tr -d '"' >> "$OS_INFO"


# Создание 50 файлов

for k in {50..100}
  do

    touch $DIR/$k.txt

  done






