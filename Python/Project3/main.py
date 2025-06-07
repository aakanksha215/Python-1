# 

import pywhatkit as pw 

txt = """ Add two or more quantum states and the result will be another valid quantum state. 
Every quantum state can be represented as a sum of two or more other distinct states. """

pw.text_to_handwriting(txt, "demo1.png", [0,0,138])
print("Executed")
