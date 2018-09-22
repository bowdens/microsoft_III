# CSESoc Hackathon project

## List of API routes
## Get a list of all open groups
GET /group/

Returns a list of all the groups

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

## Get particular group
GET /group/<id>

returns
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

## Get a particular user
GET /user/<id>
returns
{
  "id": int,
  "fName": string,
  "lName": string,
  "courses": [
    {
      "courseCode": string,
      "mark": "HD" | "DN" | "CR" | "PS" | "FL"| "ON"
    }, 
    ...
  ]
}
