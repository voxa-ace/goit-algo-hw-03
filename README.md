# Копіювання та сортування файлів за розширенням

Ця програма дозволяє копіювати файли з вихідної директорії в нову директорію і сортувати їх за розширенням.

## Вимоги

Перед використанням цієї програми вам потрібно встановити Python 3.

## Встановлення

1. Завантажте цей репозиторій на свій комп'ютер або склонуйте його за допомогою Git:

git clone https://github.com/voxa-ace/goit-algo-hw-03.git

## Використання

Для використання програми слід виконати наступні кроки:

1. Відкрийте командний рядок або термінал.

2. Запустіть програму з командними аргументами. Ось приклад команди:


Замініть `/шлях/до/вихідної/директорії` на шлях до вашої вихідної директорії і, за бажанням, `/шлях/до/директорії/призначення` на шлях до директорії, куди ви хочете скопіювати файли. Якщо ви не вказали опцію `--dest`, файли будуть скопійовані в папку `dist` у поточній робочій директорії.

3. Програма автоматично скопіює файли з вихідної директорії в папки, які відповідають їхнім розширенням. Наприклад, файли з розширенням `.txt` будуть скопійовані в папку `txt`, а файли без розширення в папку `no_extension`.

4. Готово! Ваші файли тепер скопійовані та впорядковані за розширенням у вказаній директорії.
