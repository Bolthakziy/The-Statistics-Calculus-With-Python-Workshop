#!/bash/sh

PROJECT_PATH=/home/USER_NAME	# This path can be modified.
PROJECT_NAME=GitVersion2

echo "\n We will be shifted to [$PROJECT_PATH/$PROJECT_NAME] path.\n"
cd $PROJECT_PATH/$PROJECT_NAME

git init
git add .
git commit -m "GIT2"
git remote add origin https://github.com/Bolthakziy/THE-Statistics-Calculus-With-Python-Workshop.git
git push origin master

echo "It is done.\n"
