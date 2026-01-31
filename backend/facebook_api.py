from fastapi import APIRouter
from pydantic import BaseModel

from facebook_audit import run_facebook_audit
from facebook_insights import generate_insights
from facebook_signals import extract_facebook_signals
from facebook_rules import (
    posting_consistency_score,
    content_activity_score,
    content_type_mix_score,
    engagement_health_score,
    final_facebook_audit_result
)

router = APIRouter()


class FacebookAuditRequest(BaseModel):
    page_input: str


@router.post("/audit/facebook")
def facebook_audit_endpoint(request: FacebookAuditRequest):
    """
    Facebook Audit API – V1
    Uses publicly visible signals & estimated patterns
    """

    page_info = run_facebook_audit(request.page_input)

    if page_info.get("status") != "success":
        return page_info

    signals = extract_facebook_signals(request.page_input)

    posting = posting_consistency_score(signals["last_post_date"])
    activity = content_activity_score(signals["posts_last_30_days"])
    content_mix = content_type_mix_score(signals["content_types"])
    engagement = engagement_health_score(
        likes=signals["likes"],
        comments=signals["comments"],
        shares=signals["shares"]
    )

    final_result = final_facebook_audit_result(
        posting_consistency=posting,
        content_activity=activity,
        content_type_mix=content_mix,
        engagement_health=engagement
    )

    insights = generate_insights(final_result["breakdown"])
    final_result["insights"] = insights

    return {
        "status": "success",
        "page": page_info.get("page_identifier"),
        "audit": final_result
    }
