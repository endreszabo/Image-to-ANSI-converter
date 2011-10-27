NAME
====

Image to ANSI - Converts any gd importable image to terminal ANSI codes

SYNOPSIS
========

	python2	Image-to-ANSI-converter.py <16|256|irc> <u|n> <imagefile> [imagefiles...]

	16 or 256 or irc: number of colors to use. In case of 'irc' the output will be on stdout. Ideal for piping into xclip or irc client. IRC palette is based my own urxvt palette, YMMV.
	u or n: unicode or normal characters, final images will be half in size if using unicode

DEPENDS
=======

It requires the python bindings for the gd library (eg. http://aur.archlinux.org/packages.php?ID=27603).
