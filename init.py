import socket as s
try:
    import urllib3
except:
    import urllib
    
import os
import sqlite3
import _thread

def about_project():
    return '''
            <h3>TCP/IP Server - HTTP project (Python)</h3><p>
            <h4>Introduction</h4><br>
            <p>This project aims at understanding how tcp/ip sockets work by use of http headers.<br>The main client for
            this server is a web browser. The server serves at a default port 2000.<br> The default ip is 0.0.0.0, meaning it can accept any ip range assigned by the host
            machine. All the pages served are made of html, css and js. The forms are processed in either http get or post<br> methods.</p>
            <h4>Server Features</h4><br>
            <ul>
            <li>GET and POST methods support- The server can receive both GET and POST through request('http_request_string') inbuilt function. </li>
            <li>Multithreading- This server is capable of handling many clients at a go.</li>
            <li>SQLITE3 support- the server has a default sqlite3 database support.</li>
            <li>HTML file serving support- The server is able to host and serve third party html files. These files should be pasted in the<br> 'public/' folder in the
            server root directory.</li>
            <li>Loading image files -ther server is able to load jpg/png/gif image files-this files should be included in the public folder.</li>
            <li>Video streaming support- video formarts such as mp4/5, mkv,3gp are supported.</li>
            <li>Restiful API's support- if you are looking to build an api for some system, this server can act as a template for start off.</li>
            </ul>
            <p><h4>Licence</h4><br>
            <p>This software is licenced under LGPL licence. You may read the licence <a href='https://google.com?q=LGPL+LICENCE' target='_blank'>online</a> to see what it is comprised of.</p>
            <h4>Developer</h4><br>
            <p>This software is developed by Kelvin Mwangi Magochi.<br> You can get in touch with him at Tel: +254718265708 or E-mail: admin@webninjaafrica.com.</p><br>
            
            <

        '''

def template(co,current,user=""):
    menu=""
    content="""
    <!DOCTYPE html>
    <html>
    <head><meta name='viewport' content='width=device-width; initial-scale=1.0'><title>SERVER | """+current+"""</title>"""
    content+="""
    <link rel="stylesheet" type="text/css" href="css/fonts/font-awesome.css">
    <link rel="stylesheet" type="text/css" href="css/helper.css">
    <style type="text/css">
    body{margin: 0px; padding: 0px; font-family: Arial,Tahoma; font-size: 0.9599em;}
    .main{width: 100%; margin: 0px; padding: 0px; min-height: 467px;}
    .left,.right{ float: left; min-height: 766px;  }
    .left{ width: 18%; border-left: 1px solid grey; background: #323232; position: fixed; }
    .right{width: 81.897%; border: 1px solid black; margin-left: 18%;}
    .menu{margin: 0px; padding: 0px;}
    """
    content+="""
    .menu li{ list-style-type: none; width: 100%;   border-bottom: 1px solid grey;}
    .menu li a{padding:3px; padding-left:3px;font-weight:bold; display: block; cursor: pointer; text-decoration: none; color: #e3e3e3; background: rgba(23,200,90,.12); height: 25px;line-height: 23px;}
    .menu li a:hover{ background: rgba(233,56,178,.156); color: white; font-weight: bold; }
    .profile{  width: 89%; padding: 3%; min-height: 98px; background: grey;  margin-top: 2px; margin-bottom: 24px; margin: 2%;}
    .below,.top{width: 96.09786%; padding: 2%; margin-top: 0px;}
    .top{ padding-top:3px;line-height:75%;height: 47px; border-bottom: 1px solid lightgrey; background: #e3e3e3; }
    .below{ min-height: 738px; } .thumb{ width: 90%;padding: 2%;margin-top: 0.2px; } 
    .cont{ width: 86%; padding: 3%; min-height: 5px; margin-top: -4%; }
    button{ background: #323232; color: #e9e9e9; border: none;padding: 5px; }
    .btn{width:116px;height:47px; text-decoration:none; padding:7px; border-radius: 5px; text-align:center;}
    .pry{ background: rgba(34,45,233,.899); color: white;}
    .pry:hover{ background: rgba(34,45,233,.69);}
    .btn:hover{ box-shadow: 1px 1px 1px 2px black;}
    </style></head><body><div class="main"><div class="left"><div class="profile">SOCKET SERVER<br>(TCP/IP)<br>ADMIN A/C</div>
    <ul class="menu"><li><a href="home"><i class="fa fa-tachometer"></i>&nbsp;&nbsp;&nbsp;DASHBOARD</a></li>
    <li><a href="new-user"><i class="fa fa-plus"></i>&nbsp;&nbsp;&nbsp;ADD USER</a></li><li>"""
    
    content+="""<a href="all-users"><i class="fa fa-users"></i>&nbsp;&nbsp;&nbsp;ALL USERS</a></li>
    """+menu+"""<li><a href="about-project"><i class="fa fa-info-circle"></i>&nbsp;&nbsp;&nbsp;ABOUT PROJECT</a></li>
    </ul></div><div class="right"><div class="top"><div class="thumb" style="margin-bottom: 34px;"><a href="/">/home/</a><a href="#">"""+current+"""</a>
    <form name="fa-search" style="margin-top: 2px;">"""
    content+="""<input type="text" name="q" id="search" style="margin-left: 35%;padding: 6px;width: 208px;border-radius: 4px;border-top-right-radius:0px;border: 1px solid grey;" placeholder="search a resource or a setting here!"><button type="submit" style="padding:6px;margin-bottom: 34px;"><i class="fa fa-search"></i> GO!</button></form></div>
    </div><div class="below"><div class="cont">"""+co+"""</div></div></div></div><script type="text/javascript" src="js/jquery.js"></script>
    <script type="text/javascript" src="js/datatables.js"></script>
    <script type="text/javascript" src="js/helper.js"></script></body></html>
    """
    return content



def db_init():
    if(os.path.exists("public/system/databases/sys_01.db")):
        db=''
    else:
        con=sqlite3.connect('public/system/databases/sys_01.db')
        cur=con.cursor()
        cur.execute("create table if not exists sys_users('user_id' varchar(20) not null, 'username' varchar(90) not null, 'password' varchar(1200) not null, 'role' varchar(7) not null)")
        con.commit()
        con=sqlite3.connect('public/system/databases/sys_01.db')
        cur=con.cursor()
        cur.execute("insert into sys_users(user_id,username,password,role) values(?,?,?,?)",('1','root','root','root'))
        con.commit()
    return "success"

def add_user(user_id,username,password,role):
        con=sqlite3.connect('public/system/databases/sys_01.db')
        cur=con.cursor()
        cur.execute("insert into sys_users(user_id,username,password,role) values(?,?,?,?)",(user_id,username,password,role))
        con.commit()
        return "success"
def update_user(user_id,username,password,role):
        con=sqlite3.connect('public/system/databases/sys_01.db')
        cur=con.cursor()
        cur.execute("update sys_users set user_id=?,password=?,role=? where username=?",(user_id,password,role,username))
        con.commit()
        return "success"
    
def login(username,password):
    con=sqlite3.connect('public/system/databases/sys_01.db')
    cur=con.cursor()
    cur.execute("select * from sys_users where username=? and password=?",(username,password))
    return len(cur.fetchall())

def user_details(username):
    con=sqlite3.connect('public/system/databases/sys_01.db')
    con.row_factory=sqlite3.Row
    cur=con.cursor()
    cur.execute("select * from sys_users where username=?",(username,))
    c=cur.fetchone()
    v={}
    try:
        v=dict(c)
    except:
        v={}
    return v



def remove_user(username):
    con=sqlite3.connect('public/system/databases/sys_01.db')
    con.row_factory=sqlite3.Row
    cur=con.cursor()
    cur.execute("delete from sys_users where username=?",(username,))
    con.commit()
    return "success"


def users():
    con=sqlite3.connect('public/system/databases/sys_01.db')
    con.row_factory=sqlite3.Row
    cur=con.cursor()
    cur.execute("select * from sys_users")
    
    c=cur.fetchall()
    html="""
        <p><a href='new-user' class='btn pry' style='padding:12px;margin-top:35px;'><i class='fa fa-user-o'></i> ADD NEW</a><p>
        <table cellpadding='5' border='1' style='width:100%;border-collapse:collapse;' id='users-table'><thead>
            <tr style='background:rgba(45,188,100,.98);color:#e9e9e9;'><th>User id</th> <th>username</th> <th>Role</th> <th>update</th><th>Remove</th></tr>
        </thead><tbody>"""
    for t in c:
        x=dict(t)
        html+="<tr><td>"+str(x['user_id'])+"</td> <td>"+str(x['username'])+"</td> <td>"+str(x['role'])+"</td> <td><a href='new-user?edit="+str(x['username'])+"'><i class='fa fa-edit'></i>&nbsp;&nbsp; Edit</a></td> <td><a href='remove?del="+str(x['username'])+"' style='color:red;'><i class='fa fa-trash'></i>&nbsp;&nbsp; Delete</a></td> </tr>"

    html+="</tbody></table>"
    return html
def redirect(file):
    return "HTTP/1.1 302 Found Location:"+str(file)+"\r\n\r\n"

def redirect_by_js(loc="all-users"):
    return "<noscript>FATAL ERROR! Please enable js to complete this operation.<br> Thank You.</noscript><script type='text/javascript'>window.location.href='"+loc+"';</script>"

def new_user(request={}):
    redirect=""
    user_id=username=user_role=password=error=disabled=""
    if("GET" in request):
        if ("edit" in request["GET"]):
            det=user_details(request["GET"]["edit"])
            disabled='readonly'
            if(len(det)>0):
                user_id=str(det['user_id'])
                username=str(det['username'])
                role="<option value='"+str(det['role'])+"'>"+str(det['role'])+"</option>"
                password=str(det["password"])
    if("POST" in request and request["REQUEST_METHOD"]=="POST"):
        
        if ("edit" in request["GET"]):
            error=update_user(request['POST']['user_id'],request['POST']['username'],request['POST']['password'],request['POST']['role'])
            redirect="<script type='text/javascript'>alert('user details changed!'); </script>"+redirect_by_js()
            
        else:
            if(len(user_details(request['POST']['username'])) >0):
                error="<div style='padding:6px;border:1px solid tomato;color:tomato;background:lightgrey;'>Error. The user already exists in the database.</div>"
            else:
                error=add_user(request['POST']['user_id'],request['POST']['username'],request['POST']['password'],request['POST']['role'])
                redirect="<script type='text/javascript'>alert('new user added to database!'); </script>"+redirect_by_js('new-user')
          
    htm='''
        <p><a href='all-users' class='btn pry' style='padding:12px;margin-top:35px;'><i class='fa fa-list'></i> ALL USERS</a><p>
        <form method='POST' class='frm' name='add-user' id='add-user'>
        <h4 style='color:#323232;'><i class='fa fa-plus'></i> USER INFORMATION</h4><p><hr><p>
        <style>
        body{background:#e9e9e9;}
        .frm{border:1px solid #e3e3e3;  padding:23px; margin:25px auto; background:white; box-shadow:1px 1px 1px 2px black;}
        table{ width:100%; font-size: 1.5em; color:grey; margin-top:24px auto;}
        td{padding:6px;}
        input{padding:15px; border:1px solid #323232; }
        button{background: rgb(112,23,56); color:white; padding:7px;} .pad43{ margin-left:50.3%;}
        input,select{ padding: 12px; width:297px; border-top-right-radius:5px; border-top-left-radius:5px; border: 2px solid grey;}
    
        select{width:325px;}
        input:focus{border: 2px solid  rgb(112,23,56); }
        </style>
        '''+error+'''
        
        <table>
        <tr><td>user id</td> <td><input type='text' name='user_id' value="'''+user_id+'''" required='required'></td></tr>
        <tr><td>username</td> <td><input type='text' name='username' value="'''+username+'''"  required='required' '''+disabled+'''></td></tr>
        <tr><td>user role</td> <td>
        <select name='role' required='required'>
        '''+user_role+'''
        <option value='root'>root/</option>
        <option value='guest'>guest</option>
        </select>
        </td></tr>
        <tr><td>password</td> <td><input type='text' name='password' value="'''+password+'''"  required='required'></td></tr>
        </table>
        <button type='submit' class='btn pad43'><b class='fa fa-save'></b> SAVE</button>
        '''+redirect+'''
        </form>

    '''
    return {"html":htm,"redirect":""}

def request(req):
    datar={}
    postb=req
    req=req.split('\n')
    z=req[0].split(" ")
    
    
    if(len(z)>2):
        datar['REQUEST_METHOD']=z[0]
        datar['REQUEST_FILE']=z[1].lstrip('/')
        datar['HTTP_VERSION']=z[2].rstrip('\r')
    else:
        datar['REQUEST_FILE']="/"
        datar['HTTP_VERSION']="HTTP/1.0"
        datar['REQUEST_METHOD']="GET"
    da={}
    get=datar['REQUEST_FILE'].split("?")
    if(len(get)>0):
        datar['REQUEST_FILE']=get[0]
        if(len(get)>1):
            
            for f in get[1].split("&"):
              
                g=f.split("=")
                if(len(g)>1):
                    da[g[0]]=g[1]
                else:
                    da[f]=""
                    
    
            
        datar['GET']=da

    d=postb.split("\r\n\r\n")
    if(len(d) >0 and z[0]=="POST"):
       
        ppi={}
        c=d[1].split('&')
        for y in c:
            postdata=y.split("=")
            if(len(postdata) >1):
                ppi[postdata[0]]=postdata[1]
            else:
                 ppi[y]=""
        datar['POST']=ppi
    for t in range(1,len(req)):
        f=req[t].split(":")
        if(len(f)==2):
            datar[f[0]]=f[1].replace('\r','')
        if(len(f) >2 and f[0]=="Host" or f[0]=="host"):
            datar[f[0]]=str((f[1]))+':'+str(f[2]).replace('\r','')
    return datar

def remove(req={},loc="all-users"):
    if "del" in req["GET"]:
        username=req["GET"]["del"]
        d=remove_user(username)
        resp=redirect_by_js(loc)
        return resp
    else:
        return redirect_by_js("login/")

def response(response,cmd="txt",content_type="text/html"):
    hd1='HTTP/1.0 200 ok\r\n'
    if(os.path.exists('public')):
        mm=''
    else:
        os.mkdir('public')
        os.mkdir('public/css')
        os.mkdir('public/css/fonts')
        os.mkdir('public/js')
        os.mkdir('public/js/plugins')
        os.mkdir('public/system')
        os.mkdir('public/system/databases')
        db_init()
        
    if(cmd=="file"):
        request_file=response
        try:
            hd1='HTTP/1.0 200 ok\r\n'
            f=open('public/'+request_file,'rb')
            content=f.read()
            
            f.close()
            if(request_file.endswith(".css")):
                hd1+="content-type: text/css\r\n"
            elif(request_file.endswith(".js")):
                hd1+="content-type: text/javascript\r\n"
            elif(request_file.endswith(".png")):
                hd1+="content-type: image/png\r\n"
            elif(request_file.endswith(".PNG")):
                hd1+="content-type: image/PNG\r\n"
            elif(request_file.endswith(".jpg")):
                hd1+="content-type: image/jpg\r\n"
            elif(request_file.endswith(".JPG")):
                hd1+="content-type: image/JPG\r\n"
            elif(request_file.endswith(".gif")):
                hd1+="content-type: image/gif\r\n"
            elif(request_file.endswith(".GIF")):
                hd1+="content-type: image/GIF\r\n"
            elif(request_file.endswith(".mp4")):
                hd1+="content-type: video/mp4\r\n"
            elif(request_file.endswith(".3gp")):
                hd1+="content-type: video/3gp\r\n"
            elif(request_file.endswith(".mp5")):
                hd1+="content-type: video/mp5\r\n"
            elif(request_file.endswith(".jpeg")):
                hd1+="content-type: video/jpeg\r\n"
            elif(request_file.endswith(".mkv")):
                hd1+="content-type: video/mkv\r\n"
            elif(request_file.endswith(".xml")):
                hd1+="content-type: application/xml\r\n"
            elif(request_file.endswith(".json")):
                hd1+="content-type: application/json\r\n"
            elif(request_file.endswith(".api")):
                hd1+="content-type: aplication/json\r\n"
            elif(request_file.endswith(".html") or request_file.endswith(".htm")):
                hd1+="content-type: text/html\r\n"
            elif(request_file.endswith(".woff")):
                hd1+="content-type: application/x-font-woff\r\n"
            elif(request_file.endswith(".woff2")):
                hd1+="content-type: application/font-woff2\r\n"
            elif(request_file.endswith(".ttf")):
                hd1+="content-type: application/x-font-ttf\r\n"
            elif(request_file.endswith(".eot")):
                hd1+="content-type: application/vnd.ms-fontobject\r\n"
            elif(request_file.endswith(".svg")):
                hd1+="content-type: image/svg+xml\r\n"
            else:
                g=''
            
        except:
            hd1="HTTP/1.0 404 NOT FOUND\r\n"
            content="<html><head><title>Error</title></head><body><center><h2>404 NOT FOUND</h2></body></html>".encode('utf-8')
    else:
        content=response.encode('utf-8')
        hd1+="content-type: "+str(content_type)+"\r\n"
    hd1+="content-length:"+str(len(content))+"\r\n"
    hd1+="connection: close\r\n\r\n"
    
    data={"headers":hd1.encode('utf-8'),"content":content}
    return data

def load_user(cs,addr):
    data=cs.recv(1024*10000).decode('utf-8')
    req=request(data)
    co=response(req['REQUEST_FILE'],'file')
    if(req['REQUEST_FILE']=='new-user'):
        z=new_user(req)
        temp=template(z['html'],"NEW USER")
        co=response(temp,'txt')
        if(z['redirect']==""):
            p=''
        else:
            co['headers']=redirect_by_js(z['redirect']).encode("utf-8")
            co['content']="".encode("utf-8")
    #print(req['REQUEST_FILE'])
    if(req['REQUEST_FILE']=='all-users'):
        co=response(template(users(),"ALL USERS"))
    if(req['REQUEST_FILE']=='remove'):
        co=response(template(remove(req),"Delete Request"))
    
    if(req['REQUEST_FILE']=='' or req['REQUEST_FILE']=='/' or req['REQUEST_FILE']=='index'):
        co=response(template(redirect_by_js('about-project'),"EXIT"))

    if(req['REQUEST_FILE']=='about-project'):
        co=response(template(about_project(),"ABOUT THIS PROJECT"))   

    if(req['REQUEST_FILE']=='home'):
        co=response(template("WELCOME TO DASHBOARD","HOME"))

    if(req['REQUEST_FILE']=='api'):
        js='{"names":"doe","addr":"juja"}'
        co=response(js,'txt','application/json')
    
    cs.sendall(co['headers']+co['content'])

    
inbuilt=['login/','system/']   
PORTNO=2000
ADDR='0.0.0.0'
app=s.socket(s.AF_INET,s.SOCK_STREAM)
app.setsockopt(s.SOL_SOCKET,s.SO_REUSEADDR,1)
app.bind((ADDR,PORTNO))
app.listen(2000)
try:
    print("Welcome To HTTP (TCP/IP) Ptython server project\n This server is able to serve html pages. To load you html pages. Please paste the pages at 'public' folder  created next to this executable file.\nThis software is developed by Kelvin Mwangi Magochi.\nYou can get in touch with him at Tel: +254718265708 or E-mail: admin@webninjaafrica.com\n This server is running at a default port of: "+str(PORTNO)+" and an address: "+str(ADDR)+"\n to run the server pages on your web browser, please type http://localhost:"+str(PORTNO)+"\n")

except:
    h=''
    #print "Welcome To HTTP (TCP/IP) Ptython server project\n This server is running at a default port of: "+str(PORTNO)+" and an address: "+str(ADDR)+"\n to run the server pages on your web browser, please type http://localhost:"+str(PORTNO)+"\n"
while 1:
    cs, addr=app.accept()
    

    e=_thread.start_new_thread(load_user,(cs,addr))
    #e.join()
    #load_user(data,cs,addr)
    

app.close()
