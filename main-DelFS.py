from FN import FN

if  __name__ == '__main__':
    c1 = FN(workDir=r'E:\OneDrive - 微信公众号奇乐帮\考研视频\英语')
    exe = True
    #exe = False
    c1.analyzeExtensions()
    #print(c1.filesName)

    #更该文件夹名
    # c1.delDsStr('【www.zxit8.com】', '', exe)

    #更改文件名
    c1.delFsStr('【微信公众号：考研船】', '', exe)
    # print(c1.filesNum)

    #使用正则表达式更改文件名
    #c1.delFsStrWithRe('.+?(\d+：)(.+?)\(.+\)', exe)
    pass