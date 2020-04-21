#!/bin/sh
# @desc Remote utils configuration
# @changed 2020.04.22, 00:06

export PROJECT_NAME="cron-downloader"
# export PROJECT_NAME=`basename "${PWD}"`

export DATE=`date "+%Y.%m.%d %H:%M:%S"`
export DATETAG=`date "+%y%m%d-%H%M"`

export PWD=`pwd`

export ARCDIR="../!ARC"
export REMOTE_ARCDIR="!ARC"

# Check for creditinals presence...
export PiServerPort="22" # Terminal connection port (may be sepcified in environment)
# Note: `$PiServerUser` and `$PiServerPw` taken from project environment
if [ -z "$PiServerUser" -o -z "$PiServerPw" -o -z "$PiServerPort" ]; then
  echo "Terminal creditinals must be specified in system environment!"
  exit 1
fi

# Commands configuration...
export PLINK_CMD="plink -C -P $PiServerPort -l $PiServerUser -pw $PiServerPw"
export CP_CMD="pscp -scp -r -C -P $PiServerPort -l $PiServerUser -pw $PiServerPw"

export ARC_CMD="tar czf"

export ROOTFILES="
  README.md \
  build-tag.txt \
  package*.json \
  requirements.txt \
  admin-install-requirements.sh \
  test.py \
"
  # index.js \

export REMOTE_TARGET_PATH="/home/pi/${PROJECT_NAME}" # Destination folder

export BUILD_TAG=`cat "./build-tag.txt"`
if [ -z "$BUILD_TAG" ]; then
  echo "Build tag must be defined!"
  exit 1
fi

export ARCNAME="$PROJECT_NAME-$BUILD_TAG.tgz"
