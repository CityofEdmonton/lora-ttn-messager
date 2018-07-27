import ctypes
import time
import os, signal
from multiprocessing import Process, active_children
from ctypes import cdll
lib = cdll.LoadLibrary('./lora-ttn.so')


# call C function for resetting Lora MAC state
def reset_lmic():
    lib.reset()

def run_lora(str):
    s = str.encode('utf-8')
    lib.start_loop.argtypes = [ctypes.c_char_p]
    lib.start_loop(s)    

def lora_proc(str):
    pactive = active_children()
    for p in pactive:
        id = p.pid
        os.kill(id,signal.SIGQUIT)
        time.sleep(50)
    lora = Process(target=run_lora, args=(str,))
    lora.start()
    i = lora.pid
    print("Lora ID: ")
    print(i)
    return i
