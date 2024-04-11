class BaseCampaign:

    campaign_unique_ids = set()
    def __init__(self, campaign_id: int, brand: str, budget: float, required_engagement: float):

        if campaign_id <= 0:
            raise ValueError('Campaign ID must be a positive integer greater than zero.')
        if campaign_id in BaseCampaign.campaign_unique_ids:
            raise ValueError(f'Campaign with ID {campaign_id} already exists. Campaign IDs must be unique.')
        BaseCampaign.campaign_unique_ids.add(campaign_id)

        self.campaign_id = campaign_id
        self.brand = brand
        self.budget = budget
        self.required_engagement = required_engagement
        self.approved_influencers = []

    def check_eligibility(self,engagement_rate: float):
        raise NotImplementedError('Subclasses must implement check_eligibility method.')