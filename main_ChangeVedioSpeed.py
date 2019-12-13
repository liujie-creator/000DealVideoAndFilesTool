from CV import CV

if  __name__ == '__main__':
    d = r'E:\OneDrive - 微信公众号奇乐帮\考研视频\英语\2019年6月六级'
    cv1 = CV(workDir=d, sleepTime=10)
    speed = 1
    # speed = 1.1
    # speed = 1.2
    # speed = 1.3
    # speed = 1.4
    # speed = 1.5
    # speed = 1.6
    # speed = 1.8
    # speed = 2
    dealOldFilesMode = 0
    gpu = False
    cv1.dealV(speed, dealOldFilesMode, gpu, 8)
    pass