# -*- coding: utf-8 -*-

import os
import plistlib
import shutil
import subprocess

from contextlib import contextmanager


BUILD_DIR = 'wfbuild'
WF_FILES = [
  'bin',
  'icon.png',
  'info.plist',
  'README.md',
  'scripts',
]


def copy(filenames, dest_folder):
  if os.path.exists(dest_folder):
    shutil.rmtree(dest_folder)
  os.makedirs(dest_folder)

  for filename in filenames:
    if os.path.isdir(filename):
      shutil.copytree(filename, f'{dest_folder}/{filename}')
    else:
      shutil.copy(filename, f'{dest_folder}/{filename}')


def plistRead(path):
  with open(path, 'rb') as f:
    return plistlib.load(f)


def plistWrite(obj, path):
  with open(path, 'wb') as f:
    return plistlib.dump(obj, f)


def fileRead(path):
  with open(path) as f:
    return f.read()


def fileWrite(contents, path):
  with open(path, 'w') as f:
    f.write(contents)


@contextmanager
def cwd(dir):
  old_wd = os.path.abspath(os.curdir)
  os.chdir(dir)
  yield
  os.chdir(old_wd)

  
def make_export_ready(plist_path):
  wf = plistRead(plist_path)

  # remove noexport vars
  wf['variablesdontexport'] = []

  with open('README.md') as f:
    wf['readme'] = f.read()

  plistWrite(wf, plist_path)
  return wf['name']


if __name__ == '__main__':
  copy(WF_FILES, BUILD_DIR)
  plist_path = f'{BUILD_DIR}/info.plist'
  fileWrite(fileRead(plist_path).replace('listfiles.sh', 'firstrun.sh'), plist_path)
  wf_name = make_export_ready(plist_path)
  with cwd(BUILD_DIR):
    subprocess.call(
      ['zip', '-q', '-r', f'../{wf_name}.alfredworkflow'] + WF_FILES
    )
