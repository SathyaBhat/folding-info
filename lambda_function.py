from folding_stats import get_and_publish_stats
VERSION="2.0.0"

def lambda_handler(event, context):
    print(f"Starting F@H stats lambda version {VERSION}")
    get_and_publish_stats()
    print(f"Goodbye!")