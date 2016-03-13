echo enter commit please:
read commit
git add -A
git commit -m"${commit}"
git push
