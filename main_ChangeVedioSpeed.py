from CV import CV

if  __name__ == '__main__':
    d = r'\\10.6.32.1\DShared\Cocos2dx游戏开发工程师'
    cv1 = CV(workDir=d, sleepTime=6)
    #speed = 1
    # speed = 1.1
    # speed = 1.2
    #speed = 1.3
    # speed = 1.4
    speed = 1.5
    #speed = 1.6
    #speed = 2
    dealOldFilesMode = 0
    gpu = False
    cv1.dealV(speed, dealOldFilesMode, gpu, 8)
    #cv1.dealV(speed = 2, dealOldFilesMode=1)
    
    #cv1.dealV(speed = 1.8, dealOldFilesMode=1)
    #cv1.dealV(speed = 1.6, dealOldFilesMode = 1)
    #cv1.dealV(speed = 1.5)
    #cv1.dealV(speed = 1.3, dealOldFilesMode = 1)
    #cv1.dealV(speed = 1.2, dealOldFilesMode = 1)
    #cv1.dealV(speed = 1, dealOldFilesMode=1)
    #print(os.getcwd())
    #print(sys.path[0])
    pass