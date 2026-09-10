[Setup]
AppName=Auto Font Changer
AppVersion=1.0.0
AppVerName=Auto Font Changer
AppPublisher=NonUnicodeConverter
AppPublisherURL=https://nonunicodeconverter.com
DefaultDirName={localappdata}\NonUnicodeConverter\PageMakerAutoFontChanger
DefaultGroupName=NonUnicodeConverter
DisableProgramGroupPage=yes
OutputBaseFilename=AutoFontChangerSetup
Compression=lzma
SolidCompression=yes
PrivilegesRequired=lowest
OutputDir=Output
SetupIconFile=setup.ico
WizardImageFile=WizardImageFile.bmp
WizardSmallImageFile=WizardSmallImageFile.bmp

[Files]
Source: "..\pagemaker-helper\target\i686-pc-windows-msvc\release\pgmkrautofontchanger.exe"; DestDir: "{app}"; DestName: "pgmkrautofontchanger.exe"; Flags: ignoreversion

[Registry]
Root: HKCU; Subkey: "Software\Classes\nonunicode"; ValueType: string; ValueName: ""; ValueData: "URL:NonUnicode Custom Protocol"; Flags: uninsdeletekey
Root: HKCU; Subkey: "Software\Classes\nonunicode"; ValueType: string; ValueName: "URL Protocol"; ValueData: ""; Flags: uninsdeletekey
Root: HKCU; Subkey: "Software\Classes\nonunicode\shell"; Flags: uninsdeletekey
Root: HKCU; Subkey: "Software\Classes\nonunicode\shell\open"; Flags: uninsdeletekey
Root: HKCU; Subkey: "Software\Classes\nonunicode\shell\open\command"; ValueType: string; ValueName: ""; ValueData: """{app}\pgmkrautofontchanger.exe"" ""%1"""; Flags: uninsdeletekey

[Icons]
Name: "{group}\Uninstall Auto Font Changer"; Filename: "{uninstallexe}"
