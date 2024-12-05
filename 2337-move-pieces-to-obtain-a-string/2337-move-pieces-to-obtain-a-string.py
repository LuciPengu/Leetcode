class Solution:
    def canChange(self, start: str, target: str) -> bool:
        lpos = []
        rpos = []
        ores = ""
        for i in range(len(start)):
            if start[i] == "L":
                lpos.append(i)
                ores += "L"
            if start[i] == "R":
                rpos.append(i)
                ores += "R"
        
        tlpos = []
        trpos = []
        opos = ""
        for i in range(len(target)):
            print(target[i])
            if target[i] == "L":
                tlpos.append(i)
                opos += "L"
            if target[i] == "R":
                trpos.append(i)
                opos += "R"
        
        try:
            for i in range(len(lpos)):
                if lpos[i] < tlpos[i]:
                    return False
        
            for i in range(len(rpos)):
                if rpos[i] > trpos[i]:
                    return False
        except:
            return False
            
        print(ores, opos)
        return ores == opos
