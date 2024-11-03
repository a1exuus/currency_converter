# Бот для конвертации валют

## Содержание

- [Введение](#введение)
- [Начало работы](#начало-работы)
- [Цель проекта](#цель-проекта)
- [FAQ](#faq)

## Введение

В репозитории который вы просматриваете имееться два файла: `bot.py` `calculations.py`

Они выполняют разные функции: в файле `bot.py` находиться бот. Именно этот файл является основным и именно его нужно запускать для корректной работы программы. В тоже время, файл `calculations.py` является своего рода самописной библиотекой, используящая сервис *ExchangeRate-API*. Этот сервис требует свой API-ключ, поэтому в проекте оставлен файл `.env`. О нём речь будет идти далее.

Проект был написан на библиотеке `telebot`, а также использует такие библиотеки как `python-dotenv`, `requests` и др.

Если при работе с программой возникли проблемы, просмотрите [часто задаваемые вопросы](#faq), возможно там вы найдете решение своей проблемы.

## Начало работы

Для начала работы установите зависимости(библиотеки) проекта следующей командой:

```pip install -r requirements.txt```

Также для корректной работы программы в файл `.env` запишите токен вашего Telegram-бота и ваш API-ключ к вышеупомянутому сервису. Пример правильно записи:

```TG_BOT_TOKEN=ваш токен # Обязательно записывайте именно под ключом TG_BOT_TOKEN!!!!  API_KEY=ваш API-ключ # Снова записывайте именно под этим ключом!!!!!``` 

## Цель проекта

Проект был создан для соревнований между программистами "**Хакатон**". Соревнования проводились в школе программирования при IT-компании "***Бюро 20***" в ноябре 2024 года.

## FAQ

### Почему именно этот сервис?

Потому-что за неимением других бесплатных альтернатив, я прибег к использованию именно этого сервиса.

### Почему я должен вводить сам API-ключ и токен бота?!

Запись секретного ключа - **обязательный процесс**. Но почему же?

Всё потому что разработчик, не хочет что-бы его секретный ключ использовали для каких-то злодеяний. Поэтому убирает его из своего проекта. Секретные ключи ***обязательны*** для выполнения программы полностью. Также вы можете не бояться что ваш ключ украдут, так как программа выложена на [GitHub](https://github.com), то вы можете в любой удобный для вас момент убедиться что программа не содержит никакого вредоносного кода. Код открыт к чтению и может быть использован любым человеком.
