#!/usr/bin/env bash

setup_git() {
  COMMIT_AUTHOR_EMAIL=$(git log ${TRAVIS_COMMIT}^! --format='%ae')
  git config --global user.email "${COMMIT_AUTHOR_EMAIL}"
  git config --global user.name "Travis CI"
}

DOC_BRANCH=documentation

commit_website_files() {
  git checkout --orphan ${DOC_BRANCH}
  git reset # By default all the files will be added to the index

  # Copy the files we want to commit
  cp doc/_source _source.new -r
  cp doc/blender_objects.inv blender_objects.inv.new

  # Clean all the files and pull from remote
  git clean -fd
  git pull origin ${DOC_BRANCH}

  # Move the copied files back
  mv _source.new doc/_source
  mv blender_objects.inv.new doc/blender_objects.inv

  # Add files and commit
  git add doc/_source
  git add doc/blender_objects.inv
  git commit --message "Travis build: $TRAVIS_BUILD_NUMBER [skip ci]"
}

upload_files() {
  git push --force --quiet --set-upstream "https://${GH_TOKEN}@github.com/wisaac407/shotgun.git" ${DOC_BRANCH}
}

setup_git
commit_website_files
upload_files
