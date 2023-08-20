$branchName = "main"  # Replace with your branch name

Write-Host "Enter your commit message:"
$commitMessage = Read-Host

git add .
git commit -m "$commitMessage"
git push origin $branchName
