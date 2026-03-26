#To split a line into fields: Pipe the output of grep to utilities like awk or cut. awk is recommended for field splitting.
Using awk with a colon (:) delimiter:

echo "returned:first.last" | awk -F: '{ print $2 }'

