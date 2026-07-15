import sys
f = 'app/hooks/useExamState.ts'
data = open(f, 'rb').read()
lines = data.split(b'\n')
print('Line 172 before:', repr(lines[171]))
# Replace the corrupted Chinese string with correct UTF-8 encoding
lines[171] = b'        console.error("\xe8\x8e\xb7\xe5\x8f\x96\xe5\x8f\x82\xe8\x80\x83\xe7\xad\x94\xe6\xa1\x88\xe5\xa4\xb1\xe8\xb4\xa5", error);'
print('Line 172 after:', repr(lines[171]))
new_data = b'\n'.join(lines)
open(f, 'wb').write(new_data)
print('File updated successfully')
