// Leetcode practice questions

// Twosum

import java.util.HashMap;
import java.util.Map;


class Solution {
    public int[] twoSum(int[] nums, int target) {

    // 1. Initialize a HashMap to track the presence of numbers.
    Map<Integer, Integer> NumsMap = new HashMap<>();

    // 2. Iterate through the array.
    for (int i=0; i < nums.length; i++){

    int Kataware = target - nums[i];
    // Calculate the kataware number

    if (NumsMap.containsKey(Kataware)){

        // Get the index of Kataware
        int KatawareIndex = NumsMap.get(Kataware);
        return new int[]{i,KatawareIndex};

    }

    NumsMap.put(nums[i],i);
    }
    return null;

}
}