# Flask app

This flask app uses `markdown` to generate html pages from markdown files. Pages on the website are represented as markdown files in the directory `pages`. Each markdown file in this directory is converted to an html file in the directory `templates`. Flask uses the html files in `templates` to serve each endpoint.

```
├── pages
|	├── git_tutorial.md
|	├── homepage.md
```

To convert the markdown files to html, from the root directory:
```
./scripts/markdown_to_html.py
```


## Deployment
Build is tested on a Windows 10 x64 computer. To serve the app locally:
```
python scripts/markdown_to_html.py
call env/Scripts/activate
python app.py
```


## Contributing
Virtual environments provide a way to containerize the deployment of the flask app. To create a new virtual environment and install all dependencies, use the following commands. The *requirements.txt* is used to maintain versioning of Python packages between machines.
```
python -m venv env
call env/Scripts/activate
pip install -r requirements.txt
```

The venv files are omitted from the Git repo for simplicity; notice that the `.gitignore` masks the directory `env`. After installing new packages to the venv, save the requirements to `requirements.txt` so that your dependencies are added to the repository.
```
python -m pip freeze > requirements.txt
```


## Credit
This solution is made possible by the great community of open-source programmers who publish their solutions on the web.

* [Flask by example](https://realpython.com/flask-by-example-part-1-project-setup/)
* [Rendering markdown from flask](https://dev.to/mrprofessor/rendering-markdown-from-flask-1l41)