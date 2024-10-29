#! /usr/bin/env bash

echo ">>> Start of install.sh script"

help() {
   echo "Install script."
   echo
   echo "Syntax: install.sh [-d|h]"
   echo "options:"
   echo "d     Enable development mode."
   echo "h     Print this help."
   echo
}

environment="prod";

while getopts ":dht:" option; do
    case $option in
        d) # set development mode
            environment="dev";;
        h) # display help
            help;
            exit;;
        \?) # Invalid option
            echo "Error: Invalid option"
            exit;;
   esac
done

if [[ $environment == "dev" ]]; then
    if [ ! -d venv ]; then
        python3.9 -m venv venv;
    fi;
    echo ">>> source venv/bin/activate;"
    source venv/bin/activate;
    echo ">>> source .env;"
    source .env;
    sleep 0.5
fi;


# Install dependencies
echo ">>> python3 --version"
python3.9 --version
echo ">>> pip3 --version"
pip3 --version
echo ">>> pip3 install --upgrade pip;"
pip3 install --upgrade pip;
echo ">>> pip3 install -r requirements.txt;"
pip3 install -r requirements.txt;
sleep 0.5

# Run migrations
# echo ">>> bash scripts/migrate.sh;"
# bash scripts/migrate.sh;
# sleep 0.5

echo ">>> End of install.sh script"
