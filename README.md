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

# add excute permission to deploy script
chmod +x deploy.sh
```

## How to test in local
```shell
npm run doc
```

Than will open as a local server address which is usally:  
 http://localhost:8080/minecraft-modpack-enigmatica-8-diary/

## How to deploy to server
```shell
./deploy.sh
```
That script is doing:
1. make a new git init in dist
2. init a new commit
3. force push to gh-pages branch