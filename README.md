NAME
====

Image to ANSI - Converts any gd importable image to terminal ANSI codes

SYNOPSIS
========

	python2	Image-to-ANSI-converter.py <16|256> <u|n> <imagefile> [imagefiles...]

	16 or 256: number of colors to use
	u or n: unicode or normal characters,
			Final images will be half in size if using unicode

DEPENDS
=======

It requires the python bindings for the gd library (eg. http://aur.archlinux.org/packages.php?ID=27603).
