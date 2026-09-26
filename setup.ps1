mkdir "c:/timage/"

Remove-Item C:\timage\bin -Recurse -Force -ErrorAction SilentlyContinue
Move-Item .\bin C:\timage

[Environment]::SetEnvironmentVariable(
    "Path",
    $env:Path + ";C:\timage\bin",
    "User"
)

Remove-Item .\setup.ps1