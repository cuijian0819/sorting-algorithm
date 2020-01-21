## 0. Background
#### 1) Big-O Notation
**Definition**: A theoretical measure of the execution of an algorithm, usually the time or memory needed, given the problem size n, which is usually the number of items. Informally, saying some equation f(n) = O(g(n)) means it is less than some constant multiple of g(n). The notation is read, "f of n is big oh of g of n".  
**Formal Definition**: f(n) = O(g(n)) means there are positive constants c and k, such that 0 ≤ f(n) ≤ cg(n) for all n ≥ k. The values of c and k must be fixed for the function f and must not depend on n.

#### 2) Stability
**Definition**: A sorting algorithm is said to be **stable** if two objects with equal keys appear in the same order in sorted output as they appear in the input array to be sorted.

![alt](https://github.com/cuijian0819/sorting-algorithm/algorithm_chart.jpg)

|Algorithm|Time Compelxity|Best Case|Worst Case|Space Compelxity|Stability|
|---------|---------------|---------|----------|----------------|---------|
|Bubble Sort|O(n^2)|O(n)|O(n^2)|O(1)|Stable|
|Insertion Sort|O(n^2)|O(n)|O(n^2)|O(1)|Stable|
|Selection Sort|O(n^2)|O(n^2)|O(n^2)|O(1)|Unstable|
|Shell Sort|O(nlogn)|O(nlog^2n)|O(nlog^2n)|O(1)|Unstable|
|Quick Sort|O(nlogn)|O(nlogn)|O(n^2)|O(logn)|Unstable|
|Merge Sort|O(nlogn)|O(nlogn)|O(nlogn)|O(n)|Stable|

## 1. Bubble Sort
* Algorithm
  1. Compare two number next to each other, if the second one is larger than the first one, then swap.
  2. Do step 1 for all the numbers in the array.
  3. Repeat the steps above until the array is sorted.

## 2. Insertion Sort
* Algorithm
  1. Basically, divide the array into two parts: sorted and unsorted.
  2. From the first number to the last number, insert it in a appropriate position in the sorted part.
  3. Fisrt number keeps still since there is no number in the unsorted array.

## 3. Selection Sort
* Algorithm
  1. Basically, divide the array into two parts: sorted and unsorted.
  2. From the unsorted part, select the least number and insert in the end of the sorted part.
  3. Repeat step 2 from the first number to the last number.

## 4. Shell Sort
* Algorithm
  1. gap = length of array / 2 
  2. Compare two numbers with the distance of gap, swap them if the first one is bigger than the second one.
  3. If it is swapped, do step 2 for the previous two numbers with the distance of gap.
  4. Repeat step 2 and 3 by using the new gap = gap / 2

## 5. Quick Sort
* Alogrithm
  1. Select a random number from the whole array, we call it "pivot".
  2. Place the number smaller than pivot to the left side of the array. 
  3. Place the number bigger than the pivot to the right side of the array.
  4. Apply the steps above recursively to the left and right side of the array.

## 6. Merge Sort
* Alogrithm
  1. Divide the array into two child arrays with same length.
  2. Apply the algorithm to the two child arrays.
  3. Merge two sorted child arrays into one final sorted array.

## 7. Demo
* [topal](https://www.toptal.com/developers/sorting-algorithms)
* [webhack](http://www.webhek.com/post/comparison-sort.html) (Chinese)

## 8. Reference
* https://blog.csdn.net/weixin_41190227/article/details/86600821
* https://gitee.com/liyu-liyu-666/PythonAlgorithm

