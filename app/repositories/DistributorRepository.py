from app.repositories.db import db
from app.repositories.models import Distributor

class DistributorRepository():
    @staticmethod
    def get_session():
        return db.session

    @staticmethod
    def add_distributor(distributor):
        # db.session.add(distributor)
        # db.session.commit()
        # return distributor

        new_distributor = Distributor(**distributor)
        db.session.add(new_distributor)
        db.session.commit()
        return new_distributor

    @staticmethod
    def getAllDist():
        all = Distributor.query.all()
        return all

    @staticmethod
    def get_id_by_name(name):
        distributor = Distributor.query.filter_by(name = name).first()
        return distributor

    @staticmethod
    def get_dist(name):
        dist = Distributor.query.filter_by(name=name).first()
        return dist
    
    @staticmethod
    def get_dist_by_id(id):
        # distributor = Distributor.query.filter(Distributor.id == id).first()
        distributor = Distributor.query.get(id)
        return distributor
    
    @staticmethod
    def update_distributor(session, args):
        distributor = DistributorRepository.get_dist_by_id(args['id'])
        if distributor.name != args['name']:
           distributor.name = args['name']
        distributor.address = args['address']
        distributor.contact = args['contact']
        session.commit()
        

        
