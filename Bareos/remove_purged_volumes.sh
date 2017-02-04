#!/bin/bash
for f in `echo "list volume" | bconsole | grep Purged | cut -d ' ' -f6`; do
  echo "delete volume=$f yes" | bconsole;
  rm -rf /mnt/backup/$f;
done

