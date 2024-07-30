class NonFollowersFinder:
    def __init__(self, service):
        self.service = service

    def find_non_followers(self):
        followers = set(self.service.get_followers())
        following = set(self.service.get_following())
        return list(following - followers)
