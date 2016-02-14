import os
import sys
import shutil
import platform
from subprocess import call
from os.path import join

#Pick a Clang-Format binary
if platform.system() == 'Darwin':
	clang_format_path = '../ClangFormat-Mac/clang-format'
elif platform.system() == 'Windows':
	clang_format_path = '../ClangFormat-Windows/clang-format'	
else:
	print("Platform not supported: " + platform.system())
	exit()

#Run Clang-Format on all eligible files
for root, dirs, files in os.walk(sys.argv[1]):
	for name in files:
		if not name.endswith(('.h', '.cpp', '.c', '.mm')):
			continue
		call([clang_format_path, '-i', '-style=file', join(root, name)])
