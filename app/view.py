# -*- coding: utf-8 -*-
from app import app
from flask import render_template,flash,redirect,session,url_for,request,jsonify,g
from func import TaskQueue,RunYaml,WriteYaml
import datetime
import re
import json
import urllib
import urllib2
from urllib import unquote
import sys
reload(sys)
sys.setdefaultencoding('utf8')

@app.route('/',methods = ['GET','POST'])
@app.route('/main',methods = ['GET','POST'])
def main():
    return render_template("main.html",title = "自动化--旗舰版")
@app.route('/audiovideo',methods = ['POST'])
def audiovideo():
    tenantids = request.values.get('tenantids')
    total = request.values.get('total')
    if total == "":
        totalids = []
    else:
        totalid =  re.split("[,|\s+]",total)
        totalids = [int(i) for i in totalid]
    enable = request.values.get('enable')
    if enable == "":
        tag = ""
    else:
        tag = True
    if tenantids.strip() == "":
        tenantid = []
    else:
        td = re.split("[,|\s+]",tenantids)
        tenantid = [int(i) for i in td]
    dataMap = {
    "tenantids":list(totalids),
    "functions":{
    "audiovideo":{
    "enable":bool(tag),
    "tenantids":list(tenantid)
    }
    }
    }
    WriteYaml(dataMap)
    results = RunYaml()
    return jsonify(result = results)
@app.route('/waitlist',methods = ['POST'])
def waitlist():
    tenantids = request.values.get('tenantids')
    total = request.values.get('total')
    if total == "":
        totalids = []
    else:
        totalid =  re.split("[,|\s+]",total)
        totalids = [int(i) for i in totalid]
    enable = request.values.get('enable')
    if enable == "":
        tag = ""
    else:
        tag = True
    if tenantids.strip() == "":
        tenantid = []
    else:
        td = re.split("[,|\s+]",tenantids)
        tenantid = [int(i) for i in td]
    dataMap = {
    "tenantids":list(totalids),
    "functions":{
    "waitlistnumber":{
    "enable":bool(tag),
    "tenantids":list(tenantid)
    }
    }
    }
    WriteYaml(dataMap)
    results = RunYaml()
    return jsonify(result = results)
@app.route('/msgrecall',methods = ['POST'])
def msgrecall():
    tenantids = request.values.get('tenantids')
    total = request.values.get('total')
    if total == "":
        totalids = []
    else:
        totalid =  re.split("[,|\s+]",total)
        totalids = [int(i) for i in totalid]
    enable = request.values.get('enable')
    if enable == "":
        tag = ""
    else:
        tag = True
    if tenantids.strip() == "":
        tenantid = []
    else:
        td = re.split("[,|\s+]",tenantids)
        tenantid = [int(i) for i in td]
    dataMap = {
    "tenantids":list(totalids),
    "functions":{
    "msgrecall":{
    "enable":bool(tag),
    "tenantids":list(tenantid)
    }
    }
    }
    WriteYaml(dataMap)
    results = RunYaml()
    return jsonify(result = results)
@app.route('/robotOptimization',methods = ['POST'])
def robotOptimization():
    tenantids = request.values.get('tenantids')
    total = request.values.get('total')
    if total == "":
        totalids = []
    else:
        totalid =  re.split("[,|\s+]",total)
        totalids = [int(i) for i in totalid]
    enable = request.values.get('enable')
    if enable == "":
        tag = ""
    else:
        tag = True
    if tenantids.strip() == "":
        tenantid = []
    else:
        td = re.split("[,|\s+]",tenantids)
        tenantid = [int(i) for i in td]
    dataMap = {
    "tenantids":list(totalids),
    "functions":{
    "robotoptimization":{
    "enable":bool(tag),
    "tenantids":list(tenantid)
    }
    }
    }
    WriteYaml(dataMap)
    results = RunYaml()
    return jsonify(result = results)

@app.route('/recommand',methods = ['POST'])
def recommand():
    tenantids = request.values.get('tenantids')
    total = request.values.get('total')
    if total == "":
        totalids = []
    else:
        totalid =  re.split("[,|\s+]",total)
        totalids = [int(i) for i in totalid]
    enable = request.values.get('enable')
    if enable == "":
        tag = ""
    else:
        tag = True
    if tenantids.strip() == "":
        tenantid = []
    else:
        td = re.split("[,|\s+]",tenantids)
        tenantid = [int(i) for i in td]
    dataMap = {
    "tenantids":list(totalids),
    "functions":{
    "recommendation":{
    "enable":bool(tag),
    "tenantids":list(tenantid)
    }
    }
    }
    WriteYaml(dataMap)
    results = RunYaml()
    return jsonify(result = results)

@app.route('/sentiment',methods = ['POST'])
def sentiment():
    tenantids = request.values.get('tenantids')
    total = request.values.get('total')
    if total.strip() == "":
        totalids = []
    else:
        totalid =  re.split("[,|\s+]",total)
        totalids = [int(i) for i in totalid]
    enable = request.values.get('enable')
    if enable == "":
        tag = ""
    else:
        tag = True

    if tenantids.strip() == "":
        tenantid = []
    else:
        td = re.split("[,|\s+]",tenantids)
        tenantid = [int(i) for i in td]
    dataMap = {
    "tenantids":list(totalids),
    "functions":{
    "sentiment":{
    "enable":bool(tag),
    "tenantids":list(tenantid)
    }
    }
    }
    WriteYaml(dataMap)
    results = RunYaml()
    return jsonify(result = results)
@app.route('/growingio',methods = ['POST'])
def growingio():
    tenantids = request.values.get('tenantids')
    total = request.values.get('total')
    if total.strip() == "":
        totalids = []
    else:
        totalid =  re.split("[,|\s+]",total)
        totalids = [int(i) for i in totalid]
    enable = request.values.get('enable')
    if enable == "":
        tag = ""
    else:
        tag = True
    if tenantids.strip() == "":
        tenantid = []
    else:
        td = re.split("[,|\s+]",tenantids)
        tenantid = [int(i) for i in td]
    dataMap = {
    "tenantids":list(totalids),
    "functions":{
    "growingio":{
    "enable":bool(tag),
    "tenantids":list(tenantid)
    }
    }
    }
    WriteYaml(dataMap)
    results = RunYaml()
    return jsonify(result = results)
@app.route('/callback',methods = ['POST'])
def callback():
    tenantids = request.values.get('tenantids')
    total = request.values.get('total')
    if total.strip() == "":
        totalids = []
    else:
        totalid =  re.split("[,|\s+]",total)
        totalids = [int(i) for i in totalid]
    enable = request.values.get('enable')
    if enable == "":
        tag = ""
    else:
        tag = True
    if tenantids.strip() == "":
        tenantid = []
    else:
        td = re.split("[,|\s+]",tenantids)
        tenantid = [int(i) for i in td]
    dataMap = {
    "tenantids":list(totalids),
    "functions":{
    "callback":{
    "enable":bool(tag),
    "tenantids":list(tenantid)
    }
    }
    }
    WriteYaml(dataMap)
    results = RunYaml()
    return jsonify(result = results)

@app.route('/robot',methods = ['POST'])
def robot():
    tenantids = request.values.get('tenantids')
    total = request.values.get('total')
    if total.strip() == "":
        totalids = []
    else:
        totalid =  re.split("[,|\s+]",total)
        totalids = [int(i) for i in totalid]
    enable = request.values.get('enable')
    if enable == "":
        tag = ""
    else:
        tag = True
    if tenantids.strip() == "":
        tenantid = []
    else:
        td = re.split("[,|\s+]",tenantids)
        tenantid = [int(i) for i in td]
    dataMap = {
    "tenantids":list(totalids),
    "functions":{
    "robotmulti":{
    "enable":bool(tag),
    "tenantids":list(tenantid)
    }
    }
    }
    WriteYaml(dataMap)
    results = RunYaml()
    return jsonify(result = results)

@app.route('/voice',methods = ['POST'])
def voice():
    tenantids = request.values.get('tenantids')
    total = request.values.get('total')
    if total.strip() == "":
        totalids = []
    else:
        totalid =  re.split("[,|\s+]",total)
        totalids = [int(i) for i in totalid]
    enable = request.values.get('enable')
    if enable == "":
        tag = ""
    else:
        tag = True
    if tenantids.strip() == "":
        tenantid = []
    else:
        td = re.split("[,|\s+]",tenantids)
        tenantid = [int(i) for i in td]
    dataMap = {
    "tenantids":list(totalids),
    "functions":{
    "voice":{
    "enable":bool(tag),
    "tenantids":list(tenantid)
    }
    }
    }
    WriteYaml(dataMap)
    results = RunYaml()
    return jsonify(result = results)
@app.route('/msgpredict',methods = ['POST'])
def msgpredict():
    tenantids = request.values.get('tenantids')
    total = request.values.get('total')
    if total.strip() == "":
        totalids = []
    else:
        totalid =  re.split("[,|\s+]",total)
        totalids = [int(i) for i in totalid]
    enable = request.values.get('enable')
    if enable == "":
        tag = ""
    else:
        tag = True
    if tenantids.strip() == "":
        tenantid = []
    else:
        td = re.split("[,|\s+]",tenantids)
        tenantid = [int(i) for i in td]
    dataMap = {
    "tenantids":list(totalids),
    "functions":{
    "msgpredict":{
    "enable":bool(tag),
    "tenantids":list(tenantid)
    }
    }
    }
    WriteYaml(dataMap)
    results = RunYaml()
    return jsonify(result = results)
@app.route('/questiontransfer',methods = ['POST'])
def questiontransfer():
    tenantids = request.values.get('tenantids')
    total = request.values.get('total')
    if total.strip() == "":
        totalids = []
    else:
        totalid =  re.split("[,|\s+]",total)
        totalids = [int(i) for i in totalid]
    enable = request.values.get('enable')
    if enable == "":
        tag = ""
    else:
        tag = True
    if tenantids.strip() == "":
        tenantid = []
    else:
        td = re.split("[,|\s+]",tenantids)
        tenantid = [int(i) for i in td]
    dataMap = {
    "tenantids":list(totalids),
    "functions":{
    "questiontransfer":{
    "enable":bool(tag),
    "tenantids":list(tenantid)
    }
    }
    }
    WriteYaml(dataMap)
    results = RunYaml()
    return jsonify(result = results)

@app.route("/agentcall",methods = ['POST'])
def agentcall():
    tenantids = request.values.get('tenantids')
    url = request.values.get('url')
    total = request.values.get('total')

    if total.strip() == "":
        totalids = []
    else:
        totalid =  re.split("[,|\s+]",total)
        totalids = [int(i) for i in totalid]
    enable = request.values.get('enable')
    if enable == "":
        tag = ""
    else:
        tag = True
    if tenantids.strip() == "":
        tenantid = []
    else:
        td = re.split("[,|\s+]",tenantids)
        tenantid = [int(i) for i in td]

    dataMap = {
    "tenantids":list(totalids),
    "functions":{
    "agentcallvisitor":{
    "enable":bool(tag),
    "tenantids":list(tenantid),
    "url": str(url),
    }
    }
    }
    WriteYaml(dataMap)
    results = RunYaml()
    return jsonify(result = results)

@app.route("/opennotice",methods = ['POST'])
def opennotice():
    tenantids = request.values.get('tenantids')
    url = request.values.get('url')
    total = request.values.get('total')

    if total.strip() == "":
        totalids = []
    else:
        totalid =  re.split("[,|\s+]",total)
        totalids = [int(i) for i in totalid]
    enable = request.values.get('enable')
    if enable == "":
        tag = ""
    else:
        tag = True
    if tenantids.strip() == "":
        tenantid = []
    else:
        td = re.split("[,|\s+]",tenantids)
        tenantid = [int(i) for i in td]

    dataMap = {
    "tenantids":list(totalids),
    "functions":{
    "sessionopennotice":{
    "enable":bool(tag),
    "tenantids":list(tenantid),
    "url": str(url),
    }
    }
    }
    WriteYaml(dataMap)
    results = RunYaml()
    return jsonify(result = results)


@app.route("/kefuorg",methods = ['POST'])
def kefuorg():
    tenantids = request.values.get('tenantids')
    mydata = request.values.get('mydata')
    name = request.values.get('name')
    secondarydomain = request.values.get('secondarydomain')
    agentnumquota = request.values.get('agentnumquota')
    description = request.values.get('description')
    total = request.values.get('total')

    if total.strip() == "":
        totalids = []
    else:
        totalid =  re.split("[,|\s+]",total)
        totalids = [int(i) for i in totalid]
    enable = request.values.get('enable')
    if enable == "":
        tag = ""
    else:
        tag = True
    if tenantids.strip() == "":
        tenantid = []
    else:
        td = re.split("[,|\s+]",tenantids)
        tenantid = [int(i) for i in td]
    myobj = {}
    mydatas = []
    mytag = mydata.split(",")
    for i in mytag:
        myobj['username'] = str(i.split("<br>")[0])
        myobj['passwd'] = str(i.split("<br>")[1])
        myobj['phone'] = str(i.split("<br>")[2])
        myobj['nicename'] = str(i.split("<br>")[3])
        mydatas.append(dict(myobj))

    dataMap = {
    "tenantids":list(totalids),
    "functions":{
    "kefuorg":{
    "enable":bool(tag),
    "tenantids":list(tenantid),
    "name": str(name),
    "description":str(description),
    "secondarydomain":str(secondarydomain),
    "agentnumquota":int(agentnumquota),
    "users":list(mydatas)
    }
    }
    }
    WriteYaml(dataMap)
    results = RunYaml()
    return jsonify(result = results)

@app.route("/keywords",methods = ['POST'])
def keywords():
    total = request.values.get('total')
    tenantids = request.values.get('tenantids')
    enable = request.values.get('mydata')
    if total.strip() == "":
        totalids = []
    else:
        totalid =  re.split("[,|\s+]",total)
        totalids = [int(i) for i in totalid]
    enable = request.values.get('enable')
    if enable == "":
        tag = ""
    else:
        tag = True
    if tenantids.strip() == "":
        tenantid = []
    else:
        td = re.split("[,|\s+]",tenantids)
        tenantid = [int(i) for i in td]
    keywords = request.values.get('keywords')

    remindcontent = request.values.get('remindcontent')

    doublewordsflag = request.values.get('doublewordsflag')
    if doublewordsflag == "":
        doublewordsflagtag = ""
    else:
        doublewordsflagtag = True
    advancedfilterflag = request.values.get('advancedfilterflag')
    if advancedfilterflag == "":
        advancedfilterflagtag = ""
    else:
        advancedfilterflagtag = True
    wildcardreplaceflag = request.values.get('wildcardreplaceflag')
    if wildcardreplaceflag == "":
        wildcardreplaceflagtag = ""
    else:
        wildcardreplaceflagtag = True
    keywordscanflag = request.values.get('keywordscanflag')
    if keywordscanflag == "":
        keywordscanflagtag = ""
    else:
        keywordscanflagtag = True
    generalwordsflag = request.values.get('generalwordsflag')
    if generalwordsflag == "":
        generalwordsflagtag = ""
    else:
        generalwordsflagtag = True
    autoappendremindflag = request.values.get('autoappendremindflag')
    if autoappendremindflag == "":
        autoappendremindflagtag = ""
    else:
        autoappendremindflagtag = True

    dataMap = {
    "tenantids":list(totalids),
    "functions":{
    "keywordscan":{
    "enable":bool(tag),
    "tenantids":list(tenantid),
    "keywords": keywords.split(","),
    "remindcontent":remindcontent,
    "doublewordsflag":bool(doublewordsflagtag),
    "generalwordsflag":bool(generalwordsflagtag),
    "advancedfilterflag":bool(advancedfilterflagtag),
    "wildcardreplaceflag":bool(wildcardreplaceflagtag),
    "keywordscanflag":bool(keywordscanflagtag),
    "autoappendremindflag":bool(autoappendremindflagtag)
    }
    }
    }
    WriteYaml(dataMap)
    results = RunYaml()
    return jsonify(result = results)

@app.route("/all",methods = ['POST'])
def all():
    total = request.values.get('total')
    tenantids = request.values.get('tenantids')
    mydata = request.values.get('mydata')
    name = request.values.get('name')
    secondarydomain = request.values.get('secondarydomain')
    agentnumquota = request.values.get('agentnumquota')
    description = request.values.get('description')
    url = request.values.get('url')
    tag = True
    if total.strip() == "":
        totalids = []
    else:
        totalid =  re.split("[,|\s+]",total)
        totalids = [int(i) for i in totalid]

    if tenantids.strip() == "":
        tenantid = []
    else:
        td = re.split("[,|\s+]",tenantids)
        tenantid = [int(i) for i in td]
    keywords = request.values.get('keywords')
    keyw = [str(i) for i in keywords.split(",")]
    remindcontent = request.values.get('remindcontent')
    doublewordsflag = request.values.get('doublewordsflag')
    if doublewordsflag == "":
        doublewordsflagtag = ""
    else:
        doublewordsflagtag = True
    advancedfilterflag = request.values.get('advancedfilterflag')
    if advancedfilterflag == "":
        advancedfilterflagtag = ""
    else:
        advancedfilterflagtag = True
    wildcardreplaceflag = request.values.get('wildcardreplaceflag')
    if wildcardreplaceflag == "":
        wildcardreplaceflagtag = ""
    else:
        wildcardreplaceflagtag = True
    keywordscanflag = request.values.get('keywordscanflag')
    if keywordscanflag == "":
        keywordscanflagtag = ""
    else:
        keywordscanflagtag = True
    generalwordsflag = request.values.get('generalwordsflag')
    if generalwordsflag == "":
        generalwordsflagtag = ""
    else:
        generalwordsflagtag = True
    autoappendremindflag = request.values.get('autoappendremindflag')
    if autoappendremindflag == "":
        autoappendremindflagtag = ""
    else:
        autoappendremindflagtag = True
    myobj = {}
    mydatas = []
    mytag = mydata.split(",")
    for i in mytag:
        myobj['username'] = str(i.split("<br>")[0])
        myobj['passwd'] = str(i.split("<br>")[1])
        myobj['phone'] = str(i.split("<br>")[2])
        myobj['nicename'] = str(i.split("<br>")[3])
        mydatas.append(dict(myobj))

    dataMap = {
    "tenantids":list(totalids),
    "functions":{
    "sentiment":{
    "enable":bool(tag),
    "tenantids":list(tenantid)
    },
    "recommendation":{
    "enable":bool(tag),
    "tenantids":list(tenantid)
    },
    "growingio":{
    "enable":bool(tag),
    "tenantids":list(tenantid)
    },
    "callback":{
    "enable":bool(tag),
    "tenantids":list(tenantid)
    },
    "robotmulti":{
    "enable":bool(tag),
    "tenantids":list(tenantid)
    },
    "voice":{
    "enable":bool(tag),
    "tenantids":list(tenantid)
    },
    "questiontransfer":{
    "enable":bool(tag),
    "tenantids":list(tenantid)
    },
    "kefuorg":{
    "enable":bool(tag),
    "tenantids":list(tenantid),
    "name": str(name),
    "description":str(description),
    "secondarydomain":str(secondarydomain),
    "agentnumquota":int(agentnumquota),
    "users":list(mydatas)
    },
    "keywordscan":{
    "enable":bool(tag),
    "tenantids":list(tenantid),
    "keywords": list(keyw),
    "remindcontent":str(remindcontent),
    "doublewordsflag":bool(doublewordsflagtag),
    "generalwordsflag":bool(generalwordsflagtag),
    "advancedfilterflag":bool(advancedfilterflagtag),
    "wildcardreplaceflag":bool(wildcardreplaceflagtag),
    "keywordscanflag":bool(keywordscanflagtag),
    "autoappendremindflag":bool(autoappendremindflagtag)
    },
    "agentcallvisitor":{
    "enable":bool(tag),
    "tenantids":list(tenantid),
    "url": str(url),
    },
    "sessionopennotice":{
    "enable":bool(tag),
    "tenantids":list(tenantid),
    "url": str(url),
    },
    "msgrecall":{
    "enable":bool(tag),
    "tenantids":list(tenantid),
    "url": str(url),
    },
    "audiovideo":{
    "enable":bool(tag),
    "tenantids":list(tenantid),
    "url": str(url),
    },
    "waitlistnumber":{
    "enable":bool(tag),
    "tenantids":list(tenantid),
    "url": str(url),
    },
    "msgpredict":{
    "enable":bool(tag),
    "tenantids":list(tenantid)
    }
    }
    }
    WriteYaml(dataMap)
    results = RunYaml()
    return jsonify(result = results)
