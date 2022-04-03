// FRUIT INTO BASKETS

/* You are visiting a farm that has a single row of fruit trees arranged from left to right. The trees are represented by an integer array fruits where fruits[i] is the type of fruit the ith tree produces.

You want to collect as much fruit as possible. However, the owner has some strict rules that you must follow:

You only have two baskets, and each basket can only hold a single type of fruit. There is no limit on the amount of fruit each basket can hold.
Starting from any tree of your choice, you must pick exactly one fruit from every tree (including the start tree) while moving to the right. The picked fruits must fit in one of your baskets.
Once you reach a tree with fruit that cannot fit in your baskets, you must stop.
Given the integer array fruits, return the maximum number of fruits you can pick.
*/
package main

func totalFruit(fruits []int) int {
	var left, right, bounty int

	baskets := make(map[int]int)
	for right < len(fruits) {
		if count, ok := baskets[fruits[right]]; ok {
			baskets[fruits[right]] = count + 1
		} else {
			baskets[fruits[right]] = 1
		}
		for len(baskets) > 2 {
			baskets[fruits[left]] -= 1
			if baskets[fruits[left]] == 0 {
				delete(baskets, fruits[left])
			}
			left += 1
		}
		right += 1
		if right-left > bounty {
			bounty = right - left
		}
	}

	return bounty
}
