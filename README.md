# RA-API

A simple API for data querying.  
The project is deployed and hosted on Heroku.

## Usage

Main site: `https://ra-api.herokuapp.com/`  
Query Full Record By HID `GET https://ra-api.herokuapp.com/api/query/hid/<hid>`  


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



