git status
git add .
$now = get-date -Format 'yyyy-MM-dd HH:mm:ss'
git commit -m "update $now"
git push

Write-Host "Date: $now"

