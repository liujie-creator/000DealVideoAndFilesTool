from FN import FN

if  __name__ == '__main__':
    c1 = FN(workDir=r'D:\BaiduNetdiskDownload\500审阅\CocosCreator官方教学视频(腾讯超清版)[20180428更新]')
    exe = True
    #exe = False
    c1.analyzeExtensions()
    #print(c1.filesName)

    #更该文件夹名
    #c1.delDsStr('cocos2dx_advanced_l1_', '', exe)

    #更改文件名
    c1.delFsStr('Cocos Creator超清教程', '', exe)
    # print(c1.filesNum)

    #使用正则表达式更改文件名
    #c1.delFsStrWithRe('.+?(\d+：)(.+?)\(.+\)', exe)
    pass