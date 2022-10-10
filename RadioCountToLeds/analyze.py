def readLog(filename):
    count=0
    time=0
    totalLogList=[]
    logList=[]
    with open(filename, 'rb') as file_to_read:
        index=0
        for line in file_to_read:
            strLine= str(line)
            if (index>=3):
                    oneList=strLine.split( )
                    #print(oneList)
                    if (len(oneList)==4):
                        try:
                            row=[]
                            row.append(int(oneList[1]))
                            row.append(int(oneList[2]))
                            row.append(False)
                            row.append(0)
                            logList.append(row)
                            #print(oneList)
                        except:
                            pass
                    
            index=index+1
        
    with open(filename, 'rb') as file_to_read:
        counter=0
        currentCounter=0
        tempLogList=copy.deepcopy(logList)
        for line in file_to_read:
            strLine=str(line)
            splitLine=re.split(',|\.|\\r| ',strLine)
            if "Delay" in strLine:
                count=count+1
                #print (splitLine)
                a=splitLine[4].replace("\\r\\n'","")
                time=time+int(a)
            
        totalLogList.append(tempLogList)
        #print(totalLogList)
        a=float(time)/float(count)
        b=float((12-count))/12
        print("Average Transmit Delay:",a)
        print("Packet Loss Rate:",b)
        return totalLogList

    
if __name__ == "__main__":
    totalLogList=readLog("/opt/tinyos-2.1.2/apps/RadioCountToLeds/screen.log")
   
    
    
    
    
    
    
    


# In[ ]:




