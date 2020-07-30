"""
markdown_to_html.py
------------------
Convert markdown files to html files.

Input : markdown files in /pages
Output : html files in /templates
"""

import markdown
import os


def main():

	print("\nConverting markdown to html.................\n")

	os.makedirs('templates',exist_ok=True)


	# read files from /pages
	files = os.listdir("pages/")
	filepaths = [{	"filename": x,
					"input_path": "pages/" + x,
					"output_path": "templates/" + x.split(".")[0] + ".html"}
				for x in files if x.split(".")[1] != 'mds']


	for file in filepaths:

		# convert to html string
		readme_file = open(file['input_path'], "r")
		md_template_string = markdown.markdown(
		    readme_file.read(), extensions=["fenced_code"]
		)

		# write to /templates
		text_file = open(file['output_path'], "w")
		text_file.write(md_template_string)
		text_file.close()



if __name__ == '__main__':
	main()