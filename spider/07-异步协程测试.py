import asyncio
import time
import aiofiles
def callback_Li(task):
    print(f'返回值是{task.result()}，是的我是李焕英')

async def fun1(name:str, second:int)->None :
    print(f'你好啊，我叫{name}')
    await asyncio.sleep(second)
    print(f'你好呀，你是叫{name}吗？')

async def main():
    asyncio.create_task(fun1('李焕英', 2))
    tasks = [asyncio.create_task(fun1('李焕英', 2)),
             asyncio.create_task(fun1('小说家', 3)),
             asyncio.create_task(fun1('曲婉婷', 4))]
    await asyncio.wait(tasks)

if __name__ == '__main__':
    start = time.time()
    asyncio.run(main())
    print(f'耗时{time.time()-start}')

    aiofiles.open()