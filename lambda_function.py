def lambda_handler(event, context):   
    items = [{
            "name":"Buy Milk",
            "status":"Complete",
            "id":1
        },
        {
            "name":"phone bill",
            "status":"active",
            "id":2
        }
    ]
    return items