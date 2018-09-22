# CSESoc Hackathon project

## List of API routes
## Get a list of all open groups
GET /group/

Returns a list of all the groups
```json
{
  "groups": [
  {
    "id": int,
    "name": string,
    "location": string,
    "description": string,
    "course codes": [],
    "time": unix timestamp,
    "convenor": userID,
    "attendees": [userID, ...],
    "maxCapacity": int,
    "privacyLevel": int
    },
    ...
    ]
}
```
## Get particular group
GET /group/<id>

returns
```json
{
    "id": int,
  "name": string,
  "location": string,
  "description": string,
  "course codes": [],
  "time": unix timestamp,
  "convenor": userID,
  "attendees": [userID, ...],
  "maxCapacity": int,
  "privacyLevel": int
}
```

## Get a particular user
GET /user/<id>
returns
```json
{
  "fname": "string",
  "lname": "string",
  "username": "string",
  "subjects": [
    {
      "courseCode": "course1",
      "mark": "mark1"
    },
   {
      "courseCode": "course2",
      "mark": "mark2"
    }
  ]
}
```
  
  ### Subjects
  GET /user/<id>/subjects
  returns
  ```
   [
    {
        "courseCode": "COMP1511",
        "mark": "DN"
    },
    {
        "courseCode": "COMP1521",
        "mark": "CR"
    },
    {
        "courseCode": "COMP3331",
        "mark": "CR"
    }
]
  
POST /usr/<id>/subjects
body
{
  "courseCode": "COMP1511",
  "mark": "DN"
}
returns
(same as above)
