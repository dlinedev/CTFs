# Python

```python
import math
print math.pow(18014398509481984,3) + math.pow(1, 3) \
      == math.pow(18014398509481983,3)
# it will return true      
```

It prints True because math.pow returns floating-point numbers, and these do not have enough precision to get the correct answer, False.

---

[“Disprove” Fermat's Last Theorem [closed]](https://codegolf.stackexchange.com/questions/32696/disprove-fermats-last-theorem)
