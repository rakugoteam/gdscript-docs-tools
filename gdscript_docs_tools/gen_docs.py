from gdscript_docs_tools import *

def gen_docs(scripts : list, output: str):
	for script in scripts:
		gen_doc(script, output)