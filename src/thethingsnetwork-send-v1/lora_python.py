import subprocess

proc = subprocess.Popen("./thethingsnetwork-send-v1", stdin=subprocess.PIPE,stdout=subprocess.PIPE)

while(1):
    value = bytes('test.', 'UTF-8')
    proc.stdin.write(value)
    proc.stdin.flush()
    result = proc.stdout.readline().strip()
    print(result)
