# curl --header "Content-Type: application/json"  --request POST  --data f'{sample_doctor}'  http://localhost:5000/doctor

import unittest
from models import Doctor,Area,DoctorQuery

class DoctorTest(unittest.TestCase):
    single_doctor = {
        "name":"Amit Shah",
        "category":"General Physican",
        "consultation_fees": 230,
        "area":[{
            "district":"xyz",
            "city":"abc",
            "state":"",
            "country":"india",
            "postalcode":"54353"
        },],
        "language":['English']
    }

    bulk_doctors = [{
        "name":"Amit Shah",
        "category":"General Physican",
        "consultation_fees": 230,
        "area":[{
            "district":"xyz",
            "city":"abc",
            "state":"",
            "country":"india",
            "postalcode":"54353"
        },],
        "language":['English']
    },
    {
        "name":"Sachin Tendulkar",
        "category":"General Physican",
        "consultation_fees": 500,
        "area":[{
            "district":"xyz",
            "city":"abc",
            "state":"",
            "country":"india",
            "postalcode":"54353"
        },],
        "language":['English','Marathi']
    },
    ]

    def test_revenueByCompany(self):
        self.assertEqual(DoctorQuery.filterQuery(maxPrice=500), {"consultation_fees":{"$gt": 0 , "$lt": 500}}, 'Incorrect query string')
        print('ok')

if __name__ == '__main__':
    unittest.main()