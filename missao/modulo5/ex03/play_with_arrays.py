#!/usr/bin/env python3

array_original = [2, 8, 9, 48, 8, 22, -12, 2]
indexMod = len(array_original) 

array_modified = []
 
for numero in range(indexMod):
    if array_original[numero] > 5:
        array_modified.append(array_original[numero] + 2)

print(f"Array original: {array_original}")
print(f"Array modificado: {array_modified}")

array_modified_set = set(array_modified)

print(f"Array modificado SET: {array_modified_set}")