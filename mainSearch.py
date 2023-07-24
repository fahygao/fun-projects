import pandas as pd


import subprocess

if __name__ == "__main__":
    # main()
    while True:
        search = input("你想搜什么梗词？")
        if search:
            print(f'收到，您想搜的梗词为 {search}')
        else:
            print("退出成功！")
            break
