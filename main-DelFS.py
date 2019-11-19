from FN import FN

if  __name__ == '__main__':
    c1 = FN(workDir=r'D:\DS\传智播客.Net学院--特供精品.Net基础全套视频教程2014版')
    exe = True
    #exe = False
    c1.analyzeExtensions()
    #print(c1.filesName)

    #更该文件夹名
    c1.delDsStr('）', '', exe)

    #更改文件名
    # c1.delFsStr('Cocos Creator超清教程', '', exe)
    # print(c1.filesNum)

    #使用正则表达式更改文件名
    #c1.delFsStrWithRe('.+?(\d+：)(.+?)\(.+\)', exe)
    pass