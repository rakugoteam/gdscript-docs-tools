def gen_docs(scripts : list, output: str, check: bool):
	for script in scripts:
		gen_doc(script, output, check)