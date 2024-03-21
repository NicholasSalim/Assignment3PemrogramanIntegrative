with open("indata.txt", "r") as file:
   
    lines = file.readlines()
    
    total = 0
    
    # Menjumlahkan angka-angka dalam file
    for line in lines:
        total += int(line)

print(f"{total:.2f}")
