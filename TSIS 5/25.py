import re
def Sol(dt):
        return re.sub(r'(\d{4})-(\d{1,2})-(\d{1,2})', '\\3-\\2-\\1', dt)
ans = "2026-01-02"
print("Original date in YYY-MM-DD Format: ",ans)
print("New date in DD-MM-YYYY Format: ",Sol(ans))
