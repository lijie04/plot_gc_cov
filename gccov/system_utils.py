#####################################################################
#																	#
#system_utils.py -  system operations related functions									#
#																	#
#####################################################################

import os
import sys
import logging
import errno
import re

def check_path_exists(path):
	"""Check if path is exists, check_path_exists(path), 
	if path is not exists, program exits."""
	if not os.path.exists(path):
		logger = logging.getLogger("timestamp")
		logger.error("Directory does not exists: %s.\n" % (path))
		sys.exit(1)

def make_sure_path_exists(path):
	"""Check if path is exists, if not exists then create path, make_sure_path_existes(path),
	if path not exists and not creatable, program exits."""
	if path == "." or path == "./":    ## judge path is indicating current dir or not.
		path = os.getcwd()
	elif re.match("/", path): ## judge path is an absolute path or not.
		pass
	else:
		path = os.getcwd() + "/" + path ## if not current dir and not an absolute path, then it should be a dir created at current dir I suppose.

	try:
		os.makedirs(path)
	except OSError as exception:
		if exception.errno != errno.EEXIST:
			logger = logging.getLogger()
			logger.error("Path does not exists and it is not creatable: %s\n" % (path))
			sys.exit(1)

def check_file_exists(input_file):
	"""Check if file exists, check_file_exists(input_file), 
	if file is not existed, program exits"""
	if not os.path.isfile(input_file):
		logger = logging.getLogger("timestamp")
		logger.error("File does not exists:" + input_file + "\n")
		sys.exit(1)

def check_files_exist(input_files):
	"""Check if batch of files or a single file exist, check_files_exist(input_files),
	if any file is not existed, program exit."""
	if type(input_files) == str:
		check_file_exists(input_files)
	else:
		if type(input_files) == list:
			for f in input_files:
				if type(f) == str:
					check_file_exists(f)
				else:
					if type(f) == list:
						check_files_exist(f)
					else:
						logger = logging.getLogger("timestamp")
						logger.error("File does not exists: " + f + "\n")
						sys.exit(1)
		else:
			logger = logging.getLogger("timestamp")
			logger.error("File seems weird, please check: " + ",".join(input_files) + "\n")
			sys.exit(1)

def make_full_path(path):
	#print(path)
	if path.startswith('/'):
		if path.endswith('/'):
			path = path
		else:
			path = path + '/'
	elif path.starswith('.'):
		if path.endswith('/'):
			path = os.getcwd() + '/'
		else:
			path = os.getcwd() + '/' + path + '/'
	else:
		if path.endswith('/'):
			path = os.getcwd() + '/' + path
		else:
			path = os.getcwd() + '/' + path + '/'
	make_sure_path_exists(path)
	return path

def check_software(sft):
	if os.system(sft) == 32512:
		sys.exit('Software %s is not exist.\n' % sft)

