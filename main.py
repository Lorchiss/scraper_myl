import os
import subprocess

if os.name == 'nt':
  directorio = os.getcwd().replace('\\','/').strip()
  buscar = subprocess.run(
    ["powershell", "-Command", f"Get-ChildItem", "-Path", f"'{directorio}'", "-Recurse","-Directory","-Filter","'spiders'"],
    stdout=subprocess.PIPE,
    text=True
  )
  buscar.stdout.replace('\\','/').strip()
  sbuscar = buscar.stdout.strip().split("\\")
  os.chdir(os.path.join(directorio, sbuscar[-2]))
  
else:
  # Se obtiene la ruta donde se esta ejecutando el script
  directorio = subprocess.run(["pwd"], stdout=subprocess.PIPE)
  directorio = directorio.stdout.decode().strip()

  # Se busca el directorio spiders con una profundidad de 3 
  buscar = subprocess.run(
      ['find', directorio, '-type','d', '-name','spiders'],
      stdout=subprocess.PIPE)

  # Se cambia de directorio al que se encuentra el spider
  sbuscar = buscar.stdout.strip().split("/")
  print(sbuscar)
  os.chdir(os.path.join(directorio, sbuscar[-2]))

# Se cambia de directorio al que se encuentra el spider


# Se ejecuta el spider
process = subprocess.Popen(['scrapy', 'crawl', 'myl','-L','INFO'],
                           stdout=subprocess.PIPE,
                           stderr=subprocess.STDOUT,
                           text=True)

for line in process.stdout:
  print(line, end='')

return_code = process.wait()

if process.returncode != 0:

  print(process.stderr)
