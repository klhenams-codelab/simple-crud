# simple-crud

Requirements
---

* Python `3.9+`
* Postgresql `2.9+`
* Django `3.2+`


> ***Note***: Use a virtual environment or container for project isolation 


## Set up configuration file

Locate `src/.env.dist`

Rename `.env.dist` to `.env` set the various configurations

# Running application
Run this command to install dependencies

1. Build the images

```bash
docker-compose build
```

3. Start your containers.

```bash
docker-compose up
```


4. If you want to run a bash shell on an existing container, you can start a shell on it by name.

```bash
docker exec -it simple_crud_web_1 bash
```

5. While in shell the you can set up the database running the following commands sequentially

```bash
python manage.py migrate

python manage.py loaddata -i fixtures/diagnosis.json
```

If you want to get a hands-on experience with the APIs, check out the links below .

<a href="https://www.postman.com/defyn-dev/workspace/mpharma" target="_blank">Postman Public Workspace</a>

<a href="https://documenter.getpostman.com/view/18209335/UyrHdsVS" target="_blank">Postman Documentation</a>