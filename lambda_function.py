from folding_stats import get_and_publish_stats

def lambda_handler(event, context):
    get_and_publish_stats()
