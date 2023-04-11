DATABASE = {
    "animals": [
        {
            "id": 1,
            "name": "Snickers",
            "species": "Dog",
            "locationId": 1,
            "customerId": 4,
            "status": "Admitted"
        },
        {
            "id": 2,
            "name": "Roman",
            "species": "Dog",
            "locationId": 1,
            "customerId": 2,
            "status": "Admitted"
        },
        {
            "id": 3,
            "name": "Blue",
            "species": "Cat",
            "locationId": 2,
            "customerId": 1,
            "status": "Admitted"
        }
    ],
    "customers": [
        {
            "id": 1,
            "name": "Ryan Tanay"
        }
    ],
    "employees": [
        {
            "id": 1,
            "name": "Jenna Solis"
        }
    ],
    "locations": [
        {
            "id": 1,
            "name": "Nashville North",
            "address": "8422 Johnson Pike"
        },
        {
            "id": 2,
            "name": "Nashville South",
            "address": "209 Emory Drive"
        }
    ]
}


def all(resource):
    """For GET requests to collection"""
    response = DATABASE[resource]
    return response

def retrieve(resources, id):
    """For GET requests to a single resource"""
    response = None
    for resource in DATABASE[resources]:
        if resource["id"] == id:
            response = resource

    return response

def create(type, resource):
    """For POST requests to a collection"""
    max_id = DATABASE[type][-1]["id"]

    new_id = max_id + 1

    resource["id"] = new_id

    DATABASE[type].append(resource)

    return resource


def update(id, type, new_resource):
    """For PUT requests to a single resource"""
    for index, resource in enumerate(DATABASE[type]):
        if resource["id"] == id:
            # Found the resource. Update the value.
            DATABASE[type][index] = new_resource
            break


def delete(id, type):
    """For DELETE requests to a single resource"""
    # Initial -1 value for resource index, in case one isn't found
    resource_index = -1

    # Iterate the type list, but use enumerate() so that you
    # can access the index value of each item
    for index, resource in enumerate(DATABASE[type]):
        if resource["id"] == id:
            # Found the resource. Store the current index.
            resource_index = index

    # If the resource was found, use pop(int) to remove it from list
    if resource_index >= 0:
        DATABASE[type].pop(resource_index)
