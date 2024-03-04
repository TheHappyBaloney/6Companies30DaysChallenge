# 1600. Throne Inheritance

class ThroneInheritance:
    def __init__(self, kingName: str):
        self.g = defaultdict(list)
        self.dead = set()
        self.king = kingName

    def birth(self, parentName: str, childName: str) -> None:
        self.g[parentName].append(childName)

    def death(self, name: str) -> None:
        self.dead.add(name)

    def getInheritanceOrder(self) -> List[str]:
        def dfs(x):
            if x not in self.dead:
                ans.append(x)
            for y in self.g[x]:
                dfs(y)

        ans = []
        dfs(self.king)
        return ans


