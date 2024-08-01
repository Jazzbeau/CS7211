cd git-practice-04
git fetch
git branch -a
git merge origin/ready1 -m 'merged ready1'
git merge origin/ready2 -m 'merged ready2'
git merge origin/ready3 -m 'merged ready3'
git branch -dr origin/ready1 origin/ready2 origin/ready3
git checkout -b update1 origin/update1
git merge main
git checkout -b update2 origin/update2
git merge main
