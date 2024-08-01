git branch2 && git checkout branch2
touch file4 && git add file4
echo 'some text' >>file4
git stash
git checkout main
