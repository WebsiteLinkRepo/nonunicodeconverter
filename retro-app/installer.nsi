!include "MUI2.nsh"

!define APPNAME "nonunicodeconverter app"
!define APPEXE "retrozilla.exe"
!define APPURL "https://unicode2nonunicode.com"

Name "${APPNAME}"
OutFile "nonunicodeconverter-retro-setup.exe"
InstallDir "$PROGRAMFILES\nonunicodeconverter"
RequestExecutionLevel admin

; UI Settings
!define MUI_ABORTWARNING
!define MUI_ICON "..\src-tauri\icons\icon.ico"
!define MUI_UNICON "..\src-tauri\icons\icon.ico"

; Pages
!insertmacro MUI_PAGE_WELCOME
!insertmacro MUI_PAGE_DIRECTORY
!insertmacro MUI_PAGE_INSTFILES
!define MUI_FINISHPAGE_RUN "$INSTDIR\${APPEXE}"
!define MUI_FINISHPAGE_RUN_PARAMETERS "-url ${APPURL}"
!insertmacro MUI_PAGE_FINISH

!insertmacro MUI_UNPAGE_WELCOME
!insertmacro MUI_UNPAGE_CONFIRM
!insertmacro MUI_UNPAGE_INSTFILES
!insertmacro MUI_UNPAGE_FINISH

!insertmacro MUI_LANGUAGE "English"

Section "Install"
  SetOutPath "$INSTDIR"
  
  ; This assumes retrozilla-portable contents will be placed in the retro-app directory
  File /r "retrozilla-portable\*"
  File "..\src-tauri\icons\icon.ico"
  
  ; Create Desktop Shortcut with custom icon
  CreateShortCut "$DESKTOP\${APPNAME}.lnk" "$INSTDIR\${APPEXE}" "-url ${APPURL}" "$INSTDIR\icon.ico" 0
  
  ; Create Start Menu Shortcut with custom icon
  CreateDirectory "$SMPROGRAMS\${APPNAME}"
  CreateShortCut "$SMPROGRAMS\${APPNAME}\${APPNAME}.lnk" "$INSTDIR\${APPEXE}" "-url ${APPURL}" "$INSTDIR\icon.ico" 0
  
  ; Create Uninstaller
  WriteUninstaller "$INSTDIR\uninstall.exe"
  
  ; Add to Add/Remove Programs
  WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\nonunicodeconverter" "DisplayName" "${APPNAME} (Retro Windows)"
  WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\nonunicodeconverter" "DisplayIcon" "$INSTDIR\icon.ico"
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
