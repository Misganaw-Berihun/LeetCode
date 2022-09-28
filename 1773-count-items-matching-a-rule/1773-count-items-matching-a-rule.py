class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        type_cnt = defaultdict(int)
        color_cnt = defaultdict(int)
        name_cnt = defaultdict(int)
        
        for item in items:
            type_cnt[item[0]] += 1
            color_cnt[item[1]] += 1
            name_cnt[item[2]] +=1 
        
        if ruleKey == 'type':
            return type_cnt[ruleValue]
        elif ruleKey == 'color':
            return color_cnt[ruleValue]
        else:
            return name_cnt[ruleValue]