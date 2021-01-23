# Flask/Python API
<p>Response POST request with bool parameter.<br>
If TRUE it response current date as aaaa-mm-dd hh:ii:ss<br>
If False it response current date as aaaa-mm-dd</p>

## Started in a fresh conda environment and only installed flask
```shell
pip install Flask
```
<p>if desired requirements in requirements.txt</p>

## Launch the server in windows 10 cmd with:
```shell
set FLASK_APP=date_post.py
python -m flask run
```

## Tested responses in windows 10 PowerShell with:
```shell
PS> Invoke-WebRequest -Uri "http://127.0.0.1:5000" -Body @{"flag"=$true} -Method Post
```
<p>Responses   {"date":"2021-01-23 00:00:06"}</p>

```shell
PS> Invoke-WebRequest -Uri "http://127.0.0.1:5000" -Body @{"flag"=$false} -Method Post
```
<p>Responses   {"date":"2021-01-23"}</p>

```shell
PS> Invoke-WebRequest -Uri "http://127.0.0.1:5000" -Method Post
```
<p>Responses   400 Bad request. Expecting body with boolean variable named flag.</p>

```shell
PS> Invoke-WebRequest -Uri "http://127.0.0.1:5000" -Body @{"flag"="any"} -Method Post
```
<p>Responses   {"date":"2021-01-23"}</p>

```shell
PS> Invoke-WebRequest -Uri "http://127.0.0.1:5000" -Method Get
```
<p>Responses   405 Method Not Allowed</p>
