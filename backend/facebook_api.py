from fastapi import APIRouter
from pydantic import BaseModel

from facebook_audit import run_facebook_audit
from facebook_signals import extract_facebook_signals
from facebook_rules import (
    posting_consistency_score,
    content_activity_score,
    content_type_mix_score,
    engagement_health_score,
    final_facebook_audit_result
)
from facebook_insights import generate_insights

router = APIRouter()


class FacebookAuditRequest(BaseModel):
    page_input: str


@router.post("/audit/facebook")
def facebook_audit_endpoint(request: FacebookAuditRequest):
    """
    Facebook Audit API – V1 (Simulated / Public Signals)
    """

    # STEP 1: Validate page input
    page_info = run_facebook_audit(request.page_input)
    if page_info["status"] != "success":
        return page_info

    # STEP 2: Generate deterministic signals (page-dependent)
    signals = extract_facebook_signals(request.page_input)

    # STEP 3: Scoring
    posting = posting_consistency_score(signals["last_post_date"])
    activity = content_activity_score(signals["posts_last_30_days"])
    content_mix = content_type_mix_score(signals["content_types"])
    engagement = engagement_health_score(
        likes=signals["likes"],
        comments=signals["comments"],
        shares=signals["shares"]
    )

    # STEP 4: Final result
    final_result = final_facebook_audit_result(
        posting_consistency=posting,
        content_activity=activity,
        content_type_mix=content_mix,
        engagement_health=engagement
    )

    # STEP 5: Insights
    final_result["insights"] = generate_insights(final_result["breakdown"])

    return {
        "status": "success",
        "page": page_info["page_identifier"],
        "audit": final_result
    }
