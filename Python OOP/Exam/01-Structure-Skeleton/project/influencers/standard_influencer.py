from project.influencers.base_influencer import BaseInfluencer
from project.campaigns.base_campaign import BaseCampaign


class StandardInfluencer(BaseInfluencer):
    def __init__(self, username: str, followers: int, engagement_rate: float):
        super().__init__(username, followers, engagement_rate)
        self.payment_percentage = 0.45

    def calculate_payment(self, campaign: BaseCampaign) -> float:
        return campaign.budget * self.payment_percentage

    def reached_followers(self, campaign_type: str) -> int:
        if campaign_type == "HighBudgetCampaign":
            return int(self.followers * self.engagement_rate * 1.2)
        elif campaign_type == "LowBudgetCampaign":
            return int(self.followers * self.engagement_rate * 0.9)
