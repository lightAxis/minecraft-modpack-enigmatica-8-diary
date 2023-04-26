#!/usr/bin/env sh

# abort on errors
set -e

./run_adjustment_script.sh

# build
npm run build

# navigate into the build output directory
cd docs/.vuepress/dist

# if you are deploying to a custom domain
# echo 'www.example.com' > CNAME

# nojellky
touch .nojekyll

git init
git add -A
git commit -m 'deploy with vuepress'


# if you are deploying to https://<USERNAME>.github.io
# git push -f git@github.com:<USERNAME>/<USERNAME>.github.io.git master

# if you are deploying to https://<USERNAME>.github.io/<REPO>
git push -f https://github.com/lightAxis/minecraft-modpack-enigmatica-8-diary.git master:gh-pages

cd -
 
