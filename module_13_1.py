import asyncio

async def start_strongman(name, power):
          print(f"Силач ", name ," начал соревнования.")

          for i in range(1,6):
             await asyncio.sleep(1/power)
             print(f"Силач ", name, " поднял ",i," шар>")

          print(f"Силач ", name ," закончил соревнования.'")

async def start_tournament():
    tournament  = asyncio.create_task(start_strongman('Betmen', 3))
    tournament1 = asyncio.create_task(start_strongman('Ironman', 4))
    tournament2 = asyncio.create_task(start_strongman('Superman', 5))
    await tournament
    await tournament1
    await tournament2

asyncio.run(start_tournament())