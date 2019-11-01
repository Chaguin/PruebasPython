# -*- coding: utf-8 -*-
def main():
    m=[[1,2,3],[4,5,6][7,8,9]]

    m[0][0]=3
    m[0][1]=2
    m[0][2]=1

    for i in range(len(m)):
        for j in range(len(m[i])):
            print(m[i][j]," ",end="")
        print()

main()