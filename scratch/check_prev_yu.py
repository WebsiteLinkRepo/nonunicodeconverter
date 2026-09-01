import subprocess

cmd = 'git show e7e388f~1:src/utils/mappings/shreeLipi.ts'
out = subprocess.check_output(cmd, shell=True).decode('utf-8')

for line in out.splitlines():
    if '"यु"' in line or '"`w"' in line or 'यु' in line:
        print(line)
