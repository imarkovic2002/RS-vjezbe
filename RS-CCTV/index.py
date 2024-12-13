import cctv     # Instanca klase CCTV_frame 
import asyncio 
import random

# Instanca klase
cctv1 = cctv.CCTV_frame(1, 10, 20, 30, "Active", "1x", "192.168.1.10")

print(cctv1.info_cctv())    # Pozivanje metode info nad instancom.

# Korutina za simulaciju kretanja
async def simulate_movement(frame_rate, seconds):
    """
    Simulira kretanje kamere za određeni frame_rate i trajanje u sekundama.
    """
    lista_koordinata = []
    for _ in range(frame_rate * seconds):
        random_x = random.uniform(-100, 100)
        random_y = random.uniform(-100, 100)
        lista_koordinata.append((random_x, random_y))
        await asyncio.sleep(1 / frame_rate)  # Simulacija čekanja između frameova
    return lista_koordinata

# Korutina za ažuriranje lokacije kamere
async def update_camera_location(instance, x, y):

    instance.location_x = x
    instance.location_y = y
    print(f"Ažurirana lokacija kamere: x={x:.2f}, y={y:.2f}")

# Glavna korutina
async def main(): 
    print("Simulacija započinje...")
    
    # Generisanje pozicija za različito trajanje
    positions = await asyncio.gather(*[simulate_movement(30, i) for i in range(1, 6)])
    
    # Spajanje svih pozicija u jednu listu
    all_positions = [pos for sublist in positions for pos in sublist]
    
    # Ažuriranje lokacije kamere za svaku generisanu poziciju
    for x, y in all_positions[:10]:  # Samo prvih 10 za prikaz 
        await update_camera_location(cctv1, x, y)
    
    print(f"Ukupno generiranih pozicija: {len(all_positions)}")

# Pokretanje glavne korutine
asyncio.run(main())
