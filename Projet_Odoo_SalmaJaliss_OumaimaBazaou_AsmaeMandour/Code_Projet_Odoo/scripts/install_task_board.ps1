param(
  [string]$OdooServerDir = 'C:\Program Files\Odoo 18.0.20251014\server',
  [string]$DbName = 'TP',
  [string]$Module = 'task_board'
)
$ErrorActionPreference = 'Stop'
$odooBin = Join-Path $OdooServerDir 'odoo-bin'
$python = 'C:\Program Files\Odoo 18.0.20251014\python\python.exe'
$conf = Join-Path $OdooServerDir 'odoo.conf'
$log = Join-Path $OdooServerDir 'odoo.log'
$moduleDir = Join-Path $OdooServerDir 'odoo\addons\task_board'
Write-Host "Checking module directory: $moduleDir"
if (-not (Test-Path $moduleDir)) { throw "Module directory not found: $moduleDir" }
Write-Host "Installing module $Module on database $DbName"
& $python $odooBin -c $conf -d $DbName -i $Module --without-http --stop-after-init
Start-Sleep -Seconds 2
Write-Host "Log verification ($log)"
$patterns = @('addons paths', 'Installing', 'module', $Module, 'ERROR', 'WARNING')
Select-String -Path $log -Pattern $patterns -SimpleMatch | Select-Object -First 100 | Write-Output
Write-Host "Completed. Restart Odoo Desktop, update apps list, then search: $Module"
