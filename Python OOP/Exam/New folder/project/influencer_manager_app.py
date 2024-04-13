from project.campaigns.base_campaign import BaseCampaign
from project.campaigns.high_budget_campaign import HighBudgetCampaign
from project.campaigns.low_budget_campaign import LowBudgetCampaign
from project.influencers.base_influencer import BaseInfluencer
from project.influencers.premium_influencer import PremiumInfluencer
from project.influencers.standard_influencer import StandardInfluencer


class InfluencerManagerApp:
    def __init__(self):
        self.influencers = []
        self.campaigns = []

    def register_influencer(
        self,
        influencer_type: str,
        username: str,
        followers: int,
        engagement_rate: float,
    ):
        if influencer_type not in ["PremiumInfluencer", "StandardInfluencer"]:
            return f"{influencer_type} is not an allowed influencer type."

        for influencer in self.influencers:
            if influencer.username == username:
                return f"{username} is already registered."

        if influencer_type == "PremiumInfluencer":
            influencer = PremiumInfluencer(username, followers, engagement_rate)
        else:
            influencer = StandardInfluencer(username, followers, engagement_rate)

        self.influencers.append(influencer)
        return f"{username} is successfully registered as a {influencer_type}."

    def create_campaign(
        self,
        campaign_type: str,
        campaign_id: int,
        brand: str,
        required_engagement: float,
    ):
        if campaign_type not in ["HighBudgetCampaign", "LowBudgetCampaign"]:
            return f"{campaign_type} is not a valid campaign type."

        for campaign in self.campaigns:
            if campaign.campaign_id == campaign_id:
                return f"Campaign ID {campaign_id} has already been created."

        if campaign_type == "HighBudgetCampaign":
            campaign = HighBudgetCampaign(campaign_id, brand, required_engagement)
        else:
            campaign = LowBudgetCampaign(campaign_id, brand, required_engagement)

        self.campaigns.append(campaign)
        return f"Campaign ID {campaign_id} for {brand} is successfully created as a {campaign_type}."

    def participate_in_campaign(self, influencer_username: str, campaign_id: int):
        influencer = None
        for inf in self.influencers:
            if inf.username == influencer_username:
                influencer = inf
                break
        if influencer is None:
            return f"Influencer '{influencer_username}' not found."

        campaign = None
        for cmp in self.campaigns:
            if cmp.campaign_id == campaign_id:
                campaign = cmp
                break
        if campaign is None:
            return f"Campaign with ID {campaign_id} not found."

        if not campaign.check_eligibility(influencer.engagement_rate):
            return f"Influencer '{influencer_username}' does not meet the eligibility criteria for the campaign with ID {campaign_id}."

        payment = influencer.calculate_payment(campaign)
        if payment > 0.0:
            campaign.approved_influencers.append(influencer)
            campaign.budget -= payment
            influencer.campaigns_participated.append(campaign)
            return f"Influencer '{influencer_username}' has successfully participated in the campaign with ID {campaign_id}."

    def calculate_total_reached_followers(self):
        total_reached_followers = {}
        for campaign in self.campaigns:
            reached_followers = sum(
                [
                    inf.reached_followers(type(campaign).__name__)
                    for inf in campaign.approved_influencers
                ]
            )
            if reached_followers > 0:
                total_reached_followers[campaign] = reached_followers
        return total_reached_followers

    def influencer_campaign_report(self, username: str):
        for influencer in self.influencers:
            if influencer.username == username:
                return influencer.display_campaigns_participated()
        return f"{username} has not participated in any campaigns."

    def campaign_statistics(self):
        sorted_campaigns = sorted(
            self.campaigns, key=lambda x: (len(x.approved_influencers), -x.budget)
        )
        statistics = []
        for campaign in sorted_campaigns:
            total_reached_followers = sum(
                [
                    inf.reached_followers(type(campaign).__name__)
                    for inf in campaign.approved_influencers
                ]
            )
            statistics.append(
                f"  * Brand: {campaign.brand}, Total influencers: {len(campaign.approved_influencers)}, Total budget: ${campaign.budget:.2f}, Total reached followers: {total_reached_followers}"
            )
        return "$$ Campaign Statistics $$\n" + "\n".join(statistics)
