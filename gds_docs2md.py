
from gdscript_docs_tools import *

if __name__ == "__main__":
	args = {}
	get_argv(args)
	# print(args)

	if args["help"]:
		print(
			"""
			gds_docs2md.py version 1.0
			It is a simple python tool that generates markdown from gdscript doc comments.

			Example of usage:
				python gds_docs2md.py -o output -ir gds_source -s plugin.gd

			Flags:
				-h, --help		will display this message
				-i, --input		you give dir sources of gdscript script to scan
				-r, --recursive		scan input recusivly
				-s, --skip		files and dirs to skip from input
			"""
		)
		exit()

	for i in args["input"]:
		scripts = scandir_for_gdscipts(
			i, args["recursive"], args["skip"]
		)
	
	gen_docs(scripts, args["output"])