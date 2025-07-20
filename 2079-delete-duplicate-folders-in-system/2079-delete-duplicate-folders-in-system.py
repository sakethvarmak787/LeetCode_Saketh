from typing import List
from collections import defaultdict

class TreeNode:
    def __init__(self):
        self.children = defaultdict(TreeNode)
        self.name = ""
        self.is_deleted = False

class Solution:
    def deleteDuplicateFolder(self, paths: List[List[str]]) -> List[List[str]]:
       
        root = TreeNode()
        for path in paths:
            node = root
            for folder in path:
                node = node.children[folder]
                node.name = folder
        
        
        serial_map = defaultdict(list)

        def serialize(node: TreeNode) -> str:
            if not node.children:
                return ""
            serial = []
            for child_name in sorted(node.children.keys()):
                child_serial = serialize(node.children[child_name])
                serial.append(f"{child_name}({child_serial})")
            serial_str = ''.join(serial)
            serial_map[serial_str].append(node)
            return serial_str

        serialize(root)

        
        for nodes in serial_map.values():
            if len(nodes) > 1:
                for node in nodes:
                    node.is_deleted = True

       
        res = []

        def collect(node: TreeNode, path: List[str]):
            for name, child in node.children.items():
                if not child.is_deleted:
                    path.append(name)
                    res.append(path[:])
                    collect(child, path)
                    path.pop()

        collect(root, [])
        return res
