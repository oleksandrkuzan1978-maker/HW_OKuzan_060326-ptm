#!/bin/bash

# ping указанного адреса с интервалом 1 секунда между попытками.
# Если время пинга превышает 100 мс или не удается выполнить пинг
# в течение 3 последовательных отправок пакетов, скрипт сообщит об этом. 
#
#set -x

read -p "Enter IP address: " HOST  # ввод имени сервера с клавиатуры

failed=0  #  Создание счетчика  НЕудачных попыток отправок пакетов


while true

do
    echo
    echo "Monitoring host: $HOST"

    ping_result=$(ping -c 1 -W 1 "$HOST")  # отправка одного пакета (-c) на указанный адрес. на отправку дается не более 1 секунды (-W)

# если команда выполнилась успешно (установлена связь с удаленным сервером),
# то проверяем время пинга

    if [ $? -eq 0 ]
       then
          failed=0
          echo "$ping_result"

          # из информационной строки пинга достаем числовое значение времени пинга
          time_ms=$(echo $ping_result | awk -F'time=|ms' '{print $2}')

          # сравнение времени пинга со 100 мс (больше или меньше)
          comparison=$(awk "BEGIN {print ($time_ms > 100)}")  

          if [ "$comparison" -eq 1 ]  #если время пинга больше 100 мс

             then

                echo -e "\nWARNING: The ping time exceeds 100 ms.\n" 
             fi

    else  # если пинг не удалось выполнить то увеличивает значение счетчика на 1
        ((failed++))  #

        if [ "$failed" -eq 3 ]  # если число последовательных неудачных попыток = трем
           then
	    
              echo -e "\nERROR: Ping failed for 3 consecutive packet transmissions.\n"
	    
              failed=0
           fi
    fi

    sleep 1
done
