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
