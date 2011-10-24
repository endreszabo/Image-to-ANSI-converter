#!/usr/bin/python
from sys import argv
from math import pow
import gd

def color256to16(color, is_back):
	red = color >> 16;
	green = color % 65536 >> 8;
	blue = color % 256;
	a16rgbtable = (
		(0, 0, 0),
		(128, 0, 0),
		(0, 128, 0),
		(128, 128, 0), 
		(0, 0, 128), 
		(128, 0, 128),
		(0, 128, 128), 
		(192, 192, 192), 
		(128, 128, 128),
		(255, 0, 0), 
		(0, 255, 0), 
		(255, 255, 0),
		(0, 0, 255), 
		(255, 0, 255), 
		(0, 255, 255),
		(255, 255, 255)
	);
	best_match = 0;
	d=0.0,
	smallest_distance = 10000000000.0;
	if is_back:
		is_back=16
	else:
		is_back=8
	for c in range(is_back):
		d = pow(a16rgbtable[c][0]-red, 2.0) +\
			pow(a16rgbtable[c][1]-green, 2.0) +\
			pow(a16rgbtable[c][2]-blue, 2.0);
		if (d<smallest_distance):
			smallest_distance = d;
			best_match = c;
	return best_match;
if len(argv)<2:
	print "usage: %s <imagefile>" % argv[0]
else:
	for imagefile in argv[1:]:
		#try:
		a=gd.image(imagefile)
		(x,y)=a.size()
		oldcolor=0
		destfile=open(imagefile+'.ansi','w')
		for h in range(y):
			for w in range(x):
				color=color256to16(a.getPixel([w,h]),1)
				if color is not oldcolor:
					destfile.write("\x1b[48;5;%dm  " % color256to16(a.getPixel([w,h]),1))
					oldcolor=color
				else:
					destfile.write("  ")
			destfile.write("\n\x1b[0m")
		destfile.close()
		#except:
		#	print "fail."
