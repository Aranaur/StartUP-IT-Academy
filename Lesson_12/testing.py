import asyncio


async def addition(string_data):
    _list = [float(i) for i in string_data.split(", ")]
    output = f'{_list[0]} + {_list[1]} = {_list[0] + _list[1]}'
    await asyncio.sleep(1)
    print(output)


async def subtraction(string_data):
    _list = [float(i) for i in string_data.split(", ")]
    output = f'{_list[0]} - {_list[1]} = {_list[0] - _list[1]}'
    await asyncio.sleep(1)
    print(output)


async def multiply(string_data):
    _list = [float(i) for i in string_data.split(", ")]
    output = f'{_list[0]} * {_list[1]} = {_list[0] * _list[1]}'
    await asyncio.sleep(1)
    print(output)


async def division(string_data):
    _list = [float(i) for i in string_data.split(", ")]
    output = f'{_list[0]} / {_list[1]} = {_list[0] / _list[1]}'
    await asyncio.sleep(1)
    print(output)


string_data = '2, 5'

loop = asyncio.get_event_loop()
tasks = [
    loop.create_task(addition(string_data)),
    loop.create_task(subtraction(string_data)),
    loop.create_task(multiply(string_data)),
    loop.create_task(division(string_data)),
]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
