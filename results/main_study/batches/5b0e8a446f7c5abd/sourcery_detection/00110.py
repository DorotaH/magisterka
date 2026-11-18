class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        edgeDict = {}
        for i, j in tickets:
            if i not in edgeDict:
                edgeDict[i] = []
            edgeDict[i].append(j)
        for i in edgeDict:
            edgeDict[i].sort(reverse=True)
        # Do Search
        retAns = []

        def searchNodes(currNode):
            print("Search:", currNode)
            if currNode not in edgeDict:
                retAns.append(currNode)
                return
            print(edgeDict[currNode])
            while (edgeDict[currNode]):
                searchNodes(edgeDict[currNode].pop())
            retAns.append(currNode)
        searchNodes("JFK")
        return retAns[::-1]
