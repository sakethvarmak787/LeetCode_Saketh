class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        # Split the strings into lists of revisions
        v1_revisions = version1.split('.')
        v2_revisions = version2.split('.')
        
        n1 = len(v1_revisions)
        n2 = len(v2_revisions)
        
        # Iterate through the maximum number of revisions present
        for i in range(max(n1, n2)):
            # Get integer value or 0 if index is out of bounds
            rev1 = int(v1_revisions[i]) if i < n1 else 0
            rev2 = int(v2_revisions[i]) if i < n2 else 0
            
            if rev1 > rev2:
                return 1
            elif rev1 < rev2:
                return -1
        
        # If we reach here, all revisions were equal
        return 0