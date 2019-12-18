import os,shutil,string,time

#coding:utf-8

# 只支持小文件
# global findCount
# findCount = 0
def gci(filepath,dstfilepath):
    files = os.listdir(filepath)
    # global findCount

    for f in files:
        # print(">>>" + os.path.split(filepath,f)[0])
        # fpath, fname = os.path.split(dstfile)  # 分离文件名和路径
        fileIn = os.path.join(filepath, f)
        if os.path.isdir(fileIn):
            gci(fileIn, dstfilepath)
        else:
            fileOutput = os.path.join(filepath,fileIn)
            # print(fileOutput)

            fopen = open(fileOutput, 'r', encoding='utf-8', errors='ignore')
            fContent = fopen.read()
            # print(fContent)
            # fopen.close()

            # time.sleep(3)

            if fContent.find("versionName=4.0.0") != -1:
                # print(fContent)
                fopen.close()
                if not os.path.exists(dstfilepath):
                    os.makedirs(dstfilepath)
                fpath, fname = os.path.split(fileOutput)  # 分离文件名和路径
                shutil.move(fileOutput, dstfilepath+fname)
                print("\r\n>>>move: " + '{0} {1} {2}'.format(fileOutput, "-->", dstfilepath+fname))
                # findCount += 1
            else:
                print("not found...")

    # print("findCount=",findCount)



# gci('源路径\\06\\','目的路径\\066\\')# open this run