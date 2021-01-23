# Flask/Python API 
### Response POST request with bool parameter.
### If TRUE it response current date as aaaa-mm-dd hh:ii:ss
### If False it response current date as aaaa-mm-dd

## Started in a fresh conda environment and only installed flask
pip install Flask
#### if desired requirements in requirements.txt

## Launch the server in windows 10 cmd with:
set FLASK_APP=date_post.py
python -m flask run

## Tested responses in windows 10 PowerShell with:

PS> Invoke-WebRequest -Uri "http://127.0.0.1:5000" -Body @{"flag"=$true} -Method Post
        Responses   {"date":"2021-01-23 00:00:06"}
PS> Invoke-WebRequest -Uri "http://127.0.0.1:5000" -Body @{"flag"=$false} -Method Post
        Responses   {"date":"2021-01-23"}
PS> Invoke-WebRequest -Uri "http://127.0.0.1:5000" -Method Post
        Responses   400 Bad request. Expecting body with boolean variable named flag.
PS> Invoke-WebRequest -Uri "http://127.0.0.1:5000" -Body @{"flag"="any"} -Method Post
        Responses   {"date":"2021-01-23"}
PS> Invoke-WebRequest -Uri "http://127.0.0.1:5000" -Method Get
        Responses   405 Method Not Allowed        
