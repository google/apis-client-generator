#!/bin/bash
# Diff two files and PASS if they are equal, FAIL otherwise.
# Usage:
#   diff_test.sh path_to_expected path_to_got

# Find input files
declare -r EXPECTED="$1"
declare -r GOT="$2"

diff_out=$(mktemp /tmp/diff_test.XXXXXXXXX)
diff -cB "$EXPECTED" "$GOT" >"$diff_out"
err=0
if [[ -s "$diff_out" ]] ; then
  cat "$diff_out"
  err=1
  echo 'To update:'
  echo '  p4 edit ' "$EXPECTED"
  echo '  cp blaze-genfiles/'"$GOT" "$EXPECTED"
  echo FAIL
else
  echo PASS
fi
exit $err
