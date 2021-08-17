from dataclasses import dataclass, field
import json
import typing

@dataclass
class Area:
    district:str=''
    city:str=''
    state:str=''
    country:str=''
    postalcode:str=''

    def toJson(self):
        return json.dumps(self.__dict__, default=lambda x: x.__dict__, indent=4)
    
    @staticmethod
    def fromJsonDict(cls, data):
        if isinstance(data, dict): # single record
            return [Area(**data)]
        else:
            out = []
            for d in data:
                out.append( Area.fromJsonDict(d) )
            return out
    
    def isValid(self):
        return False if not all([self.district, self.city, self.state, self.country, self.postalcode]) else True            

@dataclass
class Doctor:
    name:str
    category:str
    consultation_fees:float
    area:typing.List[Area] = field(default_factory=lambda: [Area()])
    language:typing.List[str] = field(default_factory=lambda: ['English'])
    
    def toJson(self):
        return json.dumps(self.__dict__, default=lambda x: x.__dict__, indent=4)
    
    @staticmethod
    def fromJsonDict(cls, data):
        if isinstance(data, dict): # single record
            area = data.pop('area',[])
            area = Area.fromJsonDict(area)
            data['area'] = area
            return [Doctor(**area)]
        else:
            out = []
            for d in data:
                out.append( Doctor.fromJsonDict(d) )
            return out

class DoctorQuery:
    
    @staticmethod
    def filterQuery(**kwargs):
        district = kwargs.get('district')
        category = kwargs.get('category')
        maxPrice = kwargs.get('maxPrice',999999999999999)
        minPrice = kwargs.get('minPrice',0)
        language = kwargs.get('language')
        query = {}
        query["consultation_fees"] =  { "$gt": minPrice , "$lt": maxPrice }
        if district:
            query['district'] = f'/{district}/'
        if category:
            query['category'] = f'{category}'
        if language:
            query['language'] = f'{language}'
        return query


