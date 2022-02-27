# Flask app
This is a template flask application, with scaffolding already created.

## Development
Install project dependencies.
```bash
pip install -r requirements.txt
```

Run the application. By default, the app loads on port 5000.
```bash
python app.py
```

## Deployment
For more detailed information see the [Docker docs](https://docs.docker.com/language/python/).

Build Docker image.
```bash
docker build --tag flask-template . 
```

Run image in Docker container.
```bash
docker run flask-template
```


## Runtime Options
Run without reloading pages when files are changed.
```bash
python app.py --no-reload
```