basedir = %A_ScriptDir%\screen_config.ini
IniRead, prog1, %basedir%, SplitScreen, screen1
IniRead, prog2, %basedir%, SplitScreen, screen2
IniRead, prog3, %basedir%, SplitScreen, screen3
IniRead, prog4, %basedir%, SplitScreen, screen4
IniRead, prog5, %basedir%, SplitScreen, screen5

Process, Exist , prog1
{
	;WinWait, %prog1%
	WinMove %prog1%,, 0, 0, (A_ScreenWidth/2), (A_ScreenHeight/3)
;    return
}
Process, Exist , %prog2%
{
	;WinWait, %prog2%
	WinMove %prog2%,, 0, (A_ScreenHeight/3), (A_ScreenWidth/2), (A_ScreenHeight/3)
;    return
}
Process, Exist , %prog3%
{
	;WinWait, %prog3%
	WinMove %prog3%,, 0, (A_ScreenHeight/3)*2, (A_ScreenWidth/2), (A_ScreenHeight/3)
;   return
}
Process, Exist , %prog4%
{
	;WinWait, %prog4%
	WinMove %prog4%,, (A_ScreenWidth/2), 0, (A_ScreenWidth), (A_ScreenHeight/2)
;    return
}
Process, Exist , %prog5%
{
;	WinWait, %prog5%
	WinMove %prog5%,, (A_ScreenWidth/2), (A_ScreenHeight/2), (A_ScreenWidth), (A_ScreenHeight)
;    return
}





