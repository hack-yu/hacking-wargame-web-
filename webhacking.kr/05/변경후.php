 <html>
<title>Challenge 5</title>
</head>

<body bgcolor=black>
    <center>
        <script>

            if (eval(document.cookie).indexOf(oldzombie) == -1) {
                bye;
            }
            if (eval(document.URL).indexOf(mode+'='+1) == -1) {
                alert('access_denied');
                history.go(-1);
            } else {
                document.write('<font size=2 color=white>Join</font><p>');
                document.write('.<p>.<p>.<p>.<p>.<p>');
                document.write('<form method=post action='+join.php+'>');
                document.write('<table border=1><tr><td><font color=gray>id</font></td><td><input type=text name='+id+' maxlength=5></td></tr>');
                document.write('<tr><td><font color=gray>pass</font></td><td><input type=text name='+pw+' maxlength=10></td></tr>');
                document.write('<tr align=center><td colspan=2><input type=submit></td></tr></form></table>');
            }
        </script>
</body>

</html>





