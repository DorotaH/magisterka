class Solution:
    def  simplifyPath(self, path: str) -> str:
        stack = []
        directory = ""

        for  c in  path+"/":
            if not c == "/":
                directory += c

            else:
                if directory == "..":
                    if stack:
                        stack.pop()
                elif directory != "" and directory != ".":
                    stack.append(directory)
                directory = ""
        
        return  "/" + "/".join(stack)
