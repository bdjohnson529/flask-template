"""
markdown_to_html.py
------------------
Convert markdown files to html files.

Input : markdown files in /pages
Output : html files in /templates
"""

import markdown
import os


def linkCss(css_file):
	header_str = f"""<head><link rel= "stylesheet" href= \"{{{{ url_for('static', filename=\'{css_file}\') }}}}\" ></head>\n"""

	return header_str

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
		body_str = markdown.markdown(
		    readme_file.read(), extensions=["fenced_code"]
		)


		header_str = linkCss('css/style.css')
		html_str = header_str + body_str


		# write to /templates
		text_file = open(file['output_path'], "w")
		text_file.write(html_str)
		text_file.close()



if __name__ == '__main__':
	main()