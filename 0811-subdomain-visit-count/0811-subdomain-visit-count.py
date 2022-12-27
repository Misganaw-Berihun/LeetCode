class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        domains = defaultdict(int)
        for domain in cpdomains:
            rep, website = domain.split(" ")
            subdomains = website.split('.')
                        
            for i in range(len(subdomains)):
                key = '.'.join(subdomains[i:])
                domains[key] += int(rep)
                
        return [str(domains[d]) + " " + str(d) for d in domains.keys()]
                