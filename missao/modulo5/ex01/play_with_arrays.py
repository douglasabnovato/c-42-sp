#!/usr/bin/env python3

array_original = [2, 8, 0, 48, 8, 22, -12, 2]
indexMod = len(array_original) 

array_modified = [0] * indexMod
 
for numero in range(indexMod):
    array_modified[numero] = array_original[numero] + 2

print(f"Array original: {array_original}")
print(f"Array modificado: {array_modified}")