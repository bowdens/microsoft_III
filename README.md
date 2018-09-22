# CSESoc Hackathon project

## List of API routes
## Get a list of all open groups
GET /group/  
Returns a list of all the groups

```json
{
    "1": {
        "course_code": [
            "COMP1511",
            "COMP1521"
        ],
        "description": "description",
        "location": "location",
        "max_capacity": 5,
        "name": "name"
    },
    "2": {
        "course_code": [
            "COMP3331",
            "COMP6841"
        ],
        "description": "test description",
        "location": "test location",
        "max_capacity": 3,
        "name": "test group"
    }
}
```
## Get particular group
GET /group/\<id\>  
returns  

```json
{
    "course_code": [
        "COMP1511",
        "COMP1521"
    ],
    "description": "description",
    "location": "location",
    "max_capacity": 5,
    "name": "name"
}
```

## Get a particular user
GET /user/\<id\>  
returns
  
```json
{
    "fname": "first",
    "lname": "last",
    "username": "tester",
    "subjects": [
        {
            "courseCode": "COMP1511",
            "mark": "DN"
        },
        {
            "courseCode": "COMP1521",
            "mark": "CR"
        }
    ]
}
```
  
  ## Create new user
  POST /user/\<id\>  
  body
  
  ```json
  {
    "fname": "first name",
    "lname": "last name",
    "username": "username",
    "password": "plaintext password"
    }
  ```
  returns
  same as above
  
  ### Subjects
  GET /user/\<id\>/subjects  
  returns
  
  ```json
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
```
  
POST /user/\<id\>/subjects  
body

  ```json
{
  "courseCode": "COMP1511",
  "mark": "DN"
}
  ```
returns
(same as above)

## User Validation
POST /validate   
body
```json
{
  "username": "username",
  "password": "plaintext password"
}
```
returns
true OR false

## Register for group
POST /group/\<groupID\>  
body

```json
{
  "username": "username"
}
```

returns the same as GET /group/\<groupID\>
same as 
