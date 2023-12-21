import requests

url = "http://216.10.245.166/Library/Addbook.php"
payload = {
"name":"Learn Appium Automation with Java",
"isbn":"Ram",
"aisle":"237",
"author":"John foe"
}
response = requests.post(url, json=payload)

print(response.text)



