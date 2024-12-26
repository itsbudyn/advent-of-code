# advent-of-code - Year 2024
### Completion
<b>Legend:  </b>
- ✅ · Completed
- 🔜 · Not attempted yet
- ❌ · Gave up

|**Task**|**1**|**2**|**3**|**4**|**5**|**6**|**7**|**8**|**9**|**10**|**11**|**12**|**13**|**14**|**15**|**16**|**17**|**18**|**19**|**20**|**21**|**22**|**23**|**24**|**25**|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|**1**|✅|✅|✅|✅|✅|✅|✅|✅|✅|✅|✅|✅|✅|✅|✅|✅|✅|✅|✅|✅|❌|✅|✅|✅|✅|
|**2**|✅|✅|✅|✅|✅|✅|✅|✅|✅|✅|✅|✅|✅|✅|✅|🔜|✅|✅|✅|✅|❌|✅|✅|🔜|🔜|

--- 
### Notes
|Day|Part|Notes|
|:-:|:-:|:---:|
|**23**|All|itertools.permutations my beloved|
|**22**|All|Completes both parts in 5.491s on 7600x. <br> For part 2, creates a dictionary of all sequences during secret generation, with their values being resulting prices from all monkeys. Also prevents the same sequence being used twice in the same monkey. In the end, just sum all of the prices per sequence and get the highest one.|
|**21**|All|Still, impressed that it took me this long to give up on an entire day, compared to previous AOC's. Enjoy my part 1 that will only work on example input.|
|**20**|**2**|Painfully slow. I have no idea on how to optimize this.|
|**19**|All|Recursion with LRU cache|
|**17**|**2**|By-Octal solution - Checks if lowest octal of initial A register, iterated from 0-7, will give a program output equal to the suffix of the program. If yes, it is multiplied by 0b10 (8), and pushed into a dict of valid initial A registers. Repeated untill output matches program 1:1. Instantly gives answer.|
|**16**|**2**|Not done, takes forever to complete|
|**16**|**1**|Incredibly hard for me, the solution is just god-awful. I'm just proud I got the star after so much work. 7.336s on 7600x|
|**12**|**2**|I was ***this*** close to giving up, but it ended up working in the end|
|**9**|**2**|21.586s on 7600x|
|**6**|**2**|23.431s on 7600x; 40.270s on i5-9300H|
