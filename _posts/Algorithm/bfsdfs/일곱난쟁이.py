import sys
import random

def main(dwarf_list: list) -> list:
    residual = sum(dwarf_list) - 100
    for dwarf_1 in dwarf_list:
        for dwarf_2 in dwarf_list:
            if dwarf_1 + dwarf_2 == residual:
                if dwarf_1==dwarf_2:
                    pass
                else:
                    dwarf_list.remove(dwarf_1)
                    dwarf_list.remove(dwarf_2)
                    dwarf_list.sort()                
                    return dwarf_list
                        
if __name__ == "__main__":
    input = sys.stdin.readline
    dwarf_list = [int(input().strip()) for _ in range(9)]
    rets = main(dwarf_list)
    for ret in rets:
        print(ret)