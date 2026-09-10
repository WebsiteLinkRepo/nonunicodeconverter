[Setup]
AppId={{5E4B5B6D-1D2A-4B6E-9C8F-7A8B9C0D1E2F}
AppName=Auto Font Changer
AppVersion=1.0.0
AppVerName=Auto Font Changer
AppPublisher=NonUnicodeConverter
AppPublisherURL=https://nonunicodeconverter.com
DefaultDirName={localappdata}\NonUnicodeConverter\AutoFontChanger
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

[Code]
var
  MaintenancePage: TInputOptionWizardPage;
  IsUpgrade: Boolean;
  UninstallPath: string;

procedure InitializeWizard;
begin
  IsUpgrade := False;
  
  if RegQueryStringValue(HKCU, 'Software\Microsoft\Windows\CurrentVersion\Uninstall\{#SetupSetting("AppId")}_is1', 'UninstallString', UninstallPath) then
  begin
    IsUpgrade := True;
    
    MaintenancePage := CreateInputOptionPage(wpWelcome,
      'Maintenance Mode', 'Auto Font Changer is already installed on your system.',
      'Please choose the maintenance operation you would like to perform:',
      True, False);
      
    MaintenancePage.Add('Repair installation (Fix missing files, shortcuts, and registry keys)');
    MaintenancePage.Add('Uninstall Auto Font Changer completely');
    
    MaintenancePage.Values[0] := True;
  end;
end;

function ShouldSkipPage(PageID: Integer): Boolean;
begin
  Result := False;
  if IsUpgrade and (PageID = wpSelectDir) then
    Result := True;
end;

function NextButtonClick(CurPageID: Integer): Boolean;
var
  ResultCode: Integer;
begin
  Result := True;
  
  if IsUpgrade and (CurPageID = MaintenancePage.ID) then
  begin
    if MaintenancePage.Values[1] then
    begin
      if MsgBox('Are you sure you want to completely remove Auto Font Changer from your system?', mbConfirmation, MB_YESNO) = idYes then
      begin
        UninstallPath := RemoveQuotes(UninstallPath);
        Exec(UninstallPath, '/SILENT', '', SW_SHOW, ewWaitUntilTerminated, ResultCode);
        Result := False;
        WizardForm.Close;
      end else
      begin
        Result := False;
      end;
    end;
  end;
end;
