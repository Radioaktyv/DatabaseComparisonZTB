class Review:

    def __init__(
            self,
            ProductId,
            UserId,
            ProfileName,
            HelpfulnessNumerator,
            HelpfulnessDenominator,
            Score,
            Time,
            Summary,
            Text

    ):
        self.ProductId = ProductId
        self.UserId = UserId
        self.ProfileName = ProfileName
        self.HelpfulnessNumerator = HelpfulnessNumerator
        self.HelpfulnessDenominator = HelpfulnessDenominator
        self.Score = Score
        self.Time = Time
        self.Summary = Summary
        self.Text = Text
