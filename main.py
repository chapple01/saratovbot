from vkbottle.bot import Bot, Message
import json
import re
import random
import asyncio

with open('database.json', 'r', encoding="utf-8") as r:
  data = json.load(r)

bot = Bot(token="vk1.a.4YbTwBeSzReSI2uiUZjYu81K6Ax7Xc3h9mna_GTJhXhz2MitiRCCxDMEO9v1zouDq9hRgZnRewekGqIXozsUjAN7RyorMcUvLP7gk5J6lx-xHYFPPMVxuM_N9e1vBKzgwqOJm8gOC5Uo7MPEopUA9aMkbEfJ1GDY23_R6Tt93Si20vB2PUhZcWix0MOll3leQoYJeEgoW9cxvfGAwCA6ww")

@bot.on.chat_message(text=['/баллы <n>', '/баллы'])
async def balli(message: Message, n=None):
    if message.from_id == 499748580 or message.from_id == 24351886:
        if n is not None:
            if n == (f'+{abs(int(n))}'):
                balli = data["balli"]
                balli += int(n)
                await message.answer(f'Баллы были добавлены. ({n})\nВсего баллов: {balli}')
            elif n == (f'-{abs(int(n))}'):
                balli = data["balli"]
                balli += int(n)
                await message.answer(f'Баллы были отняты. ({n})\nВсего баллов: {balli}')
            else:
                await message.answer(f'Введите /баллы <баллы>')
            data["balli"] = balli
            saveJson()
        else:
            await message.answer(f'Введите /баллы <баллы>. Пример: /баллы +10')
    else:
        await message.answer(f'У вас нет прав!')



sobeska = False
sleep = 30

@bot.on.chat_message(text=['/собеска'])
async def sobes(message: Message):
    if message.from_id == 183337541:
        global sobeska
        global sleep
        members = data["offmem"]
        if sobeska == False:
            sobeska = True
            await message.answer(f'Лидер Саратова начал собеседование. Собеседование продлится 30 секунд.')
            while sleep > 0:
                await asyncio.sleep(1)
                sleep -= 1
            if sleep == 0:
                sobeska = False
                sleep = 30
                if members >= 0:
                    a = random.randint(0, 15)
                    members = members + a
                    await message.answer(f'Лидер Саратова провёл собеседование и набрал жителей ({a}).\nВсего жителей: {members}')
                    data["offmem"] = members
                    saveJson()
        else:
            await message.answer(f'Собеседование уже идёт ({sleep}).')
            

@bot.on.chat_message(text=['/нрпники'])
async def ystniyballi(message: Message, n=None):
    if message.from_id == 499748580 or message.from_id == 183337541:
        members = data["offmem"]
        if members >= 1:
            await message.answer(f'Запущена проверка Саратова на НРП ники.\nВсего жителей: {members}')
            await asyncio.sleep(5)
            a = random.randint(0, 20)
            if a > members:
                await message.answer(f'В Саратове у всех НРП ники. Расстрелено: {members}')
                members = 0
            else:
                members = members - a
                await message.answer(f'В Саратове у некоторых жителей ({a}) НРП ники.\nВсе они были расстрелены.\nВсего жителей: {members}')
            
            data["offmem"] = members
            saveJson()
        else:
            await message.answer(f'В Саратове нет жителей для проверки.')

@bot.on.chat_message(text=['/устныйзабаллы'])
async def ystniyballi(message: Message, n=None):
    if message.from_id == 183337541:
        ystnie = data["ystnie"]
        strogie = data["strogie"]
        balli = data["balli"]

        if strogie >= 1 and ystnie == 0:
            strogie -=1
            ystnie = 2
            balli -=35
            await message.answer(f'Лидер Саратова снял строгий за 35 баллов, так как устных 0/3.\nВсего устных: {ystnie}/3\nВсего строгих: {strogie}/3')
        elif ystnie <= 3 and ystnie != 0:
            ystnie -=1
            balli -=35
            await message.answer(f'Лидер Саратова снял устный за 35 баллов.\nВсего устных: {ystnie}/3')
        elif ystnie == 0 and strogie == 0:
            await message.answer(f'У Саратова нет устных и строгих.\nВсего устных: {ystnie}/3\nВсего строгих: {strogie}/3')
        
        data["balli"] = balli
        data["ystnie"] = ystnie
        data["strogie"] = strogie
        saveJson()
    else:
        await message.answer(f'У вас нет прав!')

@bot.on.chat_message(text=['/строгийзабаллы'])
async def ystniyballi(message: Message, n=None):
    if message.from_id == 183337541:
        ystnie = data["ystnie"]
        strogie = data["strogie"]
        balli = data["balli"]

        if strogie <= 3 and strogie != 0:
            strogie -=1
            balli -=75
            await message.answer(f'Лидер Саратова снял строгий за 75 баллов.\nВсего строгих: {strogie}/3')
        elif strogie == 0:
            await message.answer(f'У Саратова нет строгих.\nВсего устных: {ystnie}/3\nВсего строгих: {strogie}/3')
        
        data["balli"] = balli
        data["ystnie"] = ystnie
        data["strogie"] = strogie
        saveJson()
    else:
        await message.answer(f'У вас нет прав!')

@bot.on.chat_message(text=['/+<w>'])
async def ys_plus(message: Message, w=None):
    if message.from_id == 499748580 or message.from_id == 24351886:
        if w is not None:            
            ystnie = data["ystnie"]
            strogie = data["strogie"]
            if w == 'устный':
                if ystnie < 3:
                    ystnie +=1
                    await message.answer(f'Саратову был выдан устный.\nВсего устных: {ystnie}/3')
                    if strogie == 3 and ystnie == 3:
                        await message.answer(f'Саратов, у вас 3/3 устных | 3/3 строгих.')
                else:
                    if strogie < 3:
                        ystnie = 0
                        strogie +=1
                        await message.answer(f'Саратову был выдан строгий, так как устных 3/3.\nВсего устных: {ystnie}/3\nВсего строгих: {strogie}/3')
                        if strogie == 3:
                            await message.answer(f'Саратов, у вас 3/3 строгих.\n24 часа на снятие.')
                    else:
                        await message.answer(f'У Саратова и так 3/3 устных | 3/3 строгих.')
            if w == 'строгий':
                if strogie < 3:
                    strogie +=1
                    await message.answer(f'Саратову был выдан строгий.\nВсего строгих: {strogie}/3')
                    if strogie == 3:
                        await message.answer(f'Саратов, у вас 3/3 строгих.\n24 часа на снятие.')
                else:
                    await message.answer(f'У Саратова и так 3/3 строгих.')

            data["ystnie"] = ystnie
            data["strogie"] = strogie
            saveJson()
        else:
            await message.answer(f'Введите /помощь, чтобы посмотреть команды.')
    else:
        await message.answer(f'У вас нет прав!')

@bot.on.chat_message(text=['/-<w>', '/-'])
async def ys_minus(message: Message, w=None):
    if message.from_id == 499748580 or message.from_id == 24351886:
        ystnie = data["ystnie"]
        strogie = data["strogie"]
        if w is not None:
            if w == 'устный':
                if strogie >= 1 and ystnie == 0:
                    strogie -=1
                    ystnie = 2
                    await message.answer(f'Саратову был снят строгий, так как устных 0/3.\nВсего устных: {ystnie}/3\nВсего строгих: {strogie}/3')
                elif ystnie <= 3 and ystnie != 0:
                    ystnie -=1
                    await message.answer(f'Саратову был снят устный.\nВсего устных: {ystnie}/3')
                elif ystnie == 0 and strogie == 0:
                    await message.answer(f'У Саратова нет устных и строгих.\nВсего устных: {ystnie}/3\nВсего строгих: {strogie}/3')

            if w == 'строгий':
                if strogie <= 3 and strogie != 0:
                    strogie -=1
                    await message.answer(f'Саратову был снят строгий.\nВсего строгих: {strogie}/3')
                elif strogie == 0:
                    await message.answer(f'У Саратова нет строгих.\nВсего устных: {ystnie}/3\nВсего строгих: {strogie}/3')

            data["ystnie"] = ystnie
            data["strogie"] = strogie
            saveJson()
        else:
            await message.answer(f'Введите /помощь, чтобы посмотреть команды.')
    else:
        await message.answer(f'У вас нет прав!')

@bot.on.chat_message(text=['/статистика'])
async def stats(message: Message):
    balli = data["balli"]
    ystnie = data["ystnie"]
    strogie = data["strogie"]
    members = data["offmem"]
    await message.answer(f'Статистика Саратова:\nБаллы: {balli}\nУстных: {ystnie}/3\nCтрогих: {strogie}/3\nЖители: {members}')

@bot.on.chat_message(text=['/персонал'])
async def stats(message: Message):
    await message.answer(f'''Руководство Саратова:
        Иллюминат: {data["illuminate"]}
        Главный Администратор: {data["ga"]}
        Главный следящий: {data["gs"]}
        Лидер: {data["leader"]}''')

@bot.on.chat_message(text=['/лор'])
async def stats(message: Message):
    await message.answer(f'''История Саратова:
    Саратов — город на юго-востоке европейской части России, административный центр Саратовской области.
    Из Саратова нельзя сбежать, это тюрьма строгого режима. Любые попытки сбежать приравниваются как измена родины.
    В Саратове нужно наслаждаться жизнью.
    Роли Саратова:
    · Иллюминат - управляет всем миром, потому что у него есть деньги всего мира. Должен следить за работой ГА.
    · Главный Администратор - следит за порядком работы Следящего Администратора.
    · Главный Следящий - следит за порядком работы Саратова. Поощрает и наказывает работу Лидера Саратова.
    · Лидер - бедный человек, которого пытаются слить администраторы. Следит за своим городом, работает во всю силу.
    · Граждане - обычные челики, которых принимают и увольняют, жители Саратова.
    ''')

@bot.on.chat_message(text=['/помощь'])
async def stats(message: Message):
    await message.answer('''Команды для управления Саратовом:
        Админ-команды:
        /makeleader <@id> - назначить лидером Саратова
        /removeleader <@id> - снять лидера Саратова
        /баллы <баллы> - выдать баллы Саратову. (Пример: /баллы +10)
        /±устный - выдать/cнять устный Саратову. (Пример: /+устный)
        /±строгий - выдать/cнять строгий Саратову. (Пример: /-строгий)
        /нрпники - проверить Саратов на НРП ники.

        Команды лидера:
        /собеска - провести собеседование
        /устныйзабаллы - снять устный за 35 баллов
        /строгийзабаллы - снять строгий за 75 баллов
        
        Команды:   
        /статистика - статистика Саратова
        /персонал - руководство Саратова
        /лор - лор Саратова''')

@bot.on.chat_message(text=['/makeleader <w>', '/makeleader'])
async def makeleader(message: Message, w=None):
    if message.from_id == 499748580 or message.from_id == 24351886:
        if w is not None:
            fl = re.findall("@\w+", w)
            getid = re.findall("\d+", w)
            w = re.findall("@\w+", w)
            if data['leader'] == 'Нет':
                if w[0] == fl[0]:
                    id_ = await bot.api.users.get(getid[0])
                    leader = f'@id{id_[0].id} ({id_[0].first_name} {id_[0].last_name})'
                    await message.answer(f'Лидером Саратова назначен: {leader}\nПоздравляем его!')
                else:
                    await message.answer(f'Введите /makeleader @id, чтобы назначить лидера Саратова')
            else:
                await message.answer(f'Лидер Саратова уже назначен')

            data["leader"] = leader
            saveJson()
        else:
            await message.answer(f'Введите /makeleader @id, чтобы назначить лидера Саратова')
    else:
        await message.answer(f'У вас нет прав!')

@bot.on.chat_message(text=['/removeleader <w>', '/removeleader'])
async def removeleader(message: Message, w=None):
    if message.from_id == 499748580 or message.from_id == 24351886:
        if w is not None:
            fl = re.findall("@\w+", w)
            getid = re.findall("\d+", w)
            leader = data["leader"]
            w = re.findall("@\w+", w)
            if w != []:
                if w[0] == fl[0]:
                    id_ = await bot.api.users.get(getid[0])
                    leader_ = f'@id{id_[0].id} ({id_[0].first_name} {id_[0].last_name})'
                    if leader_ == data["leader"]:
                        await message.answer(f'Лидер Саратова {leader} был снят.')
                        leader = "Нет"
                    else:
                        print(leader, data["leader"])
                        await message.answer(f'Этот участник не является лидером Саратова.')
            else:
                await message.answer(f'Введите /removeleader @id, чтобы снять лидера Саратова')
            data["leader"] = leader
            saveJson()
        else:
            await message.answer(f'Введите /removeleader @id, чтобы снять лидера Саратова')
    else:
        await message.answer(f'У вас нет прав!')

def saveJson():
    jsonFile = open("database.json", "w+", encoding="utf-8")
    jsonFile.write(json.dumps(data, ensure_ascii=False))
    jsonFile.close()

bot.run_forever()