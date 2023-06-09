# Адаптация фильмов для людей с особыми потребностями

Адаптация фильмов для людей с особыми потребностями - это процесс изменения фильмов с целью удовлетворения потребностей людей с определенными видами ограничений в зрении и эпилепсии. Эта тема является важной в свете развития инклюзивного подхода в культуре и кинематографии, который стремится сделать фильмы доступными для всех, включая людей с особыми потребностями. Кинематограф как средство массовой информации должен быть доступен для всех, и адаптация фильмов для людей с эпилепсией и дальтонизмом является важным шагом в этом направлении

Алгоритм автоматически находит массив отрезков, которые могут вызвать эпилептический припадок, сохраняет их в базу данных. При просмотре фильма подгружается этот массив и во время просмотра в нужные моменты применяет фильтр, изменяющий значение яркости и контрастности картинки во время просмотра на определённых интревалах. Кроме того, мы предоставляем возможность выбора пресетов *для эпилептиков и дальтоников*, что позволяет пользователям настроить просмотр под свои потребности. 
 
# Инструкция по развёртке

Установка postgresql + python3.11 + requirements.txt

git clone https://github.com/sloonak/truetechhack_mgotu.git 

cd repo

pip install virtualenv (если у вас еще не установлен)

virtualenv venv to create your new environment

source venv/bin/activate для входа в виртуальную среду

pip install -r requirements.txt  для установки требований в текущей среде

# Функционал

1. Алгоритм, который анализирует видеоряд на наличие отрывков, способных вызвать эпилептический припадок.

2. Фильтры для людей с особым восприятием цвета, таких как дальтонизм и различные его виды:

- Протанопия — отсутствие восприятие красного цвета.

- Дейтеранопия — отсутствие восприятия зеленого цвета.

- Тританопия — отсутствие восприятие синего цвета.
3. Ручная смена яркости и контрастности в плеере.
4. Настройки у каждого пользователя сохраяются. При включение другого фильма или сериала подгружаются последение сохранённые настройки.

# Работа базы данных и сервера

Проект по анализу видео на предмет возможных эпилептических припадков и выявление параметров для коррекции яркости и контрастности.

## Структура базы данных

Используется база данных PostgreSQL с названием video_analyze, содержащая таблицу:

### Таблица video

Содержит следующие колонки:

1. id - идентификатор записи.
2. url - URL видео.
3. status - статус анализа видео (FAILED/OK).
4. data - сериализованный массив массивов, содержащий интервалы с потенциальными эпилептическими припадками.
5. datetime - время создания или последнего обновления записи.

## Алгоритм

Проект реализует следующий алгоритм:

1. Создается специальный сервис, который отправляет URL видео на сервер для анализа.
2. На сервере проводится анализ видео: выявляются интервалы, на которых возможны эпилептические припадки, и определяются основные параметры для коррекции яркости и контрастности.
3. Создается массив массивов с интервалами, сериализуется и добавляется в таблицу video.

## Установка и настройка

В этом разделе мы рассмотрим подробные шаги по установке и настройке проекта Video Analyze.

### 1. Установка и настройка PostgreSQL

1. Скачайте и установите PostgreSQL с официального сайта: https://www.postgresql.org/download/

2. Во время установки создайте пользователя и введите пароль для него. Запомните эти данные, так как они понадобятся для подключения к базе данных.

3. Откройте pgAdmin (графический интерфейс для работы с PostgreSQL) и подключитесь к серверу баз данных с использованием учетных данных пользователя.

4. Создайте новую базу данных с именем video_analyze.

### 2. Настройка сервера

git clone <repo> 

cd <repo>

pip install virtualenv (если у вас еще не установлен)

virtualenv venv to create your new environment

source venv/bin/activate для входа в виртуальную среду

pip install -r requirements.txt  для установки требований в текущей среде

### 2. Создание таблиц

1. В pgAdmin откройте базу данных video_analyze.

2. Создайте таблицу video с помощью следующего SQL-запроса:

sql
CREATE TABLE video (
    id SERIAL PRIMARY KEY,
    url VARCHAR(2048) NOT NULL,
    status VARCHAR(16) NOT NULL,
    data TEXT,
    datetime TIMESTAMP NOT NULL
);
Выполните запрос, чтобы создать таблицу.

3. Установка и настройка сервера анализа видео
Установите необходимые зависимости для работы с сервером анализа видео. Зависимости могут варьироваться в зависимости от используемой технологии и языка программирования. Некоторые из них могут включать:
FFmpeg для работы с видеофайлами
OpenCV для анализа видео
Библиотеки для работы с PostgreSQL
Настройте сервер анализа видео:
Создайте конфигурационный файл с параметрами подключения к базе данных video_analyze.
Настройте процесс анализа видео с использованием указанных зависимостей.
4. Развертывание и настройка сервиса отправки URL
Разработайте специальный сервис, который принимает URL видео и отправляет его на сервер анализа видео. Сервис может быть реализован с использованием различных технологий, таких как Flask, Django, Express.js и других.

Настройте сервис, указав адрес сервера анализа видео.

Разверните сервис на сервере или платформе вроде Heroku, AWS, Google Cloud и других.

5. Тестирование
Проверьте работу вашего проекта, отправив URL видео на специальный сервис. Убедитесь, что сервер анализа видео корректно обрабатывает видео и сохраняет результаты в базе данных.

После успешного тестирования ваш проект будет готов к использованию.

### 3. Использование

Теперь, когда ваш проект установлен и настроен, вы можете использовать его для анализа видео на предмет возможных эпилептических припадков и выявления параметров для коррекции яркости и контрастности.

1. Отправляйте URL видео на специальный сервис. Сервис отправит URL на сервер анализа видео.
2. Сервер анализа видео будет обрабатывать видео, выявлять интервалы с потенциальными эпилептическими припадками и определять параметры для коррекции яркости и контрастности.
3. Результаты анализа будут сохраняться в таблице video базы данных video_analyze.
4. Вы можете запросить данные из таблицы video и использовать их для принятия решений о коррекции яркости и контрастности видео или предупреждения пользователей о возможных рисках для здоровья.

# Алгоритм анализа видео на выявление интервалов, представляющие потенциальный риск для эпилепсии

Мы считываем видеофайл и получаем общее количество файлов в этом видеофайле. Создаём функцию, которая будет высчитываеть интервалы представляющие риск для приступов эпилепсии. Функция будет принимать значения: начала фрейма и среднее значение яркости и контрастности. Далее мы создаём ещё одну функцию, которая перебирает все кадры видео и высчитывает их контрастность и яркость. 

Создаём функцию для расчета средней яркости и контрастности для всех кадров с использованием многопоточности и функции executor.map(). 

Создаём ещё одну функцию, которая будет обрабатывать яркость и контрастность для одного (текущего) кадра. 

Создаём модуль, который проверяет превышает ли контрастность и яркость среднее значения. По результатам этого модуля, если существует текущий интервал, добавляем его в список.

Создаём ещё одну функцию для обработки сегмената видео и поиска интервалов с потенциальными риском для приступов эппилепсии. На вход поспутает сегмент начала, сегмент конца и средную контрастность и яркость. 

Обработка каждого сегмента видео с инспльзовнием многопоточности и функции executor.submit()

В рамках этого процесса:

1. Открывается локальный видеопоток для сегмента
2. Чтение и обаработка кадров сегмената, включая вычисление яркости и контрастности
3. Запуск функции анализа кадров, которая определяет интервалы с высокими значениями яркости и контрастности, превышающими средние
4. Закрытие локального видеопотока

Сбора всех найденных интервалов с потенциальным приступом эпилепсии в единый список и преобразование индексов кадров во временные метки(в секундах)

Форматирование данных об интервалах в удобный вид для вывода и вывод данных.

Закрытие главного видеопотока(cap.release())

## Важные элементы
### Многопоточность
Многопоточность реализована с использованием модуля concurrent.futures, который предоставляет высокоуровневый интерфейс для асинхронного выполнения вызовов. В данном коде используется класс ThreadPoolExecutor для создания пула потоков.

Вычисление яркости и контрастности для всех кадров видео:

with concurrent.futures.ThreadPoolExecutor() as executor:
    frame_results = list(executor.map(process_frame_brightness_contrast, read_frames(cap)))
Здесь создается пул потоков, который автоматически будет закрыт после выполнения блока with. Функция executor.map принимает на вход функцию process_frame_brightness_contrast и итерируемый объект read_frames(cap), который представляет собой кадры видео. Функция process_frame_brightness_contrast вызывается для каждого кадра, а результаты собираются в список frame_results.

### Обработка сегментов видео

with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
    for i in range(num_threads):
        segment_start = i * segment_duration
        segment_end = (i + 1) * segment_duration if i < num_threads - 1 else total_frames
        futures.append(executor.submit(process_video_segment, segment_start, segment_end, avg_brightness, avg_contrast))
Здесь создается пул потоков с заданным количеством рабочих потоков num_threads. В цикле разбиваем видео на сегменты и вызываем функцию process_video_segment для каждого сегмента с помощью метода executor.submit. Результатом этой функции является объект concurrent.futures.Future, который добавляется в список futures

### Получение результатов из Future-объектов:

with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
    for i in range(num_threads):
        segment_start = i * segment_duration
        segment_end = (i + 1) * segment_duration if i < num_threads - 1 else total_frames
        futures.append(executor.submit(process_video_segment, segment_start, segment_end, avg_brightness, avg_contrast))
 

Здесь создается пул потоков с заданным количеством рабочих потоков num_threads. В цикле разбиваем видео на сегменты и вызываем функцию process_video_segment для каждого сегмента с помощью метода executor.submit. Результатом этой функции является объект concurrent.futures.Future, который добавляется в список futures.

# Описание функционала на Frontend
Данный проект реализует следующий функционал на клиентской стороне.

## Плеер и кнопки
На странице имеется плеер для воспроизведения видео. У плеера есть две кнопки - для режима эпилептика и дальтоника.

## Эпилептический режим
При включении режима эпилептика, на видеоплеер из базы данных отправляются промежутки (интервалы), на которых может возникнуть приступ эпилепсии. Вместе с этими промежутками отсылаются рекомендованные значения яркости и контрастности, которые необходимо установить на этом интервале.

Далее на основе полученной информации, на странице создается маска на основе элемента canvas, которая автоматически изменяет контрастность и яркость в указанные интервалы видео.

При нажатии на первую кнопку создается canvas поверх контейнера. При нажатии на вторую кнопку удаляется текущий canvas, создается новый, и открываются дополнительные кнопки для выбора типа дальтонизма. При нажатии на третью кнопку открывается диалоговое окно, в котором можно ввести значения яркости и контрастности.

Также у пользователя есть возможность вручную регулировать яркость и контрастность с помощью ползунков, чтобы обеспечить максимально комфортное и безопасное восприятие контента.
## Дальтонический режим
При включении режима дальтоника, на видео накладывается маска для различных видов дальтонизма. Вид маски можно выбрать самостоятельно.

Благодаря реализованному функционалу, наш плеер обеспечивает безопасный, комфортный и доступный просмотр видео для всех пользователей, включая людей с особыми потребностями.


# Масштабирование анализа видео для определения эпилептических рисков
Данный код может быть использован для анализа видео на предмет эпилептических рисков. В текущей реализации используется многопоточность, однако можно масштабировать процесс анализа, распределяя задачи на множество ядер или компьютеров. Вот несколько предложений по масштабированию данного кода:

## Расширение на многопроцессорные системы
Для использования мощности многопроцессорных систем можно заменить ThreadPoolExecutor на ProcessPoolExecutor из модуля concurrent.futures. Это позволит распараллелить задачи на разных ядрах процессора и получить более быстрое выполнение, особенно при анализе больших видеофайлов.

## Распределение задач на кластер компьютеров
Для выполнения анализа на кластере компьютеров можно использовать библиотеки, такие как Dask, Ray или Apache Spark. Они позволят распределить задачи на множество компьютеров, а также обрабатывать видеофайлы гораздо большего размера.

## Использование GPU
Для ускорения процесса обработки видео можно использовать GPU, которые предоставляют высокую параллельность и производительность. Библиотеки, такие как TensorFlow, PyTorch или CuPy, предоставляют возможности для обработки данных с использованием GPU.

## Оптимизация обработки видео
При масштабировании анализа видео также стоит учитывать различные методы оптимизации обработки видео, такие как использование аппаратного кодека для чтения видео, а также оптимизация алгоритмов для обработки изображений, чтобы уменьшить время выполнения задачи.
