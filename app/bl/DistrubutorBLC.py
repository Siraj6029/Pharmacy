from app.repositories.DistributorRepository import DistributorRepository

class Distributorblc():
    @staticmethod
    def update_distributor(distributor):
        session = DistributorRepository.get_session()
        distributor = DistributorRepository.update_distributor(session, distributor)
        