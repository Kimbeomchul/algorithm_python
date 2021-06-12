## 코딩테스트 연습쟝 ...

### https://solved.ac/profile/mickey1102



#### 메모이제이션
from functools import lru_cache
@lru_cache(maxsize = None)

#### heapq 
import heapq
heapq.heappop(heap)
heapq.heappush(heap, item)
heapq.heapify(heap)

#### 리스트 
# 방법 1 - itertools.chain
import itertools
list(itertools.chain.from_iterable(my_list))

# 방법 2 - itertools와 unpacking
import itertools
list(itertools.chain(*my_list))

# 방법 3 - list comprehension 이용
[element for array in my_list for element in array]

# 방법 4 - reduce 함수 이용 1
from functools import reduce
list(reduce(lambda x, y: x+y, my_list))

# 방법 5 - reduce 함수 이용 2
from functools import reduce
import operator
list(reduce(operator.add, my_list))
