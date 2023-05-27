# task_8_Selene
using Selene
Data
Interface of a DB is presented in https://my-json-server.typicode.com/IlyaKnysh/fake_db

By executing the following query, you need to get the structure of the test database in json format

GET /IlyaKnysh/fake_db/db? HTTP/1.1
Host: my-json-server.typicode.com
accept-encoding: gzip, deflate
Connection: keep-alive
cache-control: no-cache
Task
You need to write tests that will compare the data on the UI with the data in json:

1. Check DB name
2. Check author name
3. Check if the number of objects in json matches the number of resources on the UI
4. Check:
- if the resource is represented by a list of objects - the UI displays the number of list items next to the resource name
- if represented by a single object - next to the name of the resource on the UI, the label "object" is displayed
5. Check that clicking on each resource opens a page with objects from the corresponding json element
6. Check that when the next request is sent

POST /IlyaKnysh/fake_db/ad_zones? HTTP/1.1
Host: my-json-server.typicode.com
Content-Type: application/json
accept-encoding: gzip, deflate
Connection: keep-alive
cache-control: no-cache
{
"id": 11111,
"zone": "intersitial",
"type": "interstitial_rewarded_video"
}
- new zone is displayed in database structure json
- the new zone increases the number of list items next to the name of the corresponding resource on the UI

Additional requirements
Use library Selene for UI automation
Use Webdriver Manager
Use requests library for API interactions
Use a decorator that will check the success of all API responses
Add logging of sent requests and received API responses
