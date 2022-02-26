# Flask app

This flask app uses the Python module `markdown` to generate html pages from markdown files. Pages on the website are represented as markdown files in the directory `pages`. Each markdown file in this directory is converted to an html file in the directory `templates`. Flask uses the html files in `templates` to serve each endpoint.

```
├── pages
|	├── git_tutorial.md
|	├── homepage.md
```

To convert the markdown files to html, from the root directory:
```
python scripts/markdown_to_html.py
```


## Deployment
Build is tested on a Windows 10 x64 computer. Commands should be run using the the `Anaconda Prompt`, from the root of this repository. Commands may not work on the `Anaconda Powershell Prompt`. First set up your virtual environment:
```
python -m venv venv
venv\Scripts\activate
```

Install the project dependencies
pip install -r requirements.txt
```

Once the venv has been activated, you can serve the app locally:
```
python scripts/markdown_to_html.py
python app.py
```

This command serves the application on a port on your local machine. When you run `app.py`, Flask indicates which port is being used on your local IP address (127.0.0.1). The default port is usually 5000. To access the website, navigate to that port using any web browser.
```
* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```


## Contributing
Virtual environments provide a way to containerize the deployment of the flask app. To create a new virtual environment and install all dependencies, use the following commands. The *requirements.txt* is used to maintain versioning of Python packages between machines.
```
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

The venv files are omitted from the Git repo for simplicity; notice that the `.gitignore` masks the directory `env`. After installing new packages to the venv, save the requirements to `requirements.txt` so that your dependencies are added to the repository.
```
python -m pip freeze > requirements.txt
```

### CSS Styling
CSS styling is performed using the files in the directory `static/css/`. To apply css styling to markdown files, simply change line 43 in `markdown_to_html.py`. In the example below, the styling in `style.css` will be applied to all markdown files.

```
header_str = linkCss('css/style.css')
```

## Credit
This solution is made possible by the great community of open-source programmers who publish their solutions on the web.

* [Flask by example](https://realpython.com/flask-by-example-part-1-project-setup/)
* [Rendering markdown from flask](https://dev.to/mrprofessor/rendering-markdown-from-flask-1l41)
