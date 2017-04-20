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
  cp doc/keymap_domain.py keymap_domain.py.new

  # Clean all the files and pull from remote
  git clean -fd
  git pull origin ${DOC_BRANCH}

  # Move the copied files back
  rm -rf doc/
  mv _source.new doc
  mv blender_objects.inv.new doc/blender_objects.inv
  mv keymap_domain.py.new keymap_domain.py

  # Add files and commit
  git add doc
  git add keymap_domain.py
  git commit --message "Travis build: $TRAVIS_BUILD_NUMBER"
}

upload_files() {
  git push --force --quiet --set-upstream "https://${GH_TOKEN}@github.com/wisaac407/shotgun.git" ${DOC_BRANCH}
}

setup_git
commit_website_files

# Avoid leaking GH_TOKEN (unfortunately this means loosing useful error messages)
if upload_files > /dev/null 2>&1; then
  echo "git push successful"
else
  echo "git push failed"
fi
