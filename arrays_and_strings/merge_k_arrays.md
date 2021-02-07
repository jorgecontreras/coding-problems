Given K sorted arrays, return their sorted concatenation.

_Example_

For arrays = `[[1, 3, 5]`, `[2, 3]`, `[2, 3, 5, 8]]`, the output should be
`mergeKArrays(arrays)` = `[1, 2, 2, 3, 3, 3, 5, 5, 8]`.

**Input/Output**

[execution time limit] 4 seconds (py3)

**[input] array.array.integer arrays**

An array of K one-dimensional sorted arrays.

Guaranteed constraints:
* 2 ≤ arrays.length ≤ 100,
* 0 ≤ arrays[i].length ≤ 100,
* -100 ≤ arrays[i][j] ≤ 100.

**[output] array.integer**
