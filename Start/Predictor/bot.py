from aiogram import Bot, Dispatcher, executor, types
#import pyowm

import requests

bot = Bot(token="5405042618:AAE9gcNt-f8QUU3mMainIBLbEWziT_jc-2s")
dp = Dispatcher(bot)

open_weather_token = '413e8c3f51ab55346179afbbdc814f29'


#owm = pyowm.OWM('413e8c3f51ab55346179afbbdc814f29')
#la = owm.three_hours_forecast('Moscow, RU')
#print(la.will_have_clouds())

type_weather = {
    "Clear": "Ясно",
    "Clouds": "Облачно",
    "Rain": "Дождь",
    "Drizzle": "Дождь",
    "Thunderstorm": "Гроза",
    "Snow": "Снег ",
    "Mist": "Туман"}

dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await bot.send_message(message.from_user.id, 'Привет!\nЯ бот-предсказатель погоды. Просто отправь мне название города, а я подскажу, что Вам надеть :)')

dp.message_handler(content_types=["text"])
async def do_something(message: types.Message):
    try:
        r = requests.get(
            f"https://openweathermap.org/weathermap?basemap=map&cities=true&layer=temperature&lat=30&lon=-20&zoom=5={message.text}&appid={open_weather_token}&units=metric"
        )
        data = r.json()

        temp = data['main']['temp'] # Температура

        # Проверяем, есть ли тип погоды в словаре
        if data["weather"][0]["main"] in type_weather:
            wd = type_weather[data["weather"][0]["main"]]
        else:
            wd = ""

        # Есть ли дождь или нет
        if wd == 'Дождь':
            umbrl = 'и возьмите зонт'
        else:
            umbrl = ''

        # Определяем по температуре, что нам нужно надевать
        if temp < 1:
            result = 'Наденьте пальто и демисезонные сапоги'
        elif temp < 13:
            result = 'Прохладно, наденьте куртку'
        elif temp < 17:
            result = 'Тепло.Захватите ветровку, наденьте джинсы и джемпер'
        else:
            result = 'На улице жарко, самое время доставать теплые вещи'

        await bot.send_message(message.from_user.id, f"{result} {umbrl} ({data['main']['temp']}C° {wd})")

    except Exception as ex:
        await bot.send_message(message.from_user.id, "Проверьте название города")
        
executor.start_polling(dp)