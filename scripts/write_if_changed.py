import os
import sys

def write_if_changed(new, path):
  if os.path.exists(path):
    with open(path, 'r', encoding='utf-8') as f:
      old = f.read()
    if old == new:
      return False
  with open(path, 'w', encoding='utf-8') as f:
    f.write(new)
  return True

sys.modules[__name__] = write_if_changed