class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        visit = defaultdict(int)

        for cp in cpdomains:
            num, domain = cp.split(" ")
            num = int(num)

            parts = domain.split(".")
            for i in range(len(parts)):
                subdomain = ".".join(parts[i:])
                visit[subdomain] += num
        
        return [f"{v} {k}" for k, v in visit.items()]