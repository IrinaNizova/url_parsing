Для установки надо запустить скрипт startapp.sh, расположенный и корневой директории
Он:
- устанавливает модули из requirements.txt
- запускает процесс для очереди celery
- запускает сервер

Как пользоваться:
В админке http://127.0.0.1:8000/admin/sites/sites/ можно внести адрес сайт и временной сдвиг
Если зайти на главную страницу http://127.0.0.1:8000 мы увидим все внесённые сайты
При клике на url мы перейдём на страницу, где будут результаты парсинга
Если сайт ещё не обработан, будет информация об этом
