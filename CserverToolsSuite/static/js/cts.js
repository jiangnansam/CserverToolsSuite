$(document).ready(function(){
	$("#cancel_save_env").click(function ()
			{
				history.go(-1);
			});
});

function onSelect(version){
	var loading = document.getElementById('loading');
	var svn_path = document.getElementById('svn_path');
	var obj = document.getElementById(version);
	var reqUrl = window.location.protocol + "//" + window.location.host + "/dbtracking/query";
	var loading_div;
	loading.style.display="block";
	svn_path.style.display="none";
	$.ajax({
		type:"post",
		url:reqUrl,
		data:obj.value,
		success:function(response){   
			console.log(response);
			loading.style.display="none";
			svn_path.style.display="inline";
			$("#svn_path").html(response);
        },
	});
}

