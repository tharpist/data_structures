class Slow_solution:
    def twoSum(self, nums, target):
        print(f"The range is: ", len(nums))
        for num in range(len(nums)):
            print(f"first: ", num)
            for num2 in range(num + 1, len(nums)):
                print(f"second: ", num2)
                answer = nums[num] + nums[num2]
                if answer == target:
                    print("success")
                    return [num,num2]
                else:
                    print("error")
                              
                
class Fast_solution:
    def two_sum(self,nums,target):
        table={}
        for index,num in enumerate(nums):
            poop = target-num
            if poop in table:
                print(table)
                return [index,table[poop]]
            else:
                table[num]=index
                    
        return []


nums = [8,2,4,5]
target = 9


#brute = Slow_solution()
#brute.twoSum(nums, target)

nice = Fast_solution(
nice.two_sum(nums, target)