import pymongo

client = pymongo.MongoClient('mongodb://127.0.0.1:27017/')

mydb = client['Employee']

information = mydb.employeeinfo

record = {
    'firstnamr':'bilal',
    'lastname':'momin',
    'department':'data science'
}

information.insert_one(record)

#for multiple records use list of json

records = [
    {
    'firstnamr':'bilal',
    'lastname':'momin',
    'department':'data science'
    },
    {
    'firstnamr':'bilal1',
    'lastname':'momin1',
    'department':'data science1'
    },
    {
    'firstnamr':'bilal2',
    'lastname':'momin2',
    'department':'data science2'
    }
]

information.insert_many(records)

