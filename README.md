# RA-API

A simple API for data querying.  
The project is deployed and hosted on Heroku.

## Usage

Main site: `https://ra-api.herokuapp.com/`  
Query Full Record By HID `GET https://ra-api.herokuapp.com/api/query/hid/<hid>`  
Query Parts of Record By HID `POST https://ra-api.herokuapp.com/api/query`

* Access by `curl`  

```
# Query Full Record By HID
curl -i https://ra-api.herokuapp.com/api/query/hid/3126F2F5F8QR5N1OVUZEMNGHF0EPEO
```

```
# Query Parts of Record By HID
curl -H "Content-Type: application/json" -d '{"hid": "3GV1I4SEO9CX1NTBXKN9TIFKTSQ6LN", "res_hid": true, "res_content":true, "res_has_space": true}' https://ra-api.herokuapp.com/api/query
```

## API Specification
### Query Full Record By HID

Returns the full record with the given “hid”

**URL** : `/api/query/hid/<hid>`

**URL Parameters**:  

| Name | Required | Description  | Example |
|:-----|:--------- |:----------- |:--------|
| hid  | Required | The *hid* of the record.|33BFF6QPI1YEFYISIWWDVQKGH8RW3Z|

**Method** : `GET`

**Data constraints** : `hid` should be `string` type

**Example Request**:
`GET http://127.0.0.1:5000/api/query/hid/33BFF6QPI1YEFYISIWWDVQKGH8RW3Z`

#### Success Responses

**Condition** : Exists a record with the given HID.

**Code** : `200 OK`

**Response Type**: json

**Response Content Example** :
```json
{
  "result": {
        "hid": "33BFF6QPI1YEFYISIWWDVQKGH8RW3Z",
        "content": "Landmark Center, 8th Fl",
        "has_space": false     
  }
}
```
#### Failed Responses

**Condition**: Fail to find a record with the given HID.

**Code**: `404 Not Found`

**Response Type**: json
**Response Content Example** :
```json
{
  "message": "[Err] 404 Not Found.", 
  "status": 404
}
```

### Query Parts of Record By HID

Returns parts of record with the given “hid” and display parameters

**URL** : `/api/query`

**URL Parameters**:

| Name | Required | Description  | Default value | Example |
|:-----|:--------- |:----------- |:--------------| :-------|
| hid  | Required | The *hid* of the record.|  |33BFF6QPI1YEFYISIWWDVQKGH8RW3Z|
| res_hid | Optional | Whether to return `hid` field when response | false | true |
| res_content | Optional | Whether to return `content` field when response | false | true |
| res_has_space | Optional | Whether to return `has_space` field when response | false | true |

**Method** : `POST`

**Data constraints** :

**Example Request**:
```
POST http://127.0.0.1:5000/api/query  
Content-Type:application/json
Accept:application/json	

{
    'hid': 32L724R85L73LS3ARDP572E97TLPIX,
    'res_hid': true,
    'res_content': true
}
```

#### Success Responses

**Condition** : Exists a record with the given HID.

**Code** : `200 OK`

**Response Type**: json

**Response Content Example** :
Note: `result` only contains fields that are specified in the given parameters.
```json
{
  "result": {
        "hid": "33BFF6QPI1YEFYISIWWDVQKGH8RW3Z",
        "content": "Landmark Center, 8th Fl",
        "has_space": false     
  }
}
```
#### Failed Responses

**Condition**: Fail to find a record with the given HID.

**Code**: `404 Not Found`

**Response Type**: json
**Response Content Example** :
```json
{
  "message": "[Err] 404 Not Found.", 
  "status": 404
}
```

## Getting Started
### Prerequisites  
* Install Virtualenv 
```commandline
pip install virtualenv
```

### Installing
Under the project directory
* Create the virtual environment
```commandline
virtualenv ./
```
* Activate the virtual environment
```commandline
source ./bin/activate
```
* install dependencies
```commandline
pip install -r requirements.txt
```

### Configuration
* Initialize the database
```commandline
python manage.py init
```
* Migrate the database
```commandline
python manage.py migrate
```
* Upgrade the database
```commandline
python manage.py upgrade
```

### Start
Under the project directory
* Start server
```commandline
python manage.py runserver
```



