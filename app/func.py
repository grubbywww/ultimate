#! flask/bin/python
# -*- coding: utf-8 -*-
import paramiko
import os,sys,time
import threading
import os
import re
import yaml
from time import ctime,sleep
from config import ReadYaml
class TaskQueue():

    def __init__(self,hosts,option,task):
        self.hosts = hosts
        self.option = option
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.task = task
        self.port = 22 if "port" not in  self.option.keys() else self.option['port']
        self.username = 'root' if "ssh_remote_user" not in  self.option.keys() else self.option['ssh_remote_user']
        self.password = None if "ssh_remote_pass" not in  self.option.keys() else self.option['ssh_remote_pass']
        self.timeout = 1 if "timeout" not in self.option.keys() else  self.option['timeout']
        self.compress = False if "compress" not in  self.option.keys() else self.option['compress']
        if "key_path" not in self.option.keys():
            self.pkey = None
        else:
            self.ssh.load_system_host_keys()
            privatekey = os.path.expanduser(self.option['key_path'])
            self.pkey = paramiko.RSAKey.from_private_key_file(privatekey)

    def Connect(self,host):
    	try:
    		self.ssh.connect(hostname=host,port=self.port,username=self.username,password=self.password,pkey=self.pkey,timeout=self.timeout,compress=self.compress)
        except Exception,e:
            print str(e)

    def Transport(self,host):
        try:
            tp = paramiko.Transport((host,self.port))
            tp.connect(username=self.username,password=self.password,pkey=self.pkey)
            sftp = paramiko.SFTPClient.from_transport(tp)
            return sftp
        except Exception,e:
            print str(e)

    def Task(self,host):


        for i in self.task:
            if 'shell' in i.keys():
                self.Connect(host)
                if 'sudo' in self.option.keys():
                    cmd = 'sudo '+i['shell']
                else:
                    cmd = i['shell']
                try:
                    result = self.result(cmd)
                    results = re.sub('[\n]','<br>',result)
                    results = results.replace("successfully","<span class='label label-success'>successfully</span>")
                    results = results.replace("error","<span class='label label-danger'>ERROR</span>")
                    results = results.replace("failed","<span class='label label-danger'>FAILED</span>")
                    results = results.replace("warning","<span class='label label-danger'>WARNING</span>")
                    return results
                except Exception,e:
                    print str(e)
            elif 'copy' in i.keys():
                sftp = self.Transport(host)
                src = i['copy']['src']
                dest = i['copy']['dest']
                try:
                    sftp.put(src,dest)
                    #self.result(i['name'])
                    #print sftp.stat(dest)
                    #basedir = os.path.abspath(os.path.dirname(dest))
                    #print "\n".join(sftp.listdir(basedir))
                except Exception,e:
                    print str(e)

    def Run(self):

        nloops = range(len(self.hosts))
        for i in nloops:
            return self.Task(self.hosts[i])

    def result(self,cmd=''):
        if cmd is not None:
            stdin,stdout,stderr = self.ssh.exec_command(cmd)
            #print 10*"-"+"%2s" %(name)+10*"-"
            #print stderr.read()
            result = stdout.read()
            return result.lower()
def RunYaml():
    hosts = ['10.165.99.224']
    yaml = ReadYaml('/data/htdocs/ultimate/app/config.yaml')
    option = yaml.option()
    task = yaml.task()
    cmd = TaskQueue(hosts,option,task)
    result = cmd.Run()
    return result


def WriteYaml(dataMap):
    path = os.path.abspath(os.path.dirname(__file__))+"/../"
    file = "tmp.yaml"
    filename = path+file
    f = open(filename,"w")
    yaml.dump(dataMap, default_flow_style=False,stream=f,allow_unicode=True,tags=None)
    f.close()

