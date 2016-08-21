import win32gui
from time import sleep
from sys import argv

args = argv
print(args)
print(len(args))

if len(args) != 1:
    layout = int(args[1])
else:
    print("Please enter arguments: layout [required] (see docs)")

if layout == 1:
		
	gap = 20
	w1 = 900
	h1 = 450
	w2 = 900
	h2 = 450
	
	if len(args) >= 3:
		gap = int(args[2])
		
	if len(args) >= 4:
		w1 = int(args[3])
		
	if len(args) >= 5:
		h1 = int(args[4]) - gap/2
	
	if len(args) == 7:
		h2 = int(args[6]) - gap/2
	
	if len(args) >= 6:
		w2 = int(args[5])
	
		
	x1 = 1927 / 2 - w1/2
	y1 = (1080 - h1 - h2 - gap) / 2
	x2 = 1927/2 - w2/2
	y2 = (y1 + h1 + gap)
	
	print("Select window 1 and wait 3 sec")
	sleep(3)
	hwnd = win32gui.GetForegroundWindow()
	win32gui.MoveWindow(hwnd, int(x1), int(y1), int(w1), int(h1), True)
	print("Select window 2 and wait 3 sec")
	sleep(3)
	hwnd = win32gui.GetForegroundWindow()
	win32gui.MoveWindow(hwnd, int(x2), int(y2), int(w2), int(h2), True)


if layout == 2:
		
	gap = 20
	w1 = 900
	h1 = 900
	w2 = 900
	h2 = 900
	
	if len(args) >= 3:
		gap = int(args[2])
		
	if len(args) >= 4:
		w1 = int(args[3])
		
	if len(args) >= 5:
		h1 = int(args[4]) - gap/2
	
	if len(args) == 7:
		h2 = int(args[6]) - gap/2
	
	if len(args) >= 6:
		w2 = int(args[5])
	
		
	x1 = (1927 - w1 - w2 - gap) / 2
	
	y1 = ((1080 - h1)/2)
	
	
	x2 = x1 + w1 + gap
	
	
	y2 = ((1080 - h2)/2)

	
	
	
	print("Select window 1 and wait 3 sec")
	sleep(3)
	hwnd = win32gui.GetForegroundWindow()
	win32gui.MoveWindow(hwnd, int(x1), int(y1), int(w1), int(h1), True)
	print("Select window 2 and wait 3 sec")
	sleep(3)
	hwnd = win32gui.GetForegroundWindow()
	win32gui.MoveWindow(hwnd, int(x2), int(y2), int(w2), int(h2), True)

	
	
if layout == 3:
		
	gap = 20
	
	w1 = 900
	h1 = 600
	w2 = 920
	h2 = 900
	
	w3 = 900
	h3 = 300
	
	if len(args) >= 3:
		gap = int(args[2])
		
	if len(args) >= 4:
		w1 = int(args[3])
		
	if len(args) >= 5:
		h1 = int(args[4]) - gap/2
	
	if len(args) >= 6:
		w2 = int(args[5])
	
	if len(args) >= 7:
		h2 = int(args[6]) - gap/2

	if len(args) >= 8:
		w3 = int(args[7])
		
	if len(args) == 9:
	   h3 = int(args[8]) - gap/2
	  

	
		
	x1 = (1927 - w1 - w2 - gap) / 2
	
	y1 = (1080 - h1 - h3 - gap) / 2
	
	x3 = (1927 - w3 - w2 - gap) / 2
	y3 = (y1 + h1 + gap)
	
	
	
	x2 = x1 + w1 + gap
	
	
	y2 = ((1080 - h2)/2 - gap/2)

	
	
	
	print("Select window 1 and wait 3 sec")
	sleep(2)
	hwnd = win32gui.GetForegroundWindow()
	win32gui.MoveWindow(hwnd, int(x1), int(y1), int(w1), int(h1), True)
	print("Select window 2 and wait 3 sec")
	sleep(2)
	hwnd = win32gui.GetForegroundWindow()
	win32gui.MoveWindow(hwnd, int(x2), int(y2), int(w2), int(h2), True)
	
	print("Select window 3 and wait 3 sec")
	sleep(2)
	hwnd = win32gui.GetForegroundWindow()
	win32gui.MoveWindow(hwnd, int(x3), int(y3), int(w3), int(h3), True)
	win32gui.MoveWindow(hwnd, int(x3), int(y3), int(w3), int(h3), True)
	
if layout == 4:
		
	gap = 20
	
	w1 = 400
	h1 = 400
	w2 = 400
	h2 = 400
	
	w3 = 400
	h3 = 400
	
	w4 = 400
	h4 = 400
	
	if len(args) >= 3:
		gap = int(args[2])
		
	if len(args) >= 4:
		w1 = int(args[3])
		
	if len(args) >= 5:
		h1 = int(args[4]) - gap/2
	
	if len(args) >= 6:
		w2 = int(args[5])
	
	if len(args) >= 7:
		h2 = int(args[6]) - gap/2

	if len(args) >= 8:
		w3 = int(args[7])
		
	if len(args) >= 9:
	   h3 = int(args[8]) - gap/2
	  
	if len(args) >= 10:
		w4 = int(args[9])
		
	if len(args) == 11:
		h4 = int(args[10]) - gap/2
	
		
	x1 = (1927 - w1 - w2 - gap) / 2
	y1 = (1080 - h1 - h3 - gap) / 2
	x3 = (1927 - w3 - w2 - gap) / 2
	y3 = (y1 + h1 + gap)
	
	y2 = (1080 - h1 - h2 - gap) / 2
	x2 = x1 + w1 + gap
	y4 = (y1 + h1 + gap)
	x4 = x3 + w3 + gap
	
	
	
	
	print("Select window 1 and wait 3 sec")
	sleep(3)
	hwnd = win32gui.GetForegroundWindow()
	win32gui.MoveWindow(hwnd, int(x1), int(y1), int(w1), int(h1), True)
	print("Select window 2 and wait 3 sec")
	sleep(3)
	hwnd = win32gui.GetForegroundWindow()
	win32gui.MoveWindow(hwnd, int(x2), int(y2), int(w2), int(h2), True)
	
	print("Select window 3 and wait 3 sec")
	sleep(3)
	hwnd = win32gui.GetForegroundWindow()
	win32gui.MoveWindow(hwnd, int(x3), int(y3), int(w3), int(h3), True)
	
	print("Select window 4 and wait 3 sec")
	sleep(3)
	hwnd = win32gui.GetForegroundWindow()
	win32gui.MoveWindow(hwnd, int(x4), int(y4), int(w4), int(h4), True)
	
if layout == 5:
		
	gap = 20
	
	w1 = 600
	h1 = 920
	w2 = 450
	h2 = 450
	
	w3 = 450
	h3 = 450
	
	w4 = 450
	h4 = 450
	
	if len(args) >= 3:
		gap = int(args[2])
		
	if len(args) >= 4:
		w1 = int(args[3])
		
	if len(args) >= 5:
		h1 = int(args[4]) - gap/2
	
	if len(args) >= 6:
		w2 = int(args[5])
	
	if len(args) >= 7:
		h2 = int(args[6]) - gap/2

	if len(args) >= 8:
		w4 = int(args[7])
		
	if len(args) == 9:
		h4 = int(args[8]) - gap/2
	
		
	x1 = 1927 / 2 - w1
	y1 = ((1080 - h1)/2)
	
	y2 = (1080 - h2 - h4 - gap) / 2
	x2 = x1 + w1 + gap
	y4 = (y2 + h2 + gap)
	x4 = x1 + w1 + gap
	
	print(str(y2 + h4 + gap))
	
	
	
	print("Select window 1 and wait 3 sec")
	sleep(3)
	hwnd = win32gui.GetForegroundWindow()
	win32gui.MoveWindow(hwnd, int(x1), int(y1), int(w1), int(h1), True)
	print("Select window 2 and wait 3 sec")
	sleep(3)
	hwnd = win32gui.GetForegroundWindow()
	win32gui.MoveWindow(hwnd, int(x2), int(y2), int(w2), int(h2), True)
	print("Select window 4 and wait 3 sec")
	sleep(3)
	hwnd = win32gui.GetForegroundWindow()
	win32gui.MoveWindow(hwnd, int(x4), int(y4), int(w4), int(h4), True)
	




