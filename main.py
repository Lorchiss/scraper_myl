import os
import subprocess

# Se obtiene la ruta donde se esta ejecutando el script
directorio = subprocess.run(["pwd"], stdout=subprocess.PIPE)
directorio = directorio.stdout.decode().strip()

# Se busca el directorio spiders con una profundidad de 3 
buscar = subprocess.run(
    ['find', directorio, '-maxdepth','3', '-type','d', '-name','spiders'],
    stdout=subprocess.PIPE)

# Se cambia de directorio al que se encuentra el spider
sbuscar = buscar.stdout.decode().strip().split("/")
os.chdir(os.path.join(directorio, sbuscar[-2]))

# Se ejecuta el spider
process = subprocess.Popen(['scrapy', 'crawl', 'myl'],
                           stdout=subprocess.PIPE,
                           stderr=subprocess.STDOUT,
                           text=True)

for line in process.stdout:
  print(line, end='')

return_code = process.wait()

if process.returncode != 0:

  print(process.stderr)
