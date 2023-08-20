$branchName = "main"  # Replace with your branch name

Write-Host "Enter your commit message:"
$commitMessage = Read-Host

Write-Host "Enter your code:"
$code = Read-Host
$filePath = "code.py"

Add-Content -Path $filePath -Value $code

git add --all
git commit -m "$commitMessage"
git push origin $branchName
