class BaseInfluencer:
    def __init__(self, username: str, followers: int, engagement_rate: float):
        if not username.strip():
            raise ValueError('Username cannot be empty or consist only of whitespace!')
        if followers < 0:
            raise ValueError('Followers must be a non-negative integer!')
        if not (0.0 <= engagement_rate <= 5.0):
            raise ValueError('Engagement rate should be between 0 and 5.')

        self.username = username
        self.followers = followers
        self.engagement_rate = engagement_rate
        self.campaigns_participated = []

    def calculate_payment(self, campaign) -> float:
        raise NotImplementedError('Subclasses must implement calculate_payment method.')

    def reached_followers(self, campaign_type: str) -> int:
        raise NotImplementedError('Subclasses must implement reached_followers method.')

    def display_campaigns_participated(self) -> str:
        if not self.campaigns_participated:
            return f"{self.username} has not participated in any campaigns."

        result = f"{type(self).__name__} :) {self.username} :) participated in the following campaigns:\n"
        for campaign in self.campaigns_participated:
            result += f"  - Campaign ID: {campaign.campaign_id}, Brand: {campaign.brand}, Reached followers: {self.reached_followers(type(campaign).__name__)}\n"
        return result.strip()
