echo enter commit
read commit
git pull && git add -A && git commit -m "$commit" && git push
