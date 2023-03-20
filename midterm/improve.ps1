# improve the following code

function printa($a) {Write-Host "First Name: $a"}

function printb($b) {Write-Host "Last Name: $b"}

function printc($c) {Write-Host "Address: $c"}

function printd($d) {Write-Host "City: $d"}

function printe($e) {Write-Host "State: $e"}

Write-Host "### User Information ###"

printa "Nigel"
printb "Nighthawk"
printc "3820 Mundy Mill Rd"
printd "Oakwood"
printe "Georgia"

# improve the code provided above

function printUserInfo($firstName, $lastName, $address, $city, $state) {
    Write-Host "### User Information ###"
    Write-Host "First Name: $firstName"
    Write-Host "Last Name: $lastName"
    Write-Host "Address: $address"
    Write-Host "City: $city"
    Write-Host "State: $state"
}

printUserInfo "Nigel" "Nighthawk" "3820 Mundy Mill Rd" "Oakwood" "Georgia"

# Variables represent data that can be referenced inside a script or program. 
# Write the correct syntax for creating a variable in PowerShell and assigning the value "Elite H@ck3r!" to it

$var = "Elite H@ck3r!"
