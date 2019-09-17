<html>
<head>
<title>Challenge 37</title>
</head>
<body>
<!-- index.phps -->
<?

$pw="???";

$time=time();   //시간이 자동으로 설정됨


$f=fopen("tmp/tmp-$time","w");    // tmp디렉토리내 tmp-time()으로 설정된 시간 이라는으로 파일을 생성함.
fwrite($f,"127.0.0.1");           // 해당 파일내 127.0.0.1을 쓰기
fclose($f);						  // 해당 파일 닫음


$fck=@file("tmp/.number"); 		// tmp/.number 파일의 내용을 리스트로 읽음 fck에 초기화

if($fck) $fck=$fck[0];			//.number 파일에 내용이 있다면 인덱스0의 내용을 fck에 초기화
if(!$fck) $fck=0;				//.number 파일에 내용이 없다면 fck는 0으로 초기화

$fck++;							//1번째 인덱스를 가리킴

$f2=fopen("tmp/.number","w");	// tmp/.number 파일에 fck의 내용을 즉, 이전 number의 1인덱스에 있는 내용을 다시 씀
fwrite($f2,$fck);
fclose($f2);

$file_nm=$HTTP_POST_FILES[upfile][name];	// 업로드하는 파일 필터
$file_nm=str_replace("<","",$file_nm);
$file_nm=str_replace(">","",$file_nm);
$file_nm=str_replace(".","",$file_nm);
$file_nm=str_replace(" ","",$file_nm);

if($file_nm)
{
$f=@fopen("tmp/$file_nm","w");				//핉터에 걸리지 않은 파일에 리모트 서버 (요청을 하는 측의 서버) 쓰기
@fwrite($f,$_SERVER[REMOTE_ADDR]);  
@fclose($f);
}
///////////////////////////////////////////   !!!! 업로드하는 파일에 접속하는



echo("<pre>");

$kk=scandir("tmp");

for($i=0;$i<=count($kk);$i++)
{
echo("$kk[$i]\n");
}

echo("</pre>");





$ck=file("tmp/tmp-$time");			//tmp-$time에 적히는 ip주소의 7777포트로 get 요청을 보내며 패스워드를 보낸다.
$ck=$ck[0];

$request="GET /$pw HTTP/1.0\r\n";
$request.="Host: $ck\r\n";
$request.="\r\n";

$socket=@fsockopen($ck,7777,$errstr,$errno,1);

@fputs($socket,$request);

@fclose($socket);

echo("$ck:7777<br>");

if($fck>=30)
{
$kk=scandir("tmp");

for($i=0;$i<=count($kk);$i++)
{
@unlink("tmp/$kk[$i]");
}

}

?>

<form method=post enctype="multipart/form-data" action=index.php>
<input type=file name=upfile><input type=submit>
</form>




</body>
</html>