mkdir "c:/timage/"
Move-Item .\bin c:/timage

[Environment]::SetEnvironmentVariable(
    "Path",
    $env:Path + ";C:\timage\bin",
    "User"
)

Remove-Item .\setup.ps1