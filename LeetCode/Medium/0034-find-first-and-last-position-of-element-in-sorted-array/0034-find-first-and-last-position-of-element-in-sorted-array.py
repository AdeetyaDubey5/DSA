class Solution:
    def fst(self,arr,x):
        l , r = 0 , len(arr) - 1 
        fst_occurence = -1
        while (l<=r):
            mid = l + (r-l)//2
            if (arr[mid] == x):
                fst_occurence = mid
                r = mid - 1
            elif (arr[mid] > x):
                r = mid - 1 
            else:
                l = mid + 1 
        return fst_occurence

    def lst(self,arr,x):
        l , r = 0 , len(arr) - 1 
        lst_occurence = -1
        while (l<=r):
            mid = l + (r-l)//2
            if (arr[mid] == x):
                lst_occurence = mid
                l = mid + 1
            elif (arr[mid] > x):
                r = mid - 1 
            else:
                l = mid + 1 
        return lst_occurence
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ft = self.fst(nums,target)
        lt = self.lst(nums,target)

        return [ft , lt]
        
        