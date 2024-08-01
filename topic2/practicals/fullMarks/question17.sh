cd git-practice-03/
git branch branch1
git branch branch2
git checkout branch1
git mv dir1/dir2/foo dir1/foo
touch newfile1
git add newfile1
git commit -m 'a commit message'

git checkout branch2
git mv dir1/dir2/foo dir1/dir2/foo_modified
touch dir3/newfile2
git add dir3/newfile2
git rm dir3/bar
git mv dir3/ dir1/
git commit -m 'made changes'

git checkout main
cp dir3/bar dir3/bar_copy
git add dir3/bar_copy
git commit -m 'some message'
