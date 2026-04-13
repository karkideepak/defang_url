$url = "https://www.example.com/malicious"
$defanged = $url.Replace('https://', 'hXXps://').Replace('http://', 'hXXp://').Replace('.', '[.]')
Write-Output $defanged
# Output: hXXps://www[.]example[.]com/malicious
