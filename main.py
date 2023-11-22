import subprocess
import os

directorio = subprocess.run(["pwd"], stdout=subprocess.PIPE)
print(directorio.stdout.decode("utf-8"))

os.chdir('/home/runner/scrapermyl/cartas_myl')
process = subprocess.Popen(['scrapy', 'crawl', 'myl'],
                           stdout=subprocess.PIPE,
                           stderr=subprocess.STDOUT,
                           text=True)

for line in process.stdout:
  print(line, end='')

return_code = process.wait()

if process.returncode != 0:
  
  print(process.stderr)
