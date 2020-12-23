:: virtual environment
call conda remove -y -n flasktemplate --all
call conda create -y -n flasktemplate python
call activate flasktemplate

:: install requirements
call pip install -r requirements.txt