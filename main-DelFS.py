from FN import FN

if  __name__ == '__main__':
    c1 = FN(workDir=r'G:\OneDrive - Office Everyday\视频教程\CAD\十天学会CAD 2007二维')
    exe = True
    #exe = False
    c1.analyzeExtensions()
    #print(c1.filesName)

    #更该文件夹名
    # c1.delDsStr('【www.zxit8.com】', '', exe)

    #更改文件名
    c1.delFsStr('_0', '', exe)
    # print(c1.filesNum)

    #使用正则表达式更改文件名
    #c1.delFsStrWithRe('.+?(\d+：)(.+?)\(.+\)', exe)
    pass