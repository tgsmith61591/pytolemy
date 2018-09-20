#!/usr/bin/env bash

# remove due to Travis build issue 6307
# set -e
set +e  # because Travis can't get its act together

# if it's a linux build, we need to apt-get update
if [[ "$TRAVIS_OS_NAME" == "linux" ]]; then
  echo "Updating apt-get for Linux build"
  sudo apt-get -qq update


  # This is a hack, and a result of the way Bear auto-generates this script
  # if C is required. false is formated in by the __main__
  echo "Downloading gcc, g++ & gfortran"
  sudo apt-get install -y gcc
  sudo apt-get install -y g++
  sudo apt-get install -y gfortran
  sudo apt-get install libgdal1-dev

# Workaround for https://github.com/travis-ci/travis-ci/issues/6307, which
# caused the following error on MacOS X workers:
#
# Warning, RVM 1.26.0 introduces signed releases and automated check of
# signatures when GPG software found.
# /Users/travis/build.sh: line 109: shell_session_update: command not found
elif [[ "$TRAVIS_OS_NAME" == "osx" ]]; then
  echo "Updating Ruby for Mac OS build"

  # stupid travis
  command curl -sSL https://rvm.io/mpapis.asc | gpg --import -;
  rvm get stable

  # See Travis issue (yes another) 8826
  # https://github.com/travis-ci/travis-ci/issues/8826
  brew cask uninstall oclint
  # This should yield the following:
  # ==> Uninstalling Cask oclint
  # ==> Unlinking Binary '/usr/local/bin/oclint'.
  # ==> Unlinking Binary '/usr/local/bin/oclint-json-compilation-database'.
  # ==> Unlinking Binary '/usr/local/bin/oclint-xcodebuild'.
  # ==> Unlinking Binary '/usr/local/lib/oclint'.
  # ==> Unlinking Binary '/usr/local/include/c++'.

  # After oclint is uninstalled, we should be able to install GCC
  brew install gcc

  # Maybe install GDAL
  # brew install gdal || echo "GDAL might already be installed?"
  # We need version 2.3.1
  brew upgrade gdal || echo "GDAL might be up-to-date"

  # Set the C++ path per this issue: https://github.com/openMVG/openMVG/issues/316
  export CPLUS_INCLUDE_PATH="/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/include/c++/v1/"
fi
