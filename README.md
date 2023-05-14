# minecraft-modpack-enigmatica-8-diary
This is a VuePress &amp; Github Pages static website for describing our enigmatica 8 server

You can checkout our site at:  
[https://lightaxis.github.io/minecraft-modpack-enigmatica-8-diary/](https://lightaxis.github.io/minecraft-modpack-enigmatica-8-diary/)

**Table of Contents**
- [How to prepare this repo](#how-to-prepare-this-repo)
- [TroubleShooting](#troubleshooting)
- [How to test in local](#how-to-test-in-local)
- [How to deploy to server](#how-to-deploy-to-server)
- [TagLinker](#taglinker)

## How to prepare this repo

```shell
# if npm is not installed, 
sudo apt-get install npm

# init this repo as vuepress
npm install -g yarn
yarn init
yarn add -D vuepress
yarn add -D @vuepress/plugin-back-to-top
yarn add -D @vuepress/plugin-last-updated
yarn add -D vuepress-plugin-code-copy

```

## TroubleShooting
If version of 'node' is lower than 12.x version, you must reinstall node.js with higher version

```shell
## purge old node js
sudo apt purge nodejs

## remove ols apt sources.list of nodejs
sudo rm -rf /etc/apt/sources.list.d/nodesource.list

## get new sources list, 14.x version
sudo curl -sL https://deb.nodesource.com/setup_14.x | bash -
##### if above curl is failed with permission issue, try these instead #####
# wget https://deb.nodesource.com/setup_14.x
# mv setup_14.x setup_14.x.sh
# chmod +x setup_14.x.sh
# sudo ./setup_14.x.sh

## install node js with new apt.sources.list
sudo apt install nodejs

## check node version is 14.x
node --version
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
# check current branch is 'main'
# message "fatal: A branch named 'main' already exists." is normal
git branch main

# commit new changes to local main branch
# please change 'description of these changes' as your message
# ex) git commit -m "add : new systems, villager land"
git add .
git commit -m "description of these changes"

# push new changes to remote main brance
git push

# run a deply script to deploy changed docs to our server
./deploy.sh
```
That script is doing:
1. run adjustment python scripts
2. do `npm run build` to build html files
3. make a new git init in doc/.vuepress/dist
4. init a new commit
5. force push to gh-pages branch

## TagLinker
Custom comment-based text generator for document cross referencing.
python3 library only for this repo to take care of auto generating cross-reference between pages

[TagLinker ReadMe.md](./TagLinker/readme.md)