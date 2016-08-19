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
	
	if len(args) == 7:
		gap = int(args[6])
		
	if len(args) == 3:
		w1 = int(args[2])
		
	if len(args) == 4:
		h1 = int(args[3]) - gap/2
	
	if len(args) == 6:
		h2 = int(args[5]) - gap/2
	
	if len(args) == 5:
		w2 = int(args[4])
	
		
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
	
	if len(args) == 7:
		gap = int(args[6])
		
	if len(args) == 3:
		w1 = int(args[2])
		
	if len(args) == 4:
		h1 = int(args[3]) - gap/2
	
	if len(args) == 6:
		h2 = int(args[5]) - gap/2
	
	if len(args) == 5:
		w2 = int(args[4])
	
		
	x1 = (1927 - w1 - w2 - gap) / 2
	
	y1 = ((1080 - h1)/2)
	
	
	x2 = x1 + w1 + gap
	
	
	y2 = ((1080 - h1)/2)

	
	
	
	print("Select window 1 and wait 3 sec")
	sleep(3)
	hwnd = win32gui.GetForegroundWindow()
	win32gui.MoveWindow(hwnd, int(x1), int(y1), int(w1), int(h1), True)
	print("Select window 2 and wait 3 sec")
	sleep(3)
	hwnd = win32gui.GetForegroundWindow()
	win32gui.MoveWindow(hwnd, int(x2), int(y2), int(w2), int(h2), True)







