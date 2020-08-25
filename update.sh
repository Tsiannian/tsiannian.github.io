#/bin/sh
git add .
git commit -m "update"
git push 

jekyll build

cd _site
git add .
git commit --amend --no-edit
git push -f

jekyll server