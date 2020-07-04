goto :MAIN

rem pathの通ったフォルダにこいつを置いておき
rem powershellのショートカットを以下の設定で用意
rem プロパティ＞詳細設定＞管理者として実行　にチェック
rem プロパティ＞リンク先　の後ろに半角スペース区切りを入れてこいつのファイル名を追記
rem 作ったショートカットに任意のフォルダをドラッグドロップすると、
rem 管理者権限のpowershellがそのディレクトリで開く



:MAIN
setlocal

if "%~2"=="" (
  set TargetPath=%1
  goto :CHANGEDIR
)

set TargetPath=
for %%a in (%*) do (
  call :SOLVEPATH %%a
)


:CHANGEDIR
cd /d "%TargetPath%"
cmd /k powershell -Command "clear"
endlocal

goto :END


:SOLVEPATH
set tmpPathA=%TargetPath%
set tmpPathB=%1
set TargetPath=%tmpPathA% %tmpPathB%

goto :END



:END