import pprint
from ttd_workflows import Workflows

WORKFLOWS_TTD_AUTH="CgsInrKh+7WamT4QBRIHaDdzbzA1MBogZy58akhEXDFVNFsjQitMXFFgfD8sMyNifj16ci5yZCsgAQ=="

# with Workflows(
#     ttd_auth=WORKFLOWS_TTD_AUTH, #os.getenv("WORKFLOWS_TTD_AUTH", ""),
#     # server="sandbox"
# ) as workflows:

#     campaign_id = "001qobs"

#     try:
#         res = workflows.campaign.get_version(id=campaign_id)
#         print(f"Response type: {type(res)}")
#         print(f"Response content: {res}")
#         if not res or (hasattr(res, 'id') and not res.id):
#             print("Warning: Received empty response from sandbox environment")
#     except ProblemDetailsError as e:
#         print(f"Getting campaign {campaign_id} failed with: {e.data.title}")
#         print(f"Error details: {e.data}")
#     except Exception as e:
#         print(f"Unexpected error: {type(e).__name__}: {str(e)}")
#         breakpoint()



# with Workflows(
#     ttd_auth=WORKFLOWS_TTD_AUTH, #os.getenv("WORKFLOWS_TTD_AUTH", ""), ttd_auth=os.getenv("WORKFLOWS_TTD_AUTH", "")
# ) as workflows:

#     partner_id = "056uhe3"
#     query_shape = "nodes {id name}"

#     res = workflows.dmp.get_third_party_data_job(request={
#         "partner_id": partner_id,
#         "query_shape": query_shape
#     })

#     # Handle response
#     print(res.id)


with Workflows(
    ttd_auth=WORKFLOWS_TTD_AUTH, #os.getenv("WORKFLOWS_TTD_AUTH", ""), ttd_auth=os.getenv("WORKFLOWS_TTD_AUTH", "")
) as workflows:

    # resStatus = workflows.job_status.get_job_status(id=res.id)
    resStatus = workflows.job_status.get_job_status(id=42)

    # Handle response
    pprint.pprint(resStatus)
    breakpoint()


# import os
# import ttd_workflows
# from ttd_workflows import Workflows
# from ttd_workflows.utils import parse_datetime


# with Workflows(
#     ttd_auth=os.getenv("WORKFLOWS_TTD_AUTH", ""),
#     server="sandbox"
# ) as workflows:

#     res = workflows.campaign.create(request={
#         "primary_input": {
#             "description": "The description of this campaign",
#             "time_zone": "Europe/Ulyanovsk",
#             "budget": {
#                 "pacing_mode": ttd_workflows.CampaignPacingMode.PACE_AS_SOON_AS_POSSIBLE,
#                 "budget_in_advertiser_currency": 6000,
#                 "budget_in_impressions": 500,
#                 "daily_target_in_advertiser_currency": 1000,
#                 "daily_target_in_impressions": 200,
#             },
#             "seed_id": "dgqkv002",
#             "advertiser_id": "9u3bhb7",
#             "name": "The name of my campaign",
#             "primary_channel": ttd_workflows.CampaignChannelType.DOOH,
#             "primary_goal": {
#                 "maximize_reach": True
#             },
#             "start_date_in_utc": parse_datetime("2025-07-05T18:10:41.123+00:00")
#         }
#     })

#     # Handle response
#     print(res)
