import cctv
import asyncio 
import random

cctv1 = cctv.CCTV_frame(1, 10, 20, 30, "Active", "1x", "192.168.1.10")


async def simulate_moment(frame_Rate, seconds):
    lista_koordinata = []
    for _ in range(frame_Rate * seconds):
        x = random.uniform(-100, 100)
        y = random.uniform(-100, 100)
        lista_koordinata.append((x,y))
        await asyncio.sleep(1 / frame_Rate)
        
        return lista_koordinata

async def update_camera_location(instance, x, y):
        
async def main(): 
    print("Igor")
    
    positions = await asyncio.gather(*[simulate_moment(30,i) for i in range(1, 6)])
    print(positions)

  
    lista_ntorki = []
  
    for position_list in positions:
        for n_torka in position_list:
            lista_ntorki.append(n_torka)
asyncio.run(main())
    