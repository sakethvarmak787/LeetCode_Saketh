class Solution:
    def kthSmallestPrimeFraction(self, arr, k):
        # Step 1: Create a list to store ALL possible fractions
        # Each element will be:
        # (fraction_value, numerator, denominator)
        fractions = []
        
        n = len(arr)
        
        # Step 2: Generate all possible fractions
        # Outer loop picks numerator
        for i in range(n):
            # Inner loop picks denominator
            # We start from i+1 to ensure numerator < denominator
            for j in range(i + 1, n):
                
                # Compute the fraction value
                value = arr[i] / arr[j]
                
                # Store the fraction along with numerator and denominator
                fractions.append((value, arr[i], arr[j]))
                
                # ------------------ DRY RUN ------------------
                # Example: arr = [1,2,3,5]
                #
                # i = 0 → arr[i] = 1
                # j = 1 → arr[j] = 2 → value = 1/2 = 0.5 → store (0.5,1,2)
                # j = 2 → arr[j] = 3 → value = 1/3 ≈ 0.333 → store (0.333,1,3)
                # j = 3 → arr[j] = 5 → value = 1/5 = 0.2 → store (0.2,1,5)
                #
                # i = 1 → arr[i] = 2
                # j = 2 → 2/3 ≈ 0.666 → store
                # j = 3 → 2/5 = 0.4 → store
                #
                # i = 2 → arr[i] = 3
                # j = 3 → 3/5 = 0.6 → store
                # ---------------------------------------------
        
        # Step 3: Sort all fractions based on their value
        # Sorting ensures smallest fraction comes first
        fractions.sort(key=lambda x: x[0])
        
        # ------------------ DRY RUN ------------------
        # Before sorting:
        # [(0.5,1,2), (0.333,1,3), (0.2,1,5), (0.666,2,3), (0.4,2,5), (0.6,3,5)]
        #
        # After sorting:
        # [(0.2,1,5), (0.333,1,3), (0.4,2,5), (0.5,1,2), (0.6,3,5), (0.666,2,3)]
        # ---------------------------------------------
        
        # Step 4: Pick the k-th smallest fraction
        # Since list is 0-indexed → k-th element is at index (k-1)
        kth_fraction = fractions[k - 1]
        
        # kth_fraction = (value, numerator, denominator)
        
        # Step 5: Return numerator and denominator
        return [kth_fraction[1], kth_fraction[2]]
        
        # ------------------ DRY RUN ------------------
        # k = 3 → index = 2
        # fractions[2] = (0.4, 2, 5)
        #
        # return [2, 5]
        # ---------------------------------------------