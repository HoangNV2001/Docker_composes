```
git clone https://github.com/HoangNV2001/Jupyterhub-DockerSpawner 
cd Jupyterhub-mit-DockerSpawner
docker compose up -d
```

URL: [localhost:8000](http://localhost:8000) <br>
On the first open, go to signup and create an "admin" account, you don't need authorization for this first account to be created.

**Note**: 
* /data : will be shared drive. By default it is read-only, to allow write, need to change permission: 
> chmod -R 0777 /data