from services.github_api_service import GitHubAPIServiceImpl

class GitHubServiceFactory:
    @staticmethod
    def create_service(username, token):
        return GitHubAPIServiceImpl(username, token)
