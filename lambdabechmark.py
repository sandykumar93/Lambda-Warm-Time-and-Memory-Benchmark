import boto3,time,json,datetime,base64

client = boto3.client('lambda',region_name='us-east-1')

def runlambda(lambdaname,payload):
    returnthis={}
    a=datetime.datetime.now()
    response = client.invoke(
        FunctionName=lambdaname,
        InvocationType='RequestResponse',
        LogType='Tail',
        Payload=json.dumps(payload)
    )
    b=datetime.datetime.now()
    
    #print("--> Client Invoke Boto Call Time + Lambda Execution Time - "+ str(b-a) ) 
    
    z=(json.dumps(response,indent=4,default=str))
    z=json.loads(z)
    z=base64.b64decode(z['LogResult'])
    z=z.splitlines()
    z=z[-1].split("REPORT")[1]
    print("--> Lambda Execution Info")
    c=z.split('\t')
    for i in c:
        if "RequestId" not in i and i!='':
            print("    --> "+i)
            i=i.split(":")
            returnthis.update({i[0]:i[1]})
            
    return returnthis

def updatelambdaconfig(lambdaname,size):
    response = client.update_function_configuration(
        FunctionName=lambdaname,
        MemorySize=size
        )

def timeloop(waitTime):
    print("--> Current Time - "+ str(datetime.datetime.now()))
    results.append(runlambda(lambdaname,paylaod))
    print("--> Next Execution in %s min\n" %(waitTime))
    time.sleep(waitTime*60)
    

def checkwarmtime():
    for i in timeinmin:
        timeloop(i)

def checkoptimalmemory():
    for x in memory:
        updatelambdaconfig(lambdaname,x)
        #cold run
        print("\nCold Start - " + str(x) + "MB")
        results.append(runlambda(lambdaname,paylaod))
        #warm run
        print("\nWarm Start - " + str(x) + "MB")
        results.append(runlambda(lambdaname,paylaod))

    updatelambdaconfig(lambdaname,memory[0])


lambdaname='lambdaname'
memory=[128,256,384,512,640,768,832]
timeinmin=[5,10,15,20,25,30]
paylaod={
  "key1": "value1",
  "Key2": "value2",
  "key3": "value3"
}
results=[]


#Invoke the below function to check optimal lambda memory
#checkoptimalmemory()

#Invoke the below function to check lambda warm time
checkwarmtime()

#Final Results are stored in "results" variable
#print(json.dumps(results, indent=4))

