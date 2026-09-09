!define APPNAME "nonunicodeconverter app"
!define APPEXE "chrome.exe"
!define APPURL "https://unicode2nonunicode.com"

Name "${APPNAME}"
OutFile "nonunicodeconverter-xp.exe"
InstallDir "$PROGRAMFILES\nonunicodeconverter"
RequestExecutionLevel admin

Page directory
Page instfiles

Section "Install"
  SetOutPath "$INSTDIR"
  
  ; This assumes supermium-portable contents will be placed in the legacy-app directory
  ; before the NSIS script is compiled.
  File /r "supermium-portable\*"
  
  ; Create Desktop Shortcut
  CreateShortCut "$DESKTOP\${APPNAME}.lnk" "$INSTDIR\${APPEXE}" "--app=${APPURL}" "$INSTDIR\${APPEXE}" 0
  
  ; Create Start Menu Shortcut
  CreateDirectory "$SMPROGRAMS\${APPNAME}"
  CreateShortCut "$SMPROGRAMS\${APPNAME}\${APPNAME}.lnk" "$INSTDIR\${APPEXE}" "--app=${APPURL}" "$INSTDIR\${APPEXE}" 0
  
  ; Create Uninstaller
  WriteUninstaller "$INSTDIR\uninstall.exe"
  
  ; Add to Add/Remove Programs
  WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\nonunicodeconverter" "DisplayName" "${APPNAME}"
  WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\nonunicodeconverter" "UninstallString" '"$INSTDIR\uninstall.exe"'
  WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\nonunicodeconverter" "QuietUninstallString" '"$INSTDIR\uninstall.exe" /S'
SectionEnd

Section "Uninstall"
  Delete "$DESKTOP\${APPNAME}.lnk"
  Delete "$SMPROGRAMS\${APPNAME}\${APPNAME}.lnk"
  RMDir "$SMPROGRAMS\${APPNAME}"
  
  RMDir /r "$INSTDIR"
  
  DeleteRegKey HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\nonunicodeconverter"
SectionEnd
