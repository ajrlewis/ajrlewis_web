#! /usr/bin/env bash

usage() {
   echo "Gandi installation & development script."
   echo
   echo "Syntax: install.sh [-d|h]"
   echo "options:"
   echo "i     Initialize gandi and github remote repositories."
   echo "p     Push to remote repositories."
   echo "d     Deploy to gandi instance."
   echo "u     Print this help for usage."
   echo
}

init() {
  if git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
    echo ">> Git repository already exists."
  else
    git init
    echo ">> Git repository initialized."
  fi
}

add_remotes(){
  echo ">> git remote add gandi git+ssh://${GANDI_USER}@${GANDI_SERVER}/${GANDI_REPO}"
  git remote add gandi git+ssh://${GANDI_USER}@${GANDI_SERVER}/${GANDI_REPO}
  echo ">> git remote add github git@github.com:${GITHUB_USER}/${GITHUB_REPO}.git"
  git remote add github git@github.com:${GITHUB_USER}/${GITHUB_REPO}.git  
}

push() {
  git push --force gandi master
  echo ">> Push to git gandi remote."
  git push --force github master
  echo ">> Push to git github remote."
}

deploy() {
  echo ">> ssh ${GANDI_USER}@${GANDI_SERVER} deploy default.git"
  ssh ${GANDI_USER}@${GANDI_SERVER} deploy default.git
  echo "ssh ${GANDI_USER}@${GANDI_SERVER} clean default.git"
  ssh ${GANDI_USER}@${GANDI_SERVER} clean default.git
}

echo ">> source .env"
source .env

while getopts ":ipdu" option; do
    case $option in
        i) #
            init;
            add_remotes;;
        p) #
            push;;
        d) #
            deploy;;
        u) # display help
            usage;
            exit;;
        \?) # Invalid option
            echo "Error: Invalid option";
            exit;;
   esac
done
