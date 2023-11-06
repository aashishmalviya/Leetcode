class Solution:
    def simplifyPath(self, path: str) -> str:
        dirAndFiles = []
        
        path = path.split("/")
        
        for current_item in path:
            if dirAndFiles and current_item == "..":
                dirAndFiles.pop()
            elif current_item not in ["", ".", ".."]:
                dirAndFiles.append(current_item)
                
        return "/" + "/".join(dirAndFiles)