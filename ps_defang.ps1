function Defang-Url {
    param (
        [string]$Url
    )
    # Replace http/https, periods, and colons
    $defanged = $Url -replace 'https', 'hXXps' -replace 'http', 'hXXp'
    $defanged = $defanged -replace '\.', '[.]'
    $defanged = $defanged -replace ':', '[:]'
    return $defanged
}

# Example Usage
$maliciousUrl = "https://malware.com/payload"
Defang-Url -Url $maliciousUrl
# Output: hXXps[://]malware[.]com/payload
