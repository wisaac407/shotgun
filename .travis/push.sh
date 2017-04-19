#!/usr/bin/env bash

setup_git() {
  COMMIT_AUTHOR_EMAIL=$(git log ${TRAVIS_COMMIT}^! --format='%ae')
  git config --global user.email "${COMMIT_AUTHOR_EMAIL}"
  git config --global user.name "Travis CI"
}

DOC_BRANCH=documentation

commit_website_files() {
  git checkout --orphan ${DOC_BRANCH}

  # Copy the files we wan't to commit
  cp doc/_source doc/_source.new -r
  cp doc/blender_objects.inv doc/blender_objects.inv.new

  rm doc/_source -rf
  rm doc/blender_objects.inv

  git pull origin documentation

  # Move the copied files back
  mv doc/_source.new doc/_source
  mv doc/blender_objects.inv.new doc/blender_objects.inv

  git add doc/_source
  git add doc/blender_objects.inv
  git commit --message "Travis build: $TRAVIS_BUILD_NUMBER [skip ci]"
}

upload_files() {
  git push --force --quiet --set-upstream "https://${GH_TOKEN}@github.com/wisaac407/shotgun.git" documentation
}

setup_git
commit_website_files
upload_files
