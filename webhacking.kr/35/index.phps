<html>
<head>
<title>Challenge 35</title>
<head>
<body>
<form method=get action=index.php>
phone : <input name=phone size=11><input type=submit value='add'>
</form>
<?
if($_GET[phone])
{
if(eregi("%|\*|/|=|from|select|x|-|#|\(\(",$_GET[phone])) exit("no hack");

@mysql_query("insert into challenge35_list(id,ip,phone) values('$_SESSION[id]','$_SERVER[REMOTE_ADDR]',$_GET[phone])") or die("query error");
echo("Done<br>");
}

$admin_ck=mysql_fetch_array(mysql_query("select ip from challenge35_list where id='admin' and ip='$_SERVER[REMOTE_ADDR]'"));

if($admin_ck[ip]==$_SERVER[REMOTE_ADDR])   // 배열이름[키워드] -> 해당 쿼리의 결과에서 특정 키워드에 속하는 값을 비교할 수 있다고??
{
@solve();
@mysql_query("delete from challenge35_list");
}
$phone_list=@mysql_query("select * from challenge35_list where ip='$_SERVER[REMOTE_ADDR]'");

echo("<!--");

while($d=@mysql_fetch_array($phone_list))
{
echo("$d[id] - $d[phone]\n");
}

echo("-->");

?>
<br><a href=index.phps>index.phps</a>
<br><br><br>
<center>Thanks to <a href=http://webhacking.kr/index.php?mode=information&id=HellSonic>HellSonic</a></center>
<br><br><br>
</body>
</html>