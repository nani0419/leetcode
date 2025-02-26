# git status
# git add .
# $now = get-date -Format 'yyyy-MM-dd HH:mm:ss'
# git commit -m "update $now"
# git push

# Write-Host "Date: $now"

# Step 1: Display current git status
git status

# Step 2: Prompt user to proceed with adding changes
$addChanges = Read-Host "Do you want to add all changes to the staging area? (y/n)"

if ($addChanges -eq 'y') {
    git add .
    Write-Host "Changes added to staging area."
} else {
    Write-Host "No changes added."
}

# Step 3: Prompt user for a commit message (can default to the current date and time)
$now = Get-Date -Format 'yyyy-MM-dd HH:mm:ss'
$commitMessage = Read-Host "Enter commit message (default is 'update $now')"

if ([string]::IsNullOrWhiteSpace($commitMessage)) {
    $commitMessage = "update $now"
}

# Step 4: Commit with the provided message
git commit -m $commitMessage
Write-Host "Committed with message: '$commitMessage'"

# Step 5: Prompt user to push to the repository
$pushChanges = Read-Host "Do you want to push the changes to the remote repository? (y/n)"

if ($pushChanges -eq 'y') {
    git push
    Write-Host "Changes pushed to the remote repository."
} else {
    Write-Host "Changes not pushed."
}

# Step 6: Output the current date and time
Write-Host "Date: $now"
