import speedtest
import time

start = time.time()
on = speedtest.Speedtest()
velocidadedown = str(on.download())
velocidadeup = str(on.upload())

print(f'DOWNLOAD: {velocidadedown[:2]},{velocidadedown[2:4]} Mbps.\n'
       f'UPLOAD: {velocidadeup[:2]},{velocidadeup[2:4]} Mbps.')

final = time.time()
result = final - start

print("DURAÇÃO DO TESTE: {:.2f} Segundos" .format(result))



