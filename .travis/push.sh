#!/usr/bin/env bash

setup_git() {
  COMMIT_AUTHOR_EMAIL=$(git log ${TRAVIS_COMMIT}^! --format='%ae')
  git config --global user.email "${COMMIT_AUTHOR_EMAIL}"
  git config --global user.name "[skip ci] Travis CI"
}

commit_website_files() {
  git checkout -b documentation
  git add doc/_source
  git add doc/blender_objects.inv
  git commit --message "Travis build: $TRAVIS_BUILD_NUMBER"
}

upload_files() {
  git push --force --quiet --set-upstream "https://${GH_TOKEN}@github.com/wisaac407/shotgun.git" documentation
}

setup_git
commit_website_files
upload_files
