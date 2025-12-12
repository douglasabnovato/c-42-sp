#!/usr/bin/env python3

import sys
import re 

output = "none"
  
if len(sys.argv) == 3: 
    keyword = sys.argv[1]  
    target_string = sys.argv[2] 
      
    occurrences_list = re.findall(keyword, target_string)
     
    count = len(occurrences_list) 
    
    if count > 0: 
        output = str(count)
 
print(output)
