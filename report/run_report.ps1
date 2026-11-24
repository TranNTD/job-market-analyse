# Paths on THIS computer — adjust if the tools are somewhere else
$BirtLib = "C:\Users\trann\dev\tools\birt-runtime\ReportEngine\lib\*"
$Jdbc    = "C:\Users\trann\dev\tools\jdbc\postgresql-42.7.14.jar"

java -cp "$BirtLib;$Jdbc" report\src\ReportRunner.java