function AddUser(ev){
str='<div class="form-group"><div class="col-md-12" ><form class="form-inline" role="form"><div class="form-group"><input type="text" class="form-control username input-circle"  placeholder="Username"></div><div class="form-group" style="margin-left:30px"><input type="text" class="form-control passwd input-circle"  placeholder="Passwd"></div><div class="form-group" style="margin-left:30px"><input type="text" class="form-control phone input-circle"  placeholder="Phone"></div><div class="form-group" style="margin-left:30px"><input type="text" class="form-control nickname input-circle"  placeholder="Nickname"></div></form></div></div>'
$(ev).parent().parent().after(str);

}

function AddAllUser(ev){
str='<div class="form-group"><div class="col-md-12" ><form class="form-inline all-inline" role="form"><div class="form-group"><input type="text" class="form-control usernames input-circle"  placeholder="Username"></div><div class="form-group" style="margin-left:30px"><input type="text" class="form-control passwds input-circle"  placeholder="Passwd"></div><div class="form-group" style="margin-left:30px"><input type="text" class="form-control phones input-circle"  placeholder="Phone"></div><div class="form-group" style="margin-left:30px"><input type="text" class="form-control nicknames input-circle"  placeholder="Nickname"></div></form></div></div>'
$(ev).parent().parent().after(str);

}


function DelUser(ev){
    $(ev).parent().parent().next().remove();
}

function change(da){
    if (da=="recommand"){
        title="智能人机协作";
          $("#portlet").find(".modal-footer").html('<button type="button" class="btn blue" onclick="recommandtion()">Run</button><button type="button" class="btn default" data-dismiss="modal" >Close</button>');
   }else if(da=="opennotice"){
        title="获知访客APP版本信息";
          $("#portlet").find(".modal-footer").html('<button type="button" class="btn blue" onclick="opennotices()">Run</button>  <button type="button" class="btn default" data-dismiss="modal" >Close</button>');
    }else if(da=="sentiment"){
        title="智能质检";
          $("#portlet").find(".modal-footer").html('<button type="button" class="btn blue" onclick="sentiments()">Run</button>  <button type="button" class="btn default" data-dismiss="modal" >Close</button>');
    }else if(da=="growingio"){
           title="访客轨迹分析 && 网站访客统计";
         $("#portlet").find(".modal-footer").html('<button type="button" class="btn blue" onclick="growingios()">Run</button>  <button type="button" class="btn default" data-dismiss="modal" >Close</button>');
    }else if(da=="callback"){
        title="自定义事件推送";
          $("#portlet").find(".modal-footer").html('<button type="button" class="btn blue" onclick="callbacks()">Run</button>  <button type="button" class="btn default" data-dismiss="modal" >Close</button>');
    }else if(da=="robot"){
        title="开通多机器人";
          $("#portlet").find(".modal-footer").html('<button type="button" class="btn blue" onclick="robots()">Run</button>  <button type="button" class="btn default" data-dismiss="modal" >Close</button>');
    }else if(da=="voice"){
        title="客户之声";
         $("#portlet").find(".modal-footer").html('<button type="button" class="btn blue" onclick="voices()">Run</button>  <button type="button" class="btn default" data-dismiss="modal" >Close</button>');
    }else if(da=="questiontransfer"){
        title="开通机器人推荐问题的转人工按钮";
          $("#portlet").find(".modal-footer").html('<button type="button" class="btn blue" onclick="questiontransfers()">Run</button>  <button type="button" class="btn default" data-dismiss="modal" >Close</button>');

    }else if(da=="msgpredict"){
        title="开通消息预知功能";
          $("#portlet").find(".modal-footer").html('<button type="button" class="btn blue" onclick="msgpredicts()">Run</button>  <button type="button" class="btn default" data-dismiss="modal" >Close</button>');
    }else if(da=="msgrecall"){
        title="消息撤回";
          $("#portlet").find(".modal-footer").html('<button type="button" class="btn blue" onclick="msgrecalls()">Run</button>  <button type="button" class="btn default" data-dismiss="modal" >Close</button>');
    }else if(da=="waitlist"){
        title="排队人数展示";
          $("#portlet").find(".modal-footer").html('<button type="button" class="btn blue" onclick="waitlists()">Run</button>  <button type="button" class="btn default" data-dismiss="modal" >Close</button>');
    }else if(da=="audiovideo"){
        title="音响视频";
     $("#portlet").find(".modal-footer").html('<button type="button" class="btn blue" onclick="audio()">Run</button>  <button type="button" class="btn default" data-dismiss="modal" >Close</button>');
    }else if(da=="robotOptimization"){
        title="机器人知识问答库优化";
          $("#portlet").find(".modal-footer").html('<button type="button" class="btn blue" onclick="robotOptimization()">Run</button>  <button type="button" class="btn default" data-dismiss="modal" >Close</button>');
      }
    $("#portlet").find('h4').text(title);
}

function robotOptimization(){
tenantid = $("#recom").val();
total = $("#td").val();
if (tenantid=="" && total==""){
    alert("tenantid不能为空");
    return false;
}

 if($("#radio53").attr("checked")=="checked"){

action="true";
}else{
action="";
}
    $(".recommand").html("<img src='/static/images/ajax_loader3.gif'>");
    $.post($SCRIPT_ROOT + '/robotOptimization', {
            total: $("#td").val(),
            tenantids: tenantid,
            enable: action,
            now: new Date().getTime()
        },
        function(data) {
            $(".recommand").html('<div class="well well-lg" id="recommand_result" style="display: none;"></div>')
            $("#recommand_result").show(500);
            $("#recommand_result").html('<p style="line-height:30px">'+data.result+'</p>');
        });

}

function msgrecalls(){
tenantid = $("#recom").val();
total = $("#td").val();
if (tenantid=="" && total==""){
    alert("tenantid不能为空");
    return false;
}

 if($("#radio53").attr("checked")=="checked"){

action="true";
}else{
action="";
}
    $(".recommand").html("<img src='/static/images/ajax_loader3.gif'>");
    $.post($SCRIPT_ROOT + '/msgrecall', {
            total: $("#td").val(),
            tenantids: tenantid,
            enable: action,
            now: new Date().getTime()
        },
        function(data) {
            $(".recommand").html('<div class="well well-lg" id="recommand_result" style="display: none;"></div>')
            $("#recommand_result").show(500);
            $("#recommand_result").html('<p style="line-height:30px">'+data.result+'</p>');
        });

}

function waitlists(){
tenantid = $("#recom").val();
total = $("#td").val();
if (tenantid=="" && total==""){
    alert("tenantid不能为空");
    return false;
}

 if($("#radio53").attr("checked")=="checked"){

action="true";
}else{
action="";
}
    $(".recommand").html("<img src='/static/images/ajax_loader3.gif'>");
    $.post($SCRIPT_ROOT + '/waitlist', {
            total: $("#td").val(),
            tenantids: tenantid,
            enable: action,
            now: new Date().getTime()
        },
        function(data) {
            $(".recommand").html('<div class="well well-lg" id="recommand_result" style="display: none;"></div>')
            $("#recommand_result").show(500);
            $("#recommand_result").html('<p style="line-height:30px">'+data.result+'</p>');
        });

}

function audio(){
tenantid = $("#recom").val();
total = $("#td").val();
if (tenantid=="" && total==""){
    alert("tenantid不能为空");
    return false;
}

 if($("#radio53").attr("checked")=="checked"){

action="true";
}else{
action="";
}
    $(".recommand").html("<img src='/static/images/ajax_loader3.gif'>");
    $.post($SCRIPT_ROOT + '/audiovideo', {
            total: $("#td").val(),
            tenantids: tenantid,
            enable: action,
            now: new Date().getTime()
        },
        function(data) {
            $(".recommand").html('<div class="well well-lg" id="recommand_result" style="display: none;"></div>')
            $("#recommand_result").show(500);
            $("#recommand_result").html('<p style="line-height:30px">'+data.result+'</p>');
        });

}

function recommandtion(){
tenantid = $("#recom").val();
total = $("#td").val();
if (tenantid=="" && total==""){
    alert("tenantid不能为空");
    return false;
}

 if($("#radio53").attr("checked")=="checked"){

action="true";
}else{
action="";
}
    $(".recommand").html("<img src='/static/images/ajax_loader3.gif'>");
    $.post($SCRIPT_ROOT + '/recommand', {
            total: $("#td").val(),
            tenantids: tenantid,
            enable: action,
            now: new Date().getTime()
        },
        function(data) {
            $(".recommand").html('<div class="well well-lg" id="recommand_result" style="display: none;"></div>')
            $("#recommand_result").show(500);
            $("#recommand_result").html('<p style="line-height:30px">'+data.result+'</p>');
        });

}


function sentiments(){
tenantid = $("#recom").val();
total = $("#td").val();
if (tenantid=="" && total==""){
    alert("tenantid不能为空");
    return false;
}
 if($("#radio53").attr("checked")=="checked"){
action='true';
}else{
action="";
}
    $(".recommand").html("<img src='/static/images/ajax_loader3.gif'>");
    $.post($SCRIPT_ROOT + '/sentiment', {
            total: $("#td").val(),
            tenantids: tenantid,
            enable: action,
            now: new Date().getTime()
        },
        function(data) {
            $(".recommand").html('<div class="well well-lg" id="recommand_result" style="display: none;"></div>')
            $("#recommand_result").show(500);
            $("#recommand_result").html('<p style="line-height:30px">'+data.result+'</p>');
        });

}

function opennotices(){
tenantid = $("#recom").val();
total = $("#td").val();
if (tenantid=="" && total==""){
    alert("tenantid不能为空");
    return false;
}
 if($("#radio53").attr("checked")=="checked"){
action='true';
}else{
action="";
}
    $(".recommand").html("<img src='/static/images/ajax_loader3.gif'>");
    $.post($SCRIPT_ROOT + '/opennotice', {
            total: $("#td").val(),
            tenantids: tenantid,
            enable: action,
            now: new Date().getTime()
        },
        function(data) {
            $(".recommand").html('<div class="well well-lg" id="recommand_result" style="display: none;"></div>')
            $("#recommand_result").show(500);
            $("#recommand_result").html('<p style="line-height:30px">'+data.result+'</p>');
        });

}


function growingios(){
tenantid = $("#recom").val();
total = $("#td").val();
if (tenantid=="" && total==""){
    alert("tenantid不能为空");
    return false;
}
 if($("#radio53").attr("checked")=="checked"){
action='true';
}else{
action="";
}
    $(".recommand").html("<img src='/static/images/ajax_loader3.gif'>");
    $.post($SCRIPT_ROOT + '/growingio', {
            total: $("#td").val(),
            tenantids: tenantid,
            enable: action,
            now: new Date().getTime()
        },
        function(data) {
            $(".recommand").html('<div class="well well-lg" id="recommand_result" style="display: none;"></div>')
            $("#recommand_result").show(500);
            $("#recommand_result").html('<p style="line-height:30px">'+data.result+'</p>');
        });
}
function callbacks(){
tenantid = $("#recom").val();
total = $("#td").val();
if (tenantid=="" && total==""){
    alert("tenantid不能为空");
    return false;
}
 if($("#radio53").attr("checked")=="checked"){
action='true';
}else{
action="";
}
    $(".recommand").html("<img src='/static/images/ajax_loader3.gif'>");
    $.post($SCRIPT_ROOT + '/callback', {
            total: $("#td").val(),
            tenantids: tenantid,
            enable: action,
            now: new Date().getTime()
        },
        function(data) {
            $(".recommand").html('<div class="well well-lg" id="recommand_result" style="display: none;"></div>')
            $("#recommand_result").show(500);
            $("#recommand_result").html('<p style="line-height:30px">'+data.result+'</p>');
        });
}

function robots(){
tenantid = $("#recom").val();
total = $("#td").val();
if (tenantid=="" && total==""){
    alert("tenantid不能为空");
    return false;
}
 if($("#radio53").attr("checked")=="checked"){
action='true';
}else{
action="";
}
    $(".recommand").html("<img src='/static/images/ajax_loader3.gif'>");
    $.post($SCRIPT_ROOT + '/robot', {
            total: $("#td").val(),
            tenantids: tenantid,
            enable: action,
            now: new Date().getTime()
        },
        function(data) {
            $(".recommand").html('<div class="well well-lg" id="recommand_result" style="display: none;"></div>')
            $("#recommand_result").show(500);
            $("#recommand_result").html('<p style="line-height:30px">'+data.result+'</p>');
        });
}

function voices(){
        tenantid = $("#recom").val();
total = $("#td").val();
if (tenantid=="" && total==""){
    alert("tenantid不能为空");
    return false;
}
 if($("#radio53").attr("checked")=="checked"){
action='true';
}else{
action="";
}
    $(".recommand").html("<img src='/static/images/ajax_loader3.gif'>");
    $.post($SCRIPT_ROOT + '/voice', {
            total: $("#td").val(),
            tenantids: tenantid,
            enable: action,
            now: new Date().getTime()
        },
        function(data) {
            $(".recommand").html('<div class="well well-lg" id="recommand_result" style="display: none;"></div>')
            $("#recommand_result").show(500);
            $("#recommand_result").html('<p style="line-height:30px">'+data.result+'</p>');
        });
}

function msgpredicts(){
    tenantid = $("#recom").val();
total = $("#td").val();
if (tenantid=="" && total==""){
    alert("tenantid不能为空");
    return false;
}
 if($("#radio53").attr("checked")=="checked"){
action='true';
}else{
action="";
}
    $(".recommand").html("<img src='/static/images/ajax_loader3.gif'>");
    $.post($SCRIPT_ROOT + '/msgpredict', {
            total: $("#td").val(),
            tenantids: tenantid,
            enable: action,
            now: new Date().getTime()
        },
        function(data) {
            $(".recommand").html('<div class="well well-lg" id="recommand_result" style="display: none;"></div>')
            $("#recommand_result").show(500);
            $("#recommand_result").html('<p style="line-height:30px">'+data.result+'</p>');
        });
}


function questiontransfers(){
tenantid = $("#recom").val();
total = $("#td").val();
if (tenantid=="" && total==""){
    alert("tenantid不能为空");
    return false;
}
if($("#radio53").attr("checked")=="checked"){
action='true';
}else{
action="";
}
    $(".recommand").html("<img src='/static/images/ajax_loader3.gif'>");
    $.post($SCRIPT_ROOT + '/questiontransfer', {
            total: $("#td").val(),
            tenantids: tenantid,
            enable: action,
            now: new Date().getTime()
        },
        function(data) {
            $(".recommand").html('<div class="well well-lg" id="recommand_result" style="display: none;"></div>')
            $("#recommand_result").show(500);
            $("#recommand_result").html('<p style="line-height:30px">'+data.result+'</p>');
        });
}


function agentcall(){
tenantid = $("#agentcallvisitorid").val();
total = $("#td").val();
url = $("#agenturl").val();
if (tenantid=="" && total==""){
    alert("tenantid不能为空");
    return false;
}
if (url==""){
    alert("URL不能为空");
    return false;
}

   $(".callvisitors").html("<img src='/static/images/ajax_loader3.gif'>");
    $.post($SCRIPT_ROOT + '/agentcall', {
            total: $("#td").val(),
            tenantids: tenantid,
            url: url,
            now: new Date().getTime()
        },
        function(data) {
            $(".callvisitors").html('<div class="well well-lg" id="agentcall_result" style="display: none;"></div>')
            $("#agentcall_result").show(500);
            $("#agentcall_result").html('<p style="line-height:30px">'+data.result+'</p>');
        });


}


function kefuorgs(){
tenantid = $("#kefuorgtid").val();
total = $("#td").val();
name = $("#name").val();
sd = $("#sd").val();
ag = $("#ag").val();
descriptions=$("#descriptions").val();



if (tenantid=="" && total==""){
    alert("tenantid不能为空");
    return false;
}

if (name==""){
    alert("Name不能为空");
    return false;
}


if (ag==""){
    alert("Agentnumquota不能为空");
    return false;
}

if(isNaN(ag)){
    alert("请录入数字");
    return false;
}


if (descriptions==""){
    alert("Description不能为空");
    return false;
}


 if($("#radio1").attr("checked")=="checked"){
action='true';
}else{
action="";
}



  s="";
  if ($(".form-inline").length<1){
     alert("username,password,phone不能为空");
     return false;
  }


    var reg = /^\w+((-\w+)|(\.\w+))*\@[A-Za-z0-9]+((\.|-)[A-Za-z0-9]+)*\.[A-Za-z0-9]+$/;

      if($(".form-inline").find('.username').val()==""){
        alert("username不能为空");
        return false;
    }

     if(!reg.test($(".form-inline").find('.username').val())) {
        alert("username必须是邮箱格式");
        return false;
    }


      if($(".form-inline").find('.passwd').val()==""){
        alert("密码不能为空");
        return false;
    }

      if($(".form-inline").find('.phone').val()==""){
        alert("电话不能为空");
        return false;
    }


  $(".form-inline").each(function(index,element){

    str=""
    str=$(element).find('.username').val()+"<br>"+$(element).find('.passwd').val()+"<br>"+$(element).find('.phone').val()+"<br>"+$(element).find('.nickname').val()+",";
    s+=str;


  });

  s=s.substring(0,s.length-1);

   $(".kefuorg").html("<img src='/static/images/ajax_loader3.gif'>");
    $.post($SCRIPT_ROOT + '/kefuorg', {
            total: $("#td").val(),
            tenantids: tenantid,
            name: name,
            secondarydomain: sd,
            agentnumquota: ag,
            description: descriptions,
            enable: action,
            mydata:s,
            now: new Date().getTime()
        },
        function(data) {
            $(".kefuorg").html('<div class="well well-lg" id="kefuorg_result" style="display: none;"></div>')
            $("#kefuorg_result").show(500);
            $("#kefuorg_result").html('<p style="line-height:30px">'+data.result+'</p>');
        });

}


function keywords(){
tenantid = $("#keyid").val();
total = $("#td").val();
kw = $("#kw").val();
rc = $("#rc").val();


if (tenantid=="" && total==""){
    alert("tenantid不能为空");
    return false;
}

//if (kw==""){
//    alert("Keywords不能为空");
//   return false;
//}

//if (rc==""){
//    alert("Remindcontent不能为空");
//    return false;
//}

if($("#radio3").attr("checked")=="checked"){
action='true';
}else{
action="";
}

if($("#double1").attr("checked")=="checked"){
double='true';
}else{
double="";
}

if($("#genera1").attr("checked")=="checked"){
genera='true';
}else{
genera="";
}

if($("#advanced1").attr("checked")=="checked"){
advanced='true';
}else{
advanced="";
}

if($("#wildcard1").attr("checked")=="checked"){
wildcard='true';
}else{
wildcard="";
}

if($("#auto1").attr("checked")=="checked"){
auto='true';
}else{
auto="";
}
if($("#keyword1").attr("checked")=="checked"){
keyword='true';
}else{
keyword="";
}

 $(".key").html("<img src='/static/images/ajax_loader3.gif'>");
    $.post($SCRIPT_ROOT + '/keywords', {
            total: $("#td").val(),
            tenantids: tenantid,
            keywords: kw,
            remindcontent: rc,
            generalwordsflag:genera,
            doublewordsflag: double,
            advancedfilterflag: advanced,
            wildcardreplaceflag: wildcard,
            enable: action,
            keywordscanflag:keyword,
            autoappendremindflag:auto,
            now: new Date().getTime()
        },
        function(data) {
            $(".key").html('<div class="well well-lg" id="key_result" style="display: none;"></div>')
            $("#key_result").show(500);
            $("#key_result").html('<p style="line-height:30px">'+data.result+'</p>');
        });

}



function alls(){
tenantid = $("#allid").val();
total = $("#td").val();
name = $(".name").val();
sd = $(".sd").val();
ag = $(".ag").val();
url=$("#allurl").val();

descriptions=$(".descriptions").val();
kw = $(".kw").val();
rc = $(".rc").val();

if (tenantid=="" && total==""){
    alert("tenantid不能为空");
    return false;
}
if (url==""){
       alert("IP不能为空");
    return false;
}
if (kw==""){
    alert("Keywords不能为空");
    return false;
}

if (rc==""){
    alert("Remindcontent不能为空");
    return false;
}

if(ag==""){
    alert("Agentnumquota不能为空");
    return false;
}

if(isNaN(ag)){
    alert("Agentnumquota请录入数字");
    return false;
}

if($("#double3").attr("checked")=="checked"){
double='true';
}else{
double="";
}

if($("#genera3").attr("checked")=="checked"){
genera='true';
}else{
genera="";
}

if($("#advanced3").attr("checked")=="checked"){
advanced='true';
}else{
advanced="";
}

if($("#wildcard3").attr("checked")=="checked"){
wildcard='true';
}else{
wildcard="";
}

if($("#auto3").attr("checked")=="checked"){
auto='true';
}else{
auto="";
}
if($("#keyword3").attr("checked")=="checked"){
keyword='true';
}else{
keyword="";
}


  s="";
if ($(".all-inline").length<1){
alert("username,password,phone不能为空");
return false;
}

    var reg = /^\w+((-\w+)|(\.\w+))*\@[A-Za-z0-9]+((\.|-)[A-Za-z0-9]+)*\.[A-Za-z0-9]+$/;

      if($(".all-inline").find('.usernames').val()==""){
        alert("username不能为空");
        return false;
    }

     if(!reg.test($(".all-inline").find('.usernames').val())) {
        alert("username必须是邮箱格式");
        return false;
    }


      if($(".all-inline").find('.passwds').val()==""){
        alert("密码不能为空");
        return false;
    }

      if($(".all-inline").find('.phones').val()==""){
        alert("电话不能为空");
        return false;
    }


  $(".all-inline").each(function(index,element){

    str=""
    str=$(element).find('.usernames').val()+"<br>"+$(element).find('.passwds').val()+"<br>"+$(element).find('.phones').val()+"<br>"+$(element).find('.nicknames').val()+",";
    s+=str;

  });
  s=s.substring(0,s.length-1);

$(".alls").html("<img src='/static/images/ajax_loader3.gif'>");
    $.post($SCRIPT_ROOT + '/all', {
            total: $("#td").val(),
            tenantids: tenantid,
            keywords: kw,
            remindcontent: rc,
            generalwordsflag:genera,
            doublewordsflag: double,
            advancedfilterflag: advanced,
            wildcardreplaceflag: wildcard,
            keywordscanflag:keyword,
            autoappendremindflag:auto,
            name: name,
            url:url,
            secondarydomain: sd,
            agentnumquota: ag,
            description: descriptions,
            mydata:s,
            now: new Date().getTime()
        },
        function(data) {
            $(".alls").html('<div class="well well-lg" id="all_result" style="display: none;"></div>')
            $("#all_result").show(500);
            $("#all_result").html('<p style="line-height:30px">'+data.result+'</p>');
        });
}
