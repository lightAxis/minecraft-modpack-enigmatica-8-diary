# minecraft-modpack-enigmatica-8-diary
This is a VuePress &amp; Github Pages static website for describing our enigmatica 8 server

You can checkout our site at:  
[https://lightaxis.github.io/minecraft-modpack-enigmatica-8-diary/](https://lightaxis.github.io/minecraft-modpack-enigmatica-8-diary/)

## How to prepare this repo

```shell
# if npm is not installed, 
sudo apt-get install npm

# init this repo as vuepress
npm init -y
npm install -D vuepress
npm audit fix

# add excute permission to shell scripts
# chmod +x deploy.sh
# chmod +x local_test.sh

# add execute permission to python scripts
# chmod +x image_adjust.py
# chmod +x make_player_profile.py
```

## How to test in local
```shell
./local_test.sh
```

That script is doing:
1. run adjustment python scripts
2. do `npm run doc` to build html files and open local test server

Than will open as a local server address which is usally:  
 http://localhost:8080/minecraft-modpack-enigmatica-8-diary/

## How to deploy to server
```shell
./deploy.sh
```
That script is doing:
1. run adjustment python scripts
2. do `npm run build` to build html files
3. make a new git init in doc/.vuepress/dist
4. init a new commit
5. force push to gh-pages branch