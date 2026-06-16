#!/bin/bash
#
# Дирректория в которой создаются 100 файлов
DIR="/opt/060326-ptm/kuzan/HW_19/erst"

# Очищаем директорию (подготавливаем для новой партии из 100 файлов)
rm -f "$DIR"/*.* 

for i in {1..100}
do
touch "$DIR/$RANDOM".txt
done

