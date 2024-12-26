from typing import List


# My Solution
class Solution:
    class TrieNode:
        def __init__(self):
            self.is_end_of_folder = False
            self.children = {}

    def __init__(self):
        self.root = self.TrieNode()

    def removeSubfolders(self, folder):
        for path in folder:
            current_node = self.root
            folders = path.split("/")
            for folder_name in folders:
                if folder_name == "":
                    continue
                if folder_name not in current_node.children:
                    current_node.children[folder_name] = self.TrieNode()
                current_node = current_node.children[folder_name]
            current_node.is_end_of_folder = True
        result = []
        for path in folder:
            current_node = self.root
            folders = path.split("/")
            is_subfolder = False

            for i, folder_name in enumerate(folders):
                if folder_name == "":
                    continue
                next_node = current_node.children[folder_name]
                if next_node.is_end_of_folder and i != len(folders) - 1:
                    is_subfolder = True
                    break
                current_node = next_node
            if not is_subfolder:
                result.append(path)
        return result


# Best / Most Optimal Solution
class Solution2:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        result = []
        prev = ""
        for path in folder:
            if not prev or not path.startswith(prev + "/"):
                result.append(path)
                prev = path
        return result
